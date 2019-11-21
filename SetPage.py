import uiSetPage
from PyQt5 import QtWidgets,QtCore,QtGui

class SetPage(QtWidgets.QMainWindow, uiSetPage.Ui_Setting):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.slot_btn_function)  
        

    def child(self, child):
        self.child = child

    def slot_btn_function(self):
        if self.lineEdit.text() != '':
            self.child.setTime(self.lineEdit.text()) 
        if self.lineEdit_2.text() != '':
            self.child.breakTime = self.lineEdit_2.text()
        self.hide()
        self.child.show()

    
        