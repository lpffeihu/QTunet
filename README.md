# QTunet
**这里是源码，如果想要Windows可执行文件
，[请点我下载](https://github.com/lpffeihu/QTunet/releases/download/v0.03/QTunet.zip)。**

QTunet是一个带有保持在线功能的Tunet客户端

使用Python 2.7和pyQt4开发，遵循GPLv3。

注意界面上显示的“Online, XXXMB”中的流量是**登录时的流量**，不会实时更新。下面两个Up和Down是本次登录后使用的流量，会经常更新。

## 风险

本软件存在以下风险，请在仔细阅读后再考虑是否使用。

* 流量超额风险：本软件并不检查当前使用流量，花钱概不负责。

* 保持在线功能乱用风险：即使用Usereg也没法下线保持在线的IP。
如果你在三个地方保持在线，第四个地方再怎么想用也没法登录了。
如果遇到这类问题，解决方案是改Info密码。

* Tunet系统BUG风险：曾经有这样的情况发生。TUNET故障，上线1分钟以内必然强制断开。
这时某同学已经超过20G，TUNET规定每次登陆至少收费0.01元。结果白亏了他不少钱。

* 密码遗失风险：如果你选择了保存密码，密码的MD5值会保存在当前目录的setting.ini中。
虽然是MD5加密，但因为学校的info登陆貌似是只要有MD5就能登的（当然需要一些技术手段），
所以对于高手来讲，拿到你密码的MD5跟拿到你密码一样的。所以是否保存密码请考虑好。

* 通信被监听风险：2015年Tunet系统的重要更新是用了HTTPS。但是，本软件使用的是HTTP。
因此，有被监听的风险。

## 使用

### For Windows

Release中包含了Windows版本的可执行文件，请[移步](https://github.com/lpffeihu/QTunet/releases/)或[直接下载](https://github.com/lpffeihu/QTunet/releases/download/v0.03/QTunet.zip)。

### For MAC

不是特别推荐给不写代码的MAC用户使用。如果你不纠结于图形界面，请使用Bash版本的QTunet。

如果你一定要用，你需要安装pyQt。但这个貌似挺容易把系统搞乱的，这就是不推荐使用的原因。具体如何安装pyQt请Google。

我用的是Homebrew安装。首先你得装了Homebrew。然后，

```bash
brew install pyqt
```

以上命令可能会新装一个不同版本的python，而且装完了之后可能会覆盖系统默认的python，而且装完了可能要调整路径才能用。所以不推荐不爱折腾的人用嘛。

另外，在我这里点右上角的X会直接退出（最小化可以点菜单栏图标，然后选最小化）；打开后不能从Dock上去掉；Dock里图标有点丑等等。暂时没有动机改。

### For Linux

没试过。

我直接用Bash版本。

## Windows下的编译

1. 安装pyQt4和py2exe
2. 修改setup.py中的D:\Anaconda\为你的python安装路径
3. 在QTunet目录下运行
```bash
python setup.py py2exe
```

## Known Issues

* 由于用的是单线程，没网的时候或者网断的时候程序会死掉

## 关于作者

Author: feihu @ [Gu-Lab](http://gu.ee.tsinghua.edu.cn/)

Author Email: lpfffeihu (a.t.) gmail.com

作者将于2016年1月毕业，如果你愿意继续维护这个项目，请邮件联系。
