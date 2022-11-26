import binascii
from msilib.schema import SelfReg
import time

import pyvisa as visa
import cv2
import matplotlib.pyplot as plt
from childwindow import *
from depart import *
from PyQt5 import QtCore, QtGui, QtWidgets
from shiboqi import Ui_shibo
rm = visa.ResourceManager()
print(rm)
print("我的")
instr = rm.list_resources()
print(instr)
scope1 = rm.open_resource(instr[0])
scope2 = rm.open_resource(instr[1])
scope2.chunk_size = 20 * 1024 * 1024  # default value is 20*1024(20k bytes)
scope2.timeout = 30000  # default value is 2000(2s)
print(scope2)
print(scope2.query('*IDN?'))
i = 0
j = 1
scope2.write("chdr off")
scope2.write("chdr off")
# vdiv = scope2.query("c1:vdiv?")
# ofst = scope2.query("c1:ofst?")
# tdiv = scope2.query("tdiv?")
# sara = scope2.query("sara?")
# sara_unit = {'G':1E9,'M':1E6,'k':1E3}

# for unit in sara_unit.keys():

#     if sara.find(unit)!=-1:
#         sara = sara.split(unit)
#         sara = float(sara[0])*sara_unit[unit]
#         break
# sara = float(sara)

listA=[1000,10000,1000]

class ChlidWindow1(QtWidgets.QMainWindow,Ui_ChildWindow):
    def __init__(self):  # 初始化UI代码
        super(ChlidWindow1,self).__init__()
        self.setupUi(self)
        
        self.lineEdit.setText("1000")
        self.lineEdit_2.setText("1000")
        self.lineEdit_3.setText("10000")    
        self.p1.clicked.connect(self.get1)

    def get1(self):
        listA[0]=int(self.lineEdit.text())
        listA[1]=int(self.lineEdit_2.text())
        listA[2]=int(self.lineEdit_3.text())
        
            

# class ChlidWindow2(QtWidgets.QMainWindow, Ui_shibo):

#     def __init__(self):  # 初始化UI代码
#         super(ChlidWindow2,self).__init__()
#         self.setupUi(self) 

            
        


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):  # 初始化UI代码
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # 以下为逻辑代码 #ch1
        self.lineEdit_1.setText("1000")
        self.lineEdit_1.editingFinished.connect(self.SwicthF1)
        self.lineEdit_2.setText("4.0")
        self.lineEdit_2.editingFinished.connect(self.SwitchV1)
        self.lineEdit_3.setText("0.0")
        self.lineEdit_3.editingFinished.connect(self.SwicthP1)
        self.radioButton.toggled.connect(self.Run1)
        self.radioButton_2.toggled.connect(self.Stop1)
        self.comboBox_1.currentIndexChanged.connect(self.Switch1)
        self.comboBox_2.currentIndexChanged.connect(self.Swich2)
        self.radioButton_5.clicked.connect(self.ON)
        self.radioButton_6.clicked.connect(self.Stop1)
        # self.pushButton.clicked.connect(self.open)

        # 以下为CH2的代码：
        self.lineEdit_4.setText("1000")
        self.lineEdit_4.editingFinished.connect(self.SwithF2)

        self.lineEdit_5.setText("4.0")
        self.lineEdit_5.editingFinished.connect(self.SwithV2)

        self.lineEdit_6.setText("0.0")
        self.lineEdit_6.editingFinished.connect(self.SwithP2)
        self.radioButton_3.toggled.connect(self.Run2)
        self.radioButton_4.toggled.connect(self.Stop2)
        self.comboBox_1.currentIndexChanged.connect(self.Switch1)
        self.comboBox_2.currentIndexChanged.connect(self.Swich2)

        # 所调用方法：

    # 1公用函数
    
    # CH1函数：
    def ON(self): #childwindows ON
        scope1.write("C1:BSWV WVTP,SINE")
        n = float(self.lineEdit_2.text())
        scope1.write("C1:BSWV AMP,%f"%n )
        self.Run1()
        x=[]
        y=[]
        file_name = "F:\\temp.txt"
        f = open(file_name,"w+")
        for i in range(listA[0],listA[2]+listA[1],listA[1]):
            scope1.write("C1:BSWV FRQ,%f"%i)
            time.sleep(0.1) 
            # self.lineEdit_1.setText(str(i))
            # time.sleep(0.1)
            scope2.write("PACU PKPK,C1")
            AMP=str(scope2.query("C1:PAVA? AMPL"))
            AMP=AMP.split(",")
            f.write(str(i)+" "+AMP[1])
            x.append(i)
            y.append(float(AMP[1]))       
        f.close()
        print(x)
        print(y)
        plt.plot(x,y)
        plt.show()
        
                       
    def FindVpp(self,volt_value):
        for i in range(0,len(volt_value),10):
            flag1=0
            flag2=0
            if volt_value[i]<volt_value[i+10]:
                flag1=1
            if volt_value[i]>volt_value[i+10]:
                pass
  
    def B10(self):
        self.label_18.setPixmap(QtGui.QPixmap("F:\\SCDP1.jpg")) 
        
    def Run1(self):  # radiobutton
        scope1.write("C1:OUTP ON")
        scope2.write("PACU PKPK,C1")
        scope2.write("PASTAT ON")
        
        print(1)
        
    def Stop1(self):  # radiobutton
        scope1.write("C1:OUTP OFF")

    def SwicthF1(self):
        n = int(self.lineEdit_1.text())
        scope1.write("C1:BSWV FRQ,%d" % n)

    def SwitchV1(self):
        n = float(self.lineEdit_2.text())
        scope1.write("C1:BSWV AMP,%f" % n)

    def SwicthP1(self):
        n = float(self.lineEdit_3.text())
        scope1.write("C1:BSWV PHSE,%f" % n)

    def Switch1(self):  # comboBox
        s = self.comboBox_1.currentText()
        if s == "Sine":
            print("正弦波")
            scope1.write("C1:BSWV WVTP,SINE")
            self.lineEdit_1.setText("1000")
            self.lineEdit_2.setText("4.0")
            self.lineEdit_3.setText("0.0")
        if s == "Square":
            print("方波")
            scope1.write("C1:BSWV WVTP,SQUARE")
        if s == "Ramp":
            print("Ramp")
            scope1.write("C1:BSWV WVTP,RAMP")
        if s == "Pulse":
            print("Pulse")
            scope1.write("C1:BSWV WVTP,PULSE")
        if s == "Noise":
            print("Noise")
            scope1.write("C1:BSWV WVTP,NOISE")
        if s == "DC":
            print("DC")
            scope1.write("C1:BSWV WVTP,DC")
            self.lineEdit_1.setText("0.0")
            self.lineEdit_2.setText("0.0")
            self.lineEdit_3.setText("0.0")

    def OffSweep(self):
        print(0)
        scope1.write("C1:OUTP OFF")

    # ch2函数

    def Run2(self):  # radiobutton
        scope1.write("C2:OUTP ON")

    def Stop2(self):  # radiobutton
        scope1.write("C2:OUTP OFF")

    def SwithF2(self):
        n = int(self.lineEdit_4.text())
        scope1.write("C2:BSWV FRQ,%d" % n)

    def SwithV2(self):
        n = float(self.lineEdit_5.text())
        scope1.write("C2:BSWV AMP,%f" % n)

    def SwithP2(self):
        n = float(self.lineEdit_6.text())
        scope1.write("C2:BSWV PHSE,%f" % n)

    def Swich2(self):  # comboBox
        s = self.comboBox_2.currentText()
        if s == "Sine":
            print("正弦波")
            scope1.write("C2:BSWV WVTP,SINE")
            self.lineEdit_1.setText("1000")
            self.lineEdit_2.setText("4.0")
            self.lineEdit_3.setText("0.0")
        if s == "Square":
            print("方波")
            scope1.write("C2:BSWV WVTP,SQUARE")
        if s == "Ramp":
            print("Ramp")
            scope1.write("C2:BSWV WVTP,RAMP")
        if s == "Pulse":
            print("Pulse")
            scope1.write("C2:BSWV WVTP,PULSE")
        if s == "Noise":
            print("Noise")
            scope1.write("C2:BSWV WVTP,NOISE")
        if s == "DC":
            print("DC")
            scope1.write("C2:BSWV WVTP,DC")
            self.lineEdit_1.setText("0.0")
            self.lineEdit_2.setText("0.0")
            self.lineEdit_3.setText("0.0")

        # if __name__ == "__main__":
        
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    childWindow1 = ChlidWindow1()
    # childWindow2 = ChlidWindow2()
    mainWindow.pushButton.clicked.connect(childWindow1.show)
    childWindow1.p1.clicked.connect(childWindow1.close)
    childWindow1.p2.clicked.connect(childWindow1.close)
    # mainWindow.B2.clicked.connect(childWindow2.show)
    mainWindow.show()
    sys.exit(app.exec_())
    
