import uiSetPage
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QDateTime,QDate,Qt 

class SetPage(QtWidgets.QMainWindow, uiSetPage.Ui_Setting):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.slot_btn_function)  
        self.lineEdit.setText('3')
        self.lineEdit_2.setText('3')
        self.time = QTimer(self)
        self.time.setInterval(100)
        self.time.timeout.connect(self.startWork)
        self.workTime = 0
        self.startTime = 0
        self.endTime = 0
        self.isTimeStart = False

    def child(self, child):
        self.child = child

    def slot_btn_function(self):
        if self.lineEdit.text() != '' and not self.isTimeStart:
            self.isTimeStart = True
            self.setTime(self.lineEdit.text())

    def setTime(self, time):
        self.startTime = QDateTime.currentMSecsSinceEpoch()
        if '：' in time:
            timeSplit = [int(x) for x in time.split('：')]
        else:
            timeSplit = [int(x) for x in time.split(':')]
        splitLen = len(timeSplit)
        if splitLen == 3:
            self.workTime = 1000*(timeSplit[0]*60*60 + timeSplit[1]*60 + timeSplit[2])
        if splitLen == 2:
            self.workTime = 1000*(timeSplit[0]*60 + timeSplit[1])
        if splitLen == 1:
            self.workTime = timeSplit[0] * 1000
        self.lcdDisplay(self.workTime)
        self.workTime += 1000
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
            if self.lineEdit_2.text() != '':
                self.hide()
                self.child.startBreak(self.lineEdit_2.text()) 
            self.isTimeStart = False

    
        