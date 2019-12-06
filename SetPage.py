import uiSetPage
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer,QDateTime,QTime
from PyQt5.QtWidgets import QLCDNumber
from PyQt5.QtGui import QIcon

class SetPage(QtWidgets.QMainWindow, uiSetPage.Ui_Setting):
    def __init__(self, imgName):
        super().__init__()
        self.setupUi(self)
        self.init(imgName)
        
    def init(self,imgName):
        self.setWindowIcon(QIcon(imgName))
        self.btnStart.clicked.connect(self.btnStartSlot)  
        self.lineEditWorktime.setText('2:00')
        self.lineEditBreaktime.setText('1:00')
        self.timeEditStart.setTime(QTime(15,22))
        self.timeEditEnd.setTime(QTime(15,25))
        self.lcdWork.setSegmentStyle(QLCDNumber.Flat)
        self.lcdWork.setStyleSheet("border: none; color: black;")
        self.lcdWork.display("00:00:00")
        self.lcdReady.setSegmentStyle(QLCDNumber.Flat)
        self.lcdReady.setStyleSheet("border: none; color: black;")
        self.lcdReady.display("00:00:00")

        self.workTimer = QTimer(self)
        self.workTimer.setInterval(100)
        self.workTimer.timeout.connect(self.workTimerSlot)

        self.waitTimer = QTimer(self)
        self.waitTimer.setInterval(100)
        self.waitTimer.timeout.connect(self.waitTimerSlot)

        self.isOnBtnStart = False
        self.cyclesNum = 0
        self.remainderTime = [0,0]

        self.workInterval = 0
        self.breakInterval = 0
        self.readyInterval = 0

        self.workStartMoment = 0
        self.cyclesStartMoment = None
        self.cyclesEndMoment = None

    def setChild(self, child):
        self.child = child
    
    def getChild(self):
        return self.child

    def hms2Msec(self, time):
        msecs = 0
        if '：' in time:
            timeArr = [int(x) for x in time.split('：')]
        else:
            timeArr = [int(x) for x in time.split(':')]
        arrLen = len(timeArr)
        if arrLen == 3:
            msecs = 1000*(timeArr[0]*60*60 + timeArr[1]*60 + timeArr[2])
        if arrLen == 2:
            msecs = 1000*(timeArr[0]*60 + timeArr[1])
        if arrLen == 1:
            msecs = timeArr[0] * 1000
        return msecs

    def getInput(self):
        self.workInterval = self.hms2Msec(self.lineEditWorktime.text())
        self.breakInterval = self.hms2Msec(self.lineEditBreaktime.text())
        self.cyclesStartMoment = self.timeEditStart.time()
        self.cyclesEndMoment = self.timeEditEnd.time()
    
    def checkInput(self):
        return self.timeEditStart.text() != '0:00' \
            and self.timeEditEnd.text() != '0:00' \
            and self.lineEditWorktime.text() != ''\
            and self.lineEditBreaktime.text() != ''

    def displayLCD(self, interval, lcdChoice):
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
        if(lcdChoice==1):
            self.lcdReady.display(intervals)
        else:
            self.lcdWork.display(intervals)
    
    def btnStartSlot(self):
        if self.checkInput() and not self.isOnBtnStart:
            self.isOnBtnStart = True 
            self.getInput()
            self.readyInterval = QTime.currentTime().msecsTo(self.cyclesStartMoment)
            if(self.readyInterval >= 0):
                self.waitTimer.start()
            else:
                self.startWork()
        else:
            pass
        
    def waitTimerSlot(self):
        self.readyInterval = QTime.currentTime().msecsTo(self.cyclesStartMoment)
        if self.readyInterval <= 0:
            self.waitTimer.stop()
            self.startWork()
        else:
            self.displayLCD(self.readyInterval, 1)

    def workTimerSlot(self):
        interval = QDateTime.currentMSecsSinceEpoch() - self.workStartMoment
        remainder = self.workInterval - interval
        if 0 <= remainder:
            self.displayLCD(remainder, 2)
        else:
            self.workTimer.stop()
            self.hide()
            if(self.cyclesNum == 0):
                self.child.startBreak(self.remainderTime[1])
            else:
                self.child.startBreak(self.breakInterval)

    def startWork(self):
        diff = abs(self.cyclesEndMoment.msecsTo(QTime.currentTime()))
        mod = diff % (self.workInterval + self.breakInterval)
        self.cyclesNum = diff//(self.workInterval + self.breakInterval)
        if(mod != 0):
            self.remainderTime[0] = int((mod * (self.workInterval/(self.workInterval + self.breakInterval)))/1000)*1000
            self.remainderTime[1] = int((mod - self.remainderTime[0])/1000)*1000
        else:
            self.remainderTime[0] = 0
            self.remainderTime[1] = 0
        if(self.cyclesNum == 0):
            self.workInterval, self.breakInterval = self.remainderTime
        #Start workTimer
        self.startWorkTimer()
    
    def startWorkTimer(self, time):
        self.workStartMoment = QDateTime.currentMSecsSinceEpoch()
        self.displayLCD(time, 2)
        self.workInterval = time + 1000 #Guarantee count down from your set time
        self.workTimer.start()
    
        