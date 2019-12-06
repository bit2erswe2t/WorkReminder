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
        self.timeEditStart = QtWidgets.QTimeEdit(Setting)
        self.timeEditStart.setGeometry(QtCore.QRect(80, 30, 118, 22))
        self.timeEditStart.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 1)))
        self.timeEditStart.setTime(QtCore.QTime(0, 0, 1))
        self.timeEditStart.setObjectName("timeEditStart")
        self.timeEditEnd = QtWidgets.QTimeEdit(Setting)
        self.timeEditEnd.setGeometry(QtCore.QRect(290, 30, 118, 22))
        self.timeEditEnd.setObjectName("timeEditEnd")
        self.labelStart = QtWidgets.QLabel(Setting)
        self.labelStart.setGeometry(QtCore.QRect(30, 32, 31, 16))
        self.labelStart.setObjectName("labelStart")
        self.labelEnd = QtWidgets.QLabel(Setting)
        self.labelEnd.setGeometry(QtCore.QRect(240, 32, 31, 16))
        self.labelEnd.setObjectName("labelEnd")
        self.btnStart = QtWidgets.QPushButton(Setting)
        self.btnStart.setGeometry(QtCore.QRect(74, 160, 112, 32))
        self.btnStart.setObjectName("btnStart")
        self.labelWorktime = QtWidgets.QLabel(Setting)
        self.labelWorktime.setGeometry(QtCore.QRect(30, 70, 81, 21))
        self.labelWorktime.setObjectName("labelWorktime")
        self.labelBreaktime = QtWidgets.QLabel(Setting)
        self.labelBreaktime.setGeometry(QtCore.QRect(240, 70, 91, 21))
        self.labelBreaktime.setObjectName("labelBreaktime")
        self.lineEditWorktime = QtWidgets.QLineEdit(Setting)
        self.lineEditWorktime.setGeometry(QtCore.QRect(110, 70, 80, 21))
        self.lineEditWorktime.setObjectName("lineEditWorktime")
        self.lineEditBreaktime = QtWidgets.QLineEdit(Setting)
        self.lineEditBreaktime.setGeometry(QtCore.QRect(320, 70, 80, 21))
        self.lineEditBreaktime.setObjectName("lineEditBreaktime")
        self.lcdReady = QtWidgets.QLCDNumber(Setting)
        self.lcdReady.setGeometry(QtCore.QRect(90, 110, 101, 21))
        self.lcdReady.setDigitCount(12)
        self.lcdReady.setObjectName("lcdToStart")
        self.lcdWork = QtWidgets.QLCDNumber(Setting)
        self.lcdWork.setGeometry(QtCore.QRect(300, 110, 101, 21))
        self.lcdWork.setDigitCount(12)
        self.lcdWork.setObjectName("lcdWork")
        self.labelReady = QtWidgets.QLabel(Setting)
        self.labelReady.setGeometry(QtCore.QRect(30, 110, 51, 21))
        self.labelReady.setObjectName("labelReady")
        self.labelWork = QtWidgets.QLabel(Setting)
        self.labelWork.setGeometry(QtCore.QRect(240, 110, 81, 21))
        self.labelWork.setObjectName("labelWork")
        self.btnOver = QtWidgets.QPushButton(Setting)
        self.btnOver.setGeometry(QtCore.QRect(262, 160, 112, 32))
        self.btnOver.setObjectName("btnOver")

        self.retranslateUi(Setting)
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        _translate = QtCore.QCoreApplication.translate
        Setting.setWindowTitle(_translate("Setting", "Setting"))
        self.labelStart.setText(_translate("Setting", "Start"))
        self.labelEnd.setText(_translate("Setting", "End"))
        self.btnStart.setText(_translate("Setting", "Start"))
        self.labelWorktime.setText(_translate("Setting", "Work Time"))
        self.labelBreaktime.setText(_translate("Setting", "Break Time"))
        self.labelReady.setText(_translate("Setting", "Ready"))
        self.labelWork.setText(_translate("Setting", "Work "))
        self.btnOver.setText(_translate("Setting", "Over"))

