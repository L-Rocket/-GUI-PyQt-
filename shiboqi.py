# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shiboqi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_shibo(object):
    def setupUi(self, shibo):
        shibo.setObjectName("shibo")
        shibo.resize(805, 678)
        self.centralwidget = QtWidgets.QWidget(shibo)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 801, 641))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(22)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(10, 20, 771, 521))
        self.label_19.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_19.setText("")
        self.label_19.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_19.setPixmap(QtGui.QPixmap("F:/SCDP1.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setWordWrap(False)
        self.label_19.setOpenExternalLinks(True)
        self.label_19.setObjectName("label_19")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 550, 221, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        shibo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(shibo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 23))
        self.menubar.setObjectName("menubar")
        shibo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(shibo)
        self.statusbar.setObjectName("statusbar")
        shibo.setStatusBar(self.statusbar)

        self.retranslateUi(shibo)
        QtCore.QMetaObject.connectSlotsByName(shibo)

    def retranslateUi(self, shibo):
        _translate = QtCore.QCoreApplication.translate
        shibo.setWindowTitle(_translate("shibo", "示波器"))
        self.pushButton_3.setText(_translate("shibo", "start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    shibo = QtWidgets.QMainWindow()
    ui = Ui_shibo()
    ui.setupUi(shibo)
    shibo.show()
    sys.exit(app.exec_())
