# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1710, 817)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Header = QtWidgets.QWidget(self.centralwidget)
        self.Header.setGeometry(QtCore.QRect(10, 10, 1691, 131))
        self.Header.setStyleSheet("background-color: rgb(240,248,255);\n"
"\n"
"    border: 2px solid black;\n"
"    border-radius: 10px ;")
        self.Header.setObjectName("Header")
        self.label = QtWidgets.QLabel(self.Header)
        self.label.setGeometry(QtCore.QRect(20, 10, 131, 111))
        self.label.setMinimumSize(QtCore.QSize(50, 50))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/Logo-DH-Kinh-te-Dai-hoc-Da-Nang-DUE.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.Header)
        self.pushButton_2.setGeometry(QtCore.QRect(1630, 0, 61, 28))
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/notify_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.Header)
        self.pushButton_3.setGeometry(QtCore.QRect(1570, 0, 61, 28))
        self.pushButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/profile.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.Button_Xulyrangbuoc = QtWidgets.QPushButton(self.Header)
        self.Button_Xulyrangbuoc.setGeometry(QtCore.QRect(160, 20, 261, 91))
        self.Button_Xulyrangbuoc.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(248, 248, 248);\n"
"    border: 2px solid black;\n"
"    border-radius: 10px ;")
        self.Button_Xulyrangbuoc.setObjectName("Button_Xulyrangbuoc")
        self.Button_Phancathi = QtWidgets.QPushButton(self.Header)
        self.Button_Phancathi.setGeometry(QtCore.QRect(450, 20, 251, 91))
        self.Button_Phancathi.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(248, 248, 248);\n"
"    border: 2px solid black;\n"
"    border-radius: 10px ;")
        self.Button_Phancathi.setObjectName("Button_Phancathi")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(0, 150, 1711, 661))
        self.widget_3.setStyleSheet("background-color: rgb(240,248,255);")
        self.widget_3.setObjectName("widget_3")
        self.widget = QtWidgets.QWidget(self.widget_3)
        self.widget.setGeometry(QtCore.QRect(0, 10, 1701, 641))
        self.widget.setStyleSheet("background-color: rgb(240,248,255);")
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(150, 100, 291, 301))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/images/app.png"))
        self.label_2.setObjectName("label_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(10, 0, 1691, 641))
        self.widget_2.setStyleSheet("background-color: rgb(240,248,255);\n"
"    border: 2px solid black;\n"
"    border-radius: 10px ;")
        self.widget_2.setObjectName("widget_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(520, 210, 591, 121))
        self.label_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(248, 248, 248);\n"
"    border: 2px solid black;\n"
"    border-radius: 10px ;")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_Xulyrangbuoc.setText(_translate("MainWindow", "Chuẩn bị dữ liệu"))
        self.Button_Phancathi.setText(_translate("MainWindow", "Xếp lịch thi"))
        self.label_3.setText(_translate("MainWindow", "HỆ THỐNG XẾP LỊCH THI KẾT THÚC HỌC PHẦN"))
import resources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
