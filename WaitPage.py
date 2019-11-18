# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WaitPage.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form():
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 100, 121, 31))
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(160, 160, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Have a break..."))

