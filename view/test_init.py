# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\publish\init.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from util import FileManager
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(120, 20, 561, 531))
        self.listWidget.setObjectName("listWidget")
        self.labels = []
        self.textEdits = []
        for i in range(7):
            self.labels.append(QtWidgets.QLabel(self.centralwidget))
            self.labels[i].setGeometry(QtCore.QRect(160, 80+60*i, 121, 31))
            self.labels[i].setObjectName("label_"+str(i))
            self.textEdits.append(QtWidgets.QTextEdit(self.centralwidget))
            self.textEdits[i].setGeometry(QtCore.QRect(300, 80+60*i, 321, 31))

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 500, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DC Bob Chroller"))
        self.labels[0].setText(_translate("MainWindow", "게시글 목록 URL"))
        self.labels[1].setText(_translate("MainWindow", "한 페이지 게시글 수"))
        self.labels[2].setText(_translate("MainWindow", "시작 글 번호"))
        self.labels[3].setText(_translate("MainWindow", "끝 글 번호"))
        self.pushButton.setText(_translate("MainWindow", "시작"))
        self.labels[4].setText(_translate("MainWindow", "기본 다운로드 폴더 경로"))
        self.labels[5].setText(_translate("MainWindow", "저장할 폴더 경로"))
        self.labels[6].setText(_translate("MainWindow", "Chrome Driver 경로"))

        settings = self.readSettingFiles()
        idx = 0
        sz = len(settings)
        while idx<7 and idx<sz:
            self.textEdits[idx].setText((_translate("MainWindow", settings[idx])))
            idx += 1
        self.pushButton.clicked.connect(self.start)

    def start(self):
        print('Button Clicked')

    def readSettingFiles(self):
        print(os.curdir)
        settingFilePath = os.curdir+'/settings.txt'
        if not os.path.exists(settingFilePath):
            f = open(settingFilePath, 'w', encoding='utf-8')
            f.close()
        f = open(settingFilePath, 'r', encoding='utf-8')
        return f.readlines()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

