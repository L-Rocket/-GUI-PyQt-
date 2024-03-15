# -GUI-PyQt-示波器-信号发生器控制台

通过网口通信，该上位机能控制鼎阳的信号发生器和示波器。

另外，可以通过改变信号的频率，实时读取电路的相应，可以很便捷的测出电路的**频响特性**，从而得到其**波特图**，实现了扫频仪的功能，这也是设计该程序的初衷。

# GUI界面
### 主界面
![d46efa26df7f7b3588dca4430703d11](https://github.com/L-Rocket/-GUI-PyQt-/assets/93325265/bfe5949d-8481-4ffa-9d5b-28bfd6f73c7f)
### 扫频得到带通滤波器的波特图
![1e79dbcbb4a8d56fffcf088caa155fd](https://github.com/L-Rocket/-GUI-PyQt-/assets/93325265/fe62c70e-0920-4c44-b243-145c3ce8a9b5)

# 基本介绍



信号发生器及示波器控制GUI（PyQt）

该程序基于python及pyqt5工具包开发

信号发生器及示波器型号：鼎阳

需提前安装INMAX，本代码仅供参考，具体参照机器说明书

依赖：pyvisa, cv2

执行Dmain.py即可启动程序


# 相关shell命令


### 安装相关依赖：
```shell
pip install pyqt5 pyqt5-tools pyqt5designer pyvisa cv2
```


### 将a.ui文件转为a.py文件，没有就自动生成，如果有，就覆盖。：
```shell
pyuic5 -x a.ui -o a.py          
```


### 打包成 exe：
```shell
​pyinstaller -F main.py    
```

### 打包成 exe，并设置图标：
```shell
pyinstaller -F --icon=my.ico test.py   
```

### 打包成 exe, 且不包含控制台
```shell
pyinstaller -F -w yourfilename.py 
```






