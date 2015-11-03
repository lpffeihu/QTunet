# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(311, 231)
        self.gridLayoutWidget = QtGui.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 291, 211))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.txtUsername = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txtUsername.setEnabled(True)
        self.txtUsername.setFrame(True)
        self.txtUsername.setObjectName(_fromUtf8("txtUsername"))
        self.gridLayout.addWidget(self.txtUsername, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lblState = QtGui.QLabel(self.gridLayoutWidget)
        self.lblState.setText(_fromUtf8(""))
        self.lblState.setObjectName(_fromUtf8("lblState"))
        self.gridLayout.addWidget(self.lblState, 6, 1, 1, 1)
        self.ckAutologout = QtGui.QCheckBox(self.gridLayoutWidget)
        self.ckAutologout.setObjectName(_fromUtf8("ckAutologout"))
        self.gridLayout.addWidget(self.ckAutologout, 5, 1, 1, 1)
        self.ckKeeponline = QtGui.QCheckBox(self.gridLayoutWidget)
        self.ckKeeponline.setObjectName(_fromUtf8("ckKeeponline"))
        self.gridLayout.addWidget(self.ckKeeponline, 4, 1, 1, 1)
        self.ckAutologin = QtGui.QCheckBox(self.gridLayoutWidget)
        self.ckAutologin.setObjectName(_fromUtf8("ckAutologin"))
        self.gridLayout.addWidget(self.ckAutologin, 3, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnLogin = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnLogin.setMinimumSize(QtCore.QSize(0, 20))
        self.btnLogin.setObjectName(_fromUtf8("btnLogin"))
        self.horizontalLayout.addWidget(self.btnLogin)
        self.btnLogout = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnLogout.setMinimumSize(QtCore.QSize(0, 20))
        self.btnLogout.setObjectName(_fromUtf8("btnLogout"))
        self.horizontalLayout.addWidget(self.btnLogout)
        self.gridLayout.addLayout(self.horizontalLayout, 8, 1, 1, 1)
        self.txtPassword = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txtPassword.setEnabled(True)
        self.txtPassword.setFrame(True)
        self.txtPassword.setObjectName(_fromUtf8("txtPassword"))
        self.gridLayout.addWidget(self.txtPassword, 1, 1, 1, 1)
        self.ckSavepassword = QtGui.QCheckBox(self.gridLayoutWidget)
        self.ckSavepassword.setObjectName(_fromUtf8("ckSavepassword"))
        self.gridLayout.addWidget(self.ckSavepassword, 2, 1, 1, 1)
        self.lblDownUp = QtGui.QLabel(self.gridLayoutWidget)
        self.lblDownUp.setText(_fromUtf8(""))
        self.lblDownUp.setObjectName(_fromUtf8("lblDownUp"))
        self.gridLayout.addWidget(self.lblDownUp, 7, 1, 1, 1)
        self.btnAbout = QtGui.QToolButton(self.gridLayoutWidget)
        self.btnAbout.setObjectName(_fromUtf8("btnAbout"))
        self.gridLayout.addWidget(self.btnAbout, 8, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.txtUsername, self.txtPassword)
        Dialog.setTabOrder(self.txtPassword, self.ckSavepassword)
        Dialog.setTabOrder(self.ckSavepassword, self.ckAutologin)
        Dialog.setTabOrder(self.ckAutologin, self.ckKeeponline)
        Dialog.setTabOrder(self.ckKeeponline, self.ckAutologout)
        Dialog.setTabOrder(self.ckAutologout, self.btnLogin)
        Dialog.setTabOrder(self.btnLogin, self.btnLogout)
        Dialog.setTabOrder(self.btnLogout, self.btnAbout)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "QTunet", None))
        self.label.setText(_translate("Dialog", "用户名", None))
        self.label_2.setText(_translate("Dialog", "密码", None))
        self.ckAutologout.setText(_translate("Dialog", "退出时自动断线", None))
        self.ckKeeponline.setText(_translate("Dialog", "保持在线", None))
        self.ckAutologin.setText(_translate("Dialog", "自动登录", None))
        self.btnLogin.setText(_translate("Dialog", "登录", None))
        self.btnLogout.setText(_translate("Dialog", "断开", None))
        self.ckSavepassword.setText(_translate("Dialog", "保存密码", None))
        self.btnAbout.setText(_translate("Dialog", "i", None))

