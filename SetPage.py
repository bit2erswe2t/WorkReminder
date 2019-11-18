# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetPage.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(466, 172)
        self.timeEdit = QtWidgets.QTimeEdit(Form)
        self.timeEdit.setGeometry(QtCore.QRect(80, 30, 118, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit_2 = QtWidgets.QTimeEdit(Form)
        self.timeEdit_2.setGeometry(QtCore.QRect(290, 30, 118, 22))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 32, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(240, 32, 31, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 110, 114, 32))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(240, 70, 91, 16))
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(110, 70, 81, 21))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(320, 70, 81, 21))
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Start"))
        self.label_2.setText(_translate("Form", "End"))
        self.pushButton.setText(_translate("Form", "Start"))
        self.label_3.setText(_translate("Form", "Work Time"))
        self.label_4.setText(_translate("Form", "Break Time"))

