from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import SetPage
import WaitPage

class SetPage(QtWidgets.QMainWindow, SetPage.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.slot_btn_function)  

    def child(self, child):
        self.child = child

    def slot_btn_function(self):
        self.hide()
        self.child.show()


#inherit Ui_Form
class WaitPage(QtWidgets.QMainWindow, WaitPage.Ui_Form):
    def __init__(self, ):
        super().__init__()
        self.setupUi(self)
        
    def parent(self, parent):
        self.parent = parent

    def closeEvent(self, event):
        self.parent.show()

def main():
    app = QApplication([])
    setPage = SetPage()
    waitPage = WaitPage()
    setPage.child(waitPage)
    waitPage.parent(setPage)
    setPage.show()
    app.exec_()

if __name__ == '__main__':
    main()
