![d46efa26df7f7b3588dca4430703d11](https://github.com/L-Rocket/-GUI-PyQt-/assets/93325265/c16f89e1-0b2d-4f92-b4e5-6b8935967b1d)# -GUI-PyQt-

![d46efa26df7f7b3588dca4430703d11](https://github.com/L-Rocket/-GUI-PyQt-/assets/93325265/bfe5949d-8481-4ffa-9d5b-28bfd6f73c7f)

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



