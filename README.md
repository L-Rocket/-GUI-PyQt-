# -GUI-PyQt-
信号发生器及示波器控制GUI（PyQt）基于python

信号发生器及示波器型号：鼎阳

需提前安装INMAX，本代码仅供参考，具体参照机器说明书

pyvisa cv2

主程序所在文件Dmain.py

该程序基于python及pyqt5工具包开发

提前下载相应的包

pip install pyqt5 pyqt5-tools pyqt5designer

Qtdesigner会可以通过Listary快速找到，可以创建桌面快捷方式方便使用


将ui文件转为py文件：

cmd指令

pyuic5 -x a.ui -o a.py          # 将a.ui文件转为a.py文件，没有就自动生成，如果有，就覆盖。


