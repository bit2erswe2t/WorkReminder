import uiSetPage
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer,QDateTime,QTime
from PyQt5.QtWidgets import QLCDNumber
from PyQt5.QtGui import QIcon

class SetPage(QtWidgets.QMainWindow, uiSetPage.Ui_Setting):
    def __init__(self, imgName):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(imgName))
        self.pushButton.clicked.connect(self.startBtnSlot)  
        self.lineEdit.setText('2:00')
        self.lineEdit_2.setText('1:00')
        self.timeEdit.setTime(QTime(15,22))
        self.timeEdit_2.setTime(QTime(15,25))
        self.time = QTimer(self)
        self.time.setInterval(100)
        self.time.timeout.connect(self.startWork)
        self.waitStartTime = QTimer(self)
        self.waitStartTime.setInterval(100)
        self.waitStartTime.timeout.connect(self.waitStartTimeSlot)
        self.workTime = 0
        self.breakTime = 0
        self.startTime = 0
        self.endTime = 0
        self.isTimeStart = False
        self.workStartTime = None
        self.workEndTime = None
        self.toStart = 0
        self.workCount = 0
        self.restTime = [0,0]
        self.lcd_Work.setSegmentStyle(QLCDNumber.Flat)
        self.lcd_ToStart.setSegmentStyle(QLCDNumber.Flat)
        self.lcd_Work.setStyleSheet("border: none; color: black;")
        self.lcd_ToStart.setStyleSheet("border: none; color: black;")
        self.lcd_Work.display("00:00:00")
        self.lcd_ToStart.display("00:00:00")
        
    def child(self, child):
        self.child = child
    
    def inputTimePross(self, time):
        msecs = 0
        if '：' in time:
            timeSplit = [int(x) for x in time.split('：')]
        else:
            timeSplit = [int(x) for x in time.split(':')]
        splitLen = len(timeSplit)
        if splitLen == 3:
            msecs = 1000*(timeSplit[0]*60*60 + timeSplit[1]*60 + timeSplit[2])
        if splitLen == 2:
            msecs = 1000*(timeSplit[0]*60 + timeSplit[1])
        if splitLen == 1:
            msecs = timeSplit[0] * 1000
        return msecs

    def startBtnSlot(self):
        if self.timeEdit.text() != '0:00' and self.timeEdit_2.text() != '0:00' \
            and self.lineEdit.text() != ''  and self.lineEdit_2.text() != '' \
            and not self.isTimeStart:
            self.workTime = self.inputTimePross(self.lineEdit.text())
            self.breakTime = self.inputTimePross(self.lineEdit_2.text())
            self.workStartTime = self.timeEdit.time()
            self.workEndTime = self.timeEdit_2.time()
            self.timeDistribute()
        else:
            pass

    def timeDistribute(self):
        self.isTimeStart = True
        self.toStart = QTime.currentTime().msecsTo(self.workStartTime)
        if(self.toStart >= 0):
            self.waitStartTime.start()
        else:
            self.workAndBreak()

    def waitStartTimeSlot(self):
        self.toStart = QTime.currentTime().msecsTo(self.workStartTime)
        if self.toStart <= 0:
            self.waitStartTime.stop()
            self.workAndBreak()
        else:
            self.lcdDisplay(self.toStart, 1)

    def workAndBreak(self):
        diff = abs(self.workEndTime.msecsTo(QTime.currentTime()))
        mod = diff % (self.workTime + self.breakTime)
        self.workCount = diff//(self.workTime + self.breakTime)
        if(mod != 0):
            self.restTime[0] = int((mod * (self.workTime/(self.workTime + self.breakTime)))/1000)*1000
            self.restTime[1] = int((mod - self.restTime[0])/1000)*1000
        else:
            self.restTime[0] = 0
            self.restTime[1] = 0
        if(self.workCount==0):
            self.workTime, self.breakTime = self.restTime
        self.setTime(self.workTime)

    def setTime(self, time):
        self.startTime = QDateTime.currentMSecsSinceEpoch()
        self.lcdDisplay(time, 2)
        self.workTime = time + 1000
        self.time.start()

    def lcdDisplay(self, interval, lcdnum):
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
        if(lcdnum==1):
            self.lcd_ToStart.display(intervals)
        else:
            self.lcd_Work.display(intervals)

    def startWork(self):
        self.endTime = QDateTime.currentMSecsSinceEpoch()
        interval = self.endTime - self.startTime
        if interval <= self.workTime:
            interval = self.workTime - interval
            self.lcdDisplay(interval, 2)
        else:
            self.time.stop()
            self.hide()
            if(self.workCount == 0):
                self.child.startBreak(self.restTime[1])
            else:
                self.child.startBreak(self.breakTime)


    
        