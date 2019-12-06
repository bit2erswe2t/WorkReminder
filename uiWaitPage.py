# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WaitPage.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Waitting(object):
    def setupUi(self, Waitting):
        Waitting.setObjectName("Waitting")
        Waitting.resize(400, 300)
        Waitting.setWindowOpacity(1.0)
        self.labelTipTip = QtWidgets.QLabel(Waitting)
        self.labelTipTip.setGeometry(QtCore.QRect(140, 100, 121, 31))
        self.labelTipTip.setObjectName("labelTip")
        self.lcdCountDown = QtWidgets.QLCDNumber(Waitting)
        self.lcdCountDown.setGeometry(QtCore.QRect(120, 160, 141, 21))
        self.lcdCountDown.setDigitCount(12)
        self.lcdCountDown.setObjectName("lcdCountDown")

        self.retranslateUi(Waitting)
        QtCore.QMetaObject.connectSlotsByName(Waitting)

    def retranslateUi(self, Waitting):
        _translate = QtCore.QCoreApplication.translate
        WaittlabelTipetWindowTitle(_translate("Waitting", "Waitting"))
        self.labelTip.setText(_translate("Waitting", "Have a break..."))

