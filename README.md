# -GUI-PyQt-
信号发生器及示波器控制GUI（PyQt）基于python

信号发生器及示波器型号：鼎阳

需提前安装INMAX，本代码仅供参考，具体参照机器说明书

包：pyvisa, cv2

主程序所在文件Dmain.py

该程序基于python及pyqt5工具包开发

pip install pyqt5 pyqt5-tools pyqt5designer

将设计文件转为py文件：

pyuic5 -x a.ui -o a.py          # 将a.ui文件转为a.py文件，没有就自动生成，如果有，就覆盖。


​pyinstaller -F main.py #打包成 exe

pyinstaller -F --icon=my.ico test.py #打包成 exe，并设置图标

pyinstaller -F -w yourfilename.py #打包成 exe, 且不包含控制台



