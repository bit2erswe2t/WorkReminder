import uiSetPage
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QDateTime,QDate,Qt,QTime

class SetPage(QtWidgets.QMainWindow, uiSetPage.Ui_Setting):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.slot_btn_function)  
        self.lineEdit.setText('50')
        self.lineEdit_2.setText('12')
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

    def slot_btn_function(self):
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

    def workAndBreak(self):
        diff = abs(self.workEndTime.msecsTo(QTime.currentTime()))
        #diff = abs(self.workStartTime.msecsTo(self.workEndTime))
        mod = diff % (self.workTime + self.breakTime)
        self.workCount = diff//(self.workTime + self.breakTime)
        #print("workcount", diff, self.workCount, mod)
        if(mod != 0):
            self.restTime[0] = int((mod * (self.workTime/(self.workTime + self.breakTime)))/1000)*1000
            self.restTime[1] = int((mod - self.restTime[0])/1000)*1000
        else:
            self.restTime[0] = 0
            self.restTime[1] = 0
        if(self.workCount==0):
            self.workTime, self.breakTime = self.restTime
        #print("rest:",self.restTime)
        self.setTime(self.workTime)

    def setTime(self, time):
        self.startTime = QDateTime.currentMSecsSinceEpoch()
        self.lcdDisplay(time)
        self.workTime = time + 1000
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
        self.label_4.setText(intervals)

    def startWork(self):
        self.endTime = QDateTime.currentMSecsSinceEpoch()
        interval = self.endTime - self.startTime
        if interval <= self.workTime:
            interval = self.workTime - interval
            self.lcdDisplay(interval)
        else:
            self.time.stop()
            self.hide()
            if(self.workCount == 0):
                self.child.startBreak(self.restTime[1])
            else:
                self.child.startBreak(self.breakTime)


    
        