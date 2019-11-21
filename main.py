from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from SetPage import SetPage
from WaitPage import WaitPage

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
