from PyQt5.QtWidgets import QApplication
from SetPage import SetPage
from WaitPage import WaitPage
import base64,os
from coffeeico import img

def main():
    imgName = 'coffeeTemp.ico'
    imgTemp = open(imgName, 'wb')
    imgTemp.write(base64.b64decode(img))
    imgTemp.close()
    app = QApplication([])
    setPage = SetPage(imgName)
    waitPage = WaitPage(imgName)
    setPage.setChild(waitPage)
    waitPage.setParent(setPage)
    setPage.show()
    app.exec_()
    os.remove('coffeeTemp.ico')

if __name__ == '__main__':
    main()

