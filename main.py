from PyQt5.QtWidgets import QApplication
from SetPage import SetPage
from WaitPage import WaitPage
import base64,os
from coffeeico import img

def main():
    imgName = 'coffeeTemp.ico'
    tmp = open(imgName, 'wb')
    tmp.write(base64.b64decode(img))
    tmp.close()
    app = QApplication([])
    setPage = SetPage(imgName)
    waitPage = WaitPage(imgName)
    setPage.child(waitPage)
    waitPage.parent(setPage)
    setPage.show()
    app.exec_()
    os.remove('coffeeTemp.ico')

if __name__ == '__main__':
    main()

