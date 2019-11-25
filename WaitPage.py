import uiWaitPage
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer,QDateTime,QDate,Qt
from PyQt5.QtWidgets import QLCDNumber,QApplication

#inherit Ui_Waitting
class WaitPage(QtWidgets.QMainWindow, uiWaitPage.Ui_Waitting):
    def __init__(self, ):
        super().__init__()
        self.setupUi(self)
        self.time = QTimer(self)
        self.time.setInterval(100)
        self.time.timeout.connect(self.refresh)
        self.timerId = 0
        self.breakTime = 0
        self.startTime = 0
        self.endTime = 0
        self.setStyleSheet("QWidget{background-color:black}")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("DRINK AND BREAK")
        self.label.resize(200,100)
        self.label.move(110,80)

        self.label.setStyleSheet("QLabel{background:black;color:white;font-size:18px;font-weight:bold;}")

        self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber.setStyleSheet("border: none; color: white; background: black;")
    
    def parent(self, parent):
        self.parent = parent

    def closeEvent(self, event):
        self.time.stop()
        del self.time
        self.time = None
        self.parent.show()
    
    def startBreak(self, breakTime):
        self.setTime(breakTime)
        self.showFullScreen()
        #QTimer.singleShot(0, self.showFullScreen)
        
    def setTime(self, time):
        self.startTime = QDateTime.currentMSecsSinceEpoch()
        self.lcdDisplay(time)
        self.breakTime = time + 1000
        self.time.start()

    def lcdDisplay(self, interval):
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
        self.lcdNumber.display(intervals)

    def refresh(self):
        self.endTime = QDateTime.currentMSecsSinceEpoch()
        interval = self.endTime - self.startTime
        if interval <= self.breakTime:
            interval = self.breakTime - interval
            self.lcdDisplay(interval)
        else:
            self.time.stop()
            self.hide()
            self.parent.show() 
            if(self.parent.workCount>=0):
                print("testteat")
                if(self.parent.workCount == 0):
                    self.parent.workTime = self.parent.restTime[0]
                    self.parent.setTime(self.parent.workTime) 
                else:
                    self.parent.setTime(self.parent.workTime - 1000)
                self.parent.workCount -= 1
            if(self.parent.workCount == -1):
                self.parent.isTimeStart = False
            

        