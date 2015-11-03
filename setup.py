from distutils.core import setup
import py2exe
#setup(windows = [{"script":"SSMautoharvest.py", "icon_resources": [(1, "myico.ico")]} ])
script_path = "QTunet.pyw"
icon_path = "icon.ico"
setup(windows=[{"script":script_path,
                "icon_resources":[(1, icon_path)]}], 
      data_files = [
            ('imageformats', [
              r'D:\Anaconda\Lib\site-packages\PyQt4\plugins\imageformats\qico4.dll'
              ])],
      options={"py2exe":{"packages":["gzip"], 
                         "includes":["sip"]}})
