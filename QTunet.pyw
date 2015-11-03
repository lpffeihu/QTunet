# -*- coding: utf8 -*-
# author: feihu
# author email: lpffeihu (a.t) gmail.com

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import mainUI
import about
import sys
import urllib, urllib2
import hashlib
import time

Title = 'QTunet v0.03'
LoginAddr = 'http://net.tsinghua.edu.cn/do_login.php'
CheckPostData = 'action=check_online'
LoginPostData = "action=login&username=%s&password={MD5_HEX}%s&ac_id=1"
RadInfoAddr = 'http://net.tsinghua.edu.cn/rad_user_info.php'
LogoutAddr = 'http://net.tsinghua.edu.cn/do_login.php?action=logout'
InfoAddr = 'http://net.tsinghua.edu.cn/user_info1.php'
INTERVAL=10000

class mainUIGUI(QDialog,
        mainUI.Ui_Dialog):
    def __init__(self, parent=None):
        self._shouldHide = False
        self.initializing = True
        self.md5ed = False
        self.password = ''
        self.username = ''
        self.usedQuota = ''
        super(mainUIGUI, self).__init__(parent)
        self.__index = 0
        self.setupUi(self)
        self.setWindowTitle(Title)
        self.txtPassword.setEchoMode(QLineEdit.Password)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.connect(self.ckSavepassword, SIGNAL("toggled(bool)"),
                self.togglePassword)
        self.connect(self.txtPassword, SIGNAL("textEdited(QString)"),
                self.passwordChanged)
        self.connect(self.btnLogin, SIGNAL("clicked()"), self.login)
        self.connect(self.txtPassword, SIGNAL("returnPressed()"), self.login)
        self.connect(self.btnLogout, SIGNAL("clicked()"), self.logout)
        # self.connect(self.btnMystate, SIGNAL("clicked()"), self.showXX)
        self.connect(self.btnAbout, SIGNAL("clicked()"), self.showXX)
        #timer
        self.timer=QTimer()
        QObject.connect(self.timer,SIGNAL("timeout()"), self.OnTimer)
        #saved username and password
        self.showState()
        self.loadState()
        #tray icon
        icon = QIcon("icon.ico")
        self.setWindowIcon(icon)
        self.isTopLevel()
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(icon)
        self.trayIcon.show()
        self.trayIcon.activated.connect(self.trayClick) #点击托盘
        self.trayIcon.setToolTip('mainUI') #托盘信息
        self.Menu() #右键菜单

    def shouldHide(self):
        return self._shouldHide

    def Menu(self):
        self.minimizeAction = QAction(u"最小化", self,triggered=self.hide)
        #self.maximizeAction = QAction(u"最大化",self,triggered=self.showMaximized)
        self.restoreAction = QAction(u"还原", self,triggered=self.showNormal)
        self.quitAction = QAction(u"退出", self,triggered=self.close)
        #self.quitAction = QAction(u"退出", self,triggered=qApp.quit)
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(self.minimizeAction)
        #self.trayIconMenu.addAction(self.maximizeAction)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addSeparator() #间隔线
        self.trayIconMenu.addAction(self.quitAction)
        self.trayIcon.setContextMenu(self.trayIconMenu) #右击托盘

    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange and \
                self.isMinimized() and self.trayIcon.isVisible():
            QTimer.singleShot(0, self, SLOT("hide()"))
        else:
            event.accept()
            #event.accept()

#     def closeEvent(self, event):
#         if self.trayIcon.isVisible():
#              self.hide()
#              event.ignore()

    def trayClick(self,reason):
        if reason==QSystemTrayIcon.DoubleClick: #双击
            self.showNormal()
        elif reason==QSystemTrayIcon.MiddleClick: #中击
            self.showMessage()
        else:
            pass


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            pass

    def closeEvent(self, event):
        if self.ckAutologout.isChecked():
            self.logout()
        self.saveState()
        event.accept()
        #event.ignore()

    def OnTimer(self):
        if self.checkLogin() == False:
            print 'Found Offline.'
            self.login()
        else:
            if self.ckKeeponline.isChecked() == False:
                self.timer.stop()
                print 'Keep on line unchecked. Timer stopped.'

    def togglePassword(self, toggle):
        if self.initializing == False and toggle == True:
            self.password = ''
            self.txtPassword.clear()
            self.saveState()

    def passwordChanged(self, str):
        self.md5ed = False

    def gs(self, string):
        string = string.strip()
        if string == 'True':
            return True
        return False

    def loadState(self):
        try:
            file = open('setting.ini', 'r')
        except:
            return
        print 'loadstate'
        lines = file.readlines(100)
        if len(lines) < 6:
            return
        self.username = lines[0].strip()
        self.password = lines[1].strip()
        if self.username != '':
            self.txtUsername.setText(self.username)
        if self.password != '':
            self.txtPassword.setText('*')
            self.md5ed = True
        self.ckAutologin.setChecked(self.gs(lines[3]))
        self.ckKeeponline.setChecked(self.gs(lines[4]))
        self.ckAutologout.setChecked(self.gs(lines[5]))
        self.ckSavepassword.setChecked(self.gs(lines[2]))
        file.close()
        self.initializing = False
        if self.ckAutologin.isChecked():
            self.login()
            self._shouldHide = True

    def saveState(self):
        self.getUsernameAndPassword()
        file = open('setting.ini', 'w')
        file.write(self.username)
        file.write('\n')
        if self.ckSavepassword.isChecked():
            file.write(self.password)
        file.write('\n')
        file.write(str(self.ckSavepassword.isChecked()))
        file.write('\n')
        file.write(str(self.ckAutologin.isChecked()))
        file.write('\n')
        file.write(str(self.ckKeeponline.isChecked()))
        file.write('\n')
        file.write(str(self.ckAutologout.isChecked()))
        file.write('\n')
        #self.login()
        file.close()

    def getUsernameAndPassword(self):
        self.username = self.txtUsername.text()
        if self.md5ed == False and self.txtPassword.text() != '':
            m = hashlib.md5(str(self.txtPassword.text()))
            self.password = m.hexdigest()
            self.txtPassword.setText('*')
            self.md5ed = True

    def login(self):
        self.getUsernameAndPassword()
        if self.password == '':
            QMessageBox.information(self, 'Error', 'Password cannot be empty!')
            return
        data = urllib.urlencode({'action':'login',
            'username': self.username,
            'password' : '{MD5_HEX}'+self.password,
            'ac_id': 1})
        u = urllib2.urlopen(LoginAddr, data).read()
        #QMessageBox.information(self, 'Info', 'Login')
        print u
        error = False
        if u == 'E2532':
            print 'Start timer.'
            self.timer.start(INTERVAL)
            self.lblState.setText('Last time login not finished. Will RETRY.')
        elif 'E2531' in u:
            QMessageBox.information(self, 'Error', 'Username incorrect!')
            error = True
        elif 'E2553:' in u:
            QMessageBox.information(self, 'Error', 'Password incorrect!')
            error = True
        else:
            if self.ckKeeponline.isChecked():
                print 'Start timer.'
                self.timer.start(INTERVAL)
            self.showState()
        if error == False:
            self.disableControl()
        self.saveState()

    def enableControl(self):
        self.btnLogin.setEnabled(True)
        self.ckSavepassword.setEnabled(True)
        self.ckAutologin.setEnabled(True)
        self.ckKeeponline.setEnabled(True)

    def disableControl(self):
        self.btnLogin.setEnabled(False)
        self.ckSavepassword.setEnabled(False)
        self.ckAutologin.setEnabled(False)
        self.ckKeeponline.setEnabled(False)

    def logout(self):
        self.timer.stop()
        while True:
            try:
                u = urllib2.urlopen(LogoutAddr).read()
                break
            except:
                time.sleep(1)
        self.showState()
        self.enableControl()
        print u

    def checkLogin(self):
        # data = urllib.urlencode({'action': 'check_online'})
        while True:
            try:
                u = urllib2.urlopen(RadInfoAddr).read()
                break
            except:
                time.sleep(1)
        if u == '':
            return False
        try:
            used = u.split(',')
            print used
            self.usedQuota = '%.2fMB' % (float(used[6])/1000/1000)
            self.downSize = '%.2fMB' % (float(used[3])/1000/1000)
            self.upSize = '%.2fMB' % (float(used[4])/1000/1000)
        except Exception,ex:
            print ex.message
            self.usedQuota = ''
        return True


    def showState(self):
        if self.checkLogin() == False:
            self.lblState.setText('Offline')
            self.lblDownUp.setText("")
        else:
            self.lblState.setText('Online, ' + self.usedQuota)
            self.lblDownUp.setText("Down: " + self.downSize + ";  Up: " + self.upSize)

    def showXX(self):
        formx = ShowStatex(self)
        formx.show()

class ShowStatex(QDialog,
        about.Ui_Dialog):
    def __init__(self, parent=None):
        super(ShowStatex, self).__init__(parent)
        self.__index = 0
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = mainUIGUI()
    form.show()
    if form.shouldHide():
        form.hide()
    app.exec_()


