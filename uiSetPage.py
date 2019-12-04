# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetPage.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Setting(object):
    def setupUi(self, Setting):
        Setting.setObjectName("Setting")
        Setting.resize(448, 225)
        Setting.setWindowOpacity(1.0)
        self.timeEdit = QtWidgets.QTimeEdit(Setting)
        self.timeEdit.setGeometry(QtCore.QRect(80, 30, 118, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit_2 = QtWidgets.QTimeEdit(Setting)
        self.timeEdit_2.setGeometry(QtCore.QRect(290, 30, 118, 22))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.label = QtWidgets.QLabel(Setting)
        self.label.setGeometry(QtCore.QRect(30, 32, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Setting)
        self.label_2.setGeometry(QtCore.QRect(240, 32, 31, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Setting)
        self.pushButton.setGeometry(QtCore.QRect(160, 160, 114, 32))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Setting)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 81, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Setting)
        self.label_4.setGeometry(QtCore.QRect(240, 70, 91, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Setting)
        self.lineEdit.setGeometry(QtCore.QRect(110, 70, 80, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Setting)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 70, 80, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lcd_ToStart = QtWidgets.QLCDNumber(Setting)
        self.lcd_ToStart.setGeometry(QtCore.QRect(90, 110, 101, 21))
        self.lcd_ToStart.setDigitCount(12)
        self.lcd_ToStart.setObjectName("lcd_ToStart")
        self.lcd_Work = QtWidgets.QLCDNumber(Setting)
        self.lcd_Work.setGeometry(QtCore.QRect(300, 110, 101, 21))
        self.lcd_Work.setDigitCount(12)
        self.lcd_Work.setObjectName("lcd_Work")
        self.label_5 = QtWidgets.QLabel(Setting)
        self.label_5.setGeometry(QtCore.QRect(30, 110, 51, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Setting)
        self.label_6.setGeometry(QtCore.QRect(240, 110, 81, 21))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Setting)
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        _translate = QtCore.QCoreApplication.translate
        Setting.setWindowTitle(_translate("Setting", "Setting"))
        self.label.setText(_translate("Setting", "Start"))
        self.label_2.setText(_translate("Setting", "End"))
        self.pushButton.setText(_translate("Setting", "Start"))
        self.label_3.setText(_translate("Setting", "Work Time"))
        self.label_4.setText(_translate("Setting", "Break Time"))
        self.label_5.setText(_translate("Setting", "Ready"))
        self.label_6.setText(_translate("Setting", "Work "))

