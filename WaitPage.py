import uiWaitPage
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtCore import QTimer,QDateTime,QDate
from PyQt5.QtWidgets import QLCDNumber
import time
#继承Ui_Form
class WaitPage(QtWidgets.QMainWindow, uiWaitPage.Ui_Waitting):
    def __init__(self, ):
        super().__init__()
        self.setupUi(self)
        self.time = None
        self.timerId = 0
        self.workTime = 0
        self.breakTime = 0
        self.startTime = 0
        self.endTime = 0
        self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber.setStyleSheet("border: 2px solid black; color: red; background: silver;")

    def parent(self, parent):
        self.parent = parent

    def closeEvent(self, event):
        self.time.stop()
        self.parent.show()
    
    def setTime(self, workTime):
        self.setWorkTime(workTime)
        self.startTime = QDateTime.currentMSecsSinceEpoch()
        self.time = QTimer(self)
        self.time.setInterval(1000)
        self.time.timeout.connect(self.refresh)
        self.lcdNumber.display('0')
        self.time.start()

    def setWorkTime(self, workTime):
        workTimeSplit = [int(x) for x in workTime.split(':')]
        splitLen = len(workTimeSplit)
        if splitLen == 3:
            self.workTime = 1000*(workTimeSplit[0]*60*60 + workTimeSplit[1]*60 + workTimeSplit[2])
        if splitLen == 2:
            self.workTime = 1000*(workTimeSplit[0]*60 + workTimeSplit[1])
        if splitLen == 1:
            self.workTime = workTimeSplit[0] * 1000

    def refresh(self):
        self.endTime = QDateTime.currentMSecsSinceEpoch()
        interval = self.endTime - self.startTime
        print(interval)
        print(self.workTime)
        if interval <= self.workTime:
            interval = self.workTime - interval
            hour = interval // (60 * 60 * 1000)
            minu = (interval - hour * 60 * 60 * 1000) // (60 * 1000)
            sec = (interval - hour * 60 * 60 * 1000 - minu * 60 * 1000) // 1000
            intervals = str(hour) + ':' + str(minu) + ':' + str(sec)
            self.lcdNumber.display(intervals)
        else:
            self.time.stop()