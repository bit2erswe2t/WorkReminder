import uiWaitPage
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer,QDateTime,Qt
from PyQt5.QtWidgets import QLCDNumber,QApplication
from PyQt5.QtGui import QIcon

#inherit Ui_Waitting
class WaitPage(QtWidgets.QMainWindow, uiWaitPage.Ui_Waitting):
    def __init__(self, imgName):
        super().__init__()
        self.setupUi(self)
        self.init(self, imgName)
    
    def init(self, imgName):
        self.setWindowIcon(QIcon(imgName))
        self.setStyleSheet("QWidget{background-color:black}")
        self.labelTip.setAlignment(Qt.AlignCenter)
        self.labelTip.setText("DRINK AND BREAK")
        self.labelTip.resize(200,100)
        self.labelTip.move(110,80)
        self.labelTip.setStyleSheet("QLabel{background:black;color:white;font-size:18px;font-weight:bold;}")
        self.lcdCountDown.setSegmentStyle(QLCDNumber.Flat)
        self.lcdCountDown.setStyleSheet("border: none; color: white; background: black;")

        self.breakTimer = QTimer(self)
        self.breakTimer.setInterval(100)
        self.breakTimer.timeout.connect(self.breakTimerSlot)
        
        self.breakInterval = 0
        self.breakStartMoment = 0
        self.breakEndMoment = 0
        
    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def closeEvent(self, event):
        self.breakTimer.stop()
        del self.breakTimer
        self.breakTimer = None
        self.parent.show()
    
    def startBreak(self, time):
        self.breakStartMoment = QDateTime.currentMSecsSinceEpoch()
        self.displayLCD(time)
        self.breakInterval = time + 1000
        self.breakTimer.start()
        self.showFullScreen()

    def displayLCD(self, interval):
        hour = interval // (60 * 60 * 1000)
        minu = (interval - hour * 60 * 60 * 1000) // (60 * 1000)
        sec = (interval - hour * 60 * 60 * 1000 - minu * 60 * 1000) // 1000
        if hour<10:
            hour = '0' + str(hour)
        if minu<10:
            minu = '0' + str(minu)
        if sec<10:
            sec = '0' + str(sec)
        intervals = str(hour) + ':' + str(minu) + ':' + str(sec)
        self.lcdCountDown.display(intervals)

    def breakTimerSlot(self):
        interval = QDateTime.currentMSecsSinceEpoch() - self.breakStartMoment
        remainder = self.breakInterval - interval
        if 0 <= remainder:
            self.displayLCD(remainder)
        else:
            self.breakTimer.stop()
            self.parent.show() 
            self.hide()
            if(self.parent.cyclesNum>1):
                self.parent.startWorkTimer(self.parent.workInterval - 1000)
            elif(self.parent.cyclesNum == 1):
                self.parent.startWorkTimer(self.parent.remainderTime[0])
            else:
                self.parent.isOnBtnStart = False
            self.parent.cyclesNum -= 1
            

        