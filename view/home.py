# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\publish\home.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from Controller import Controller
from setting import Setting


class Ui_MainWindow(object):
    def makeDefaultSettingUi(self):
        self.labels = []
        self.textEdits = []
        for i in range(4):
            self.textEdits.append(QtWidgets.QTextEdit(self.centralwidget))
            self.textEdits[i].setGeometry(QtCore.QRect(300, 70+70*i, 321, 31))
            self.textEdits[i].setObjectName("textEdit_"+str(i))
            self.labels.append(QtWidgets.QLabel(self.centralwidget))
            self.labels[i].setGeometry(QtCore.QRect(160, 70+70*i, 111, 31))
            self.labels[i].setObjectName("label_"+str(i))
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(160, 100, 81, 16))
        self.checkBox.setObjectName("checkBox")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(500, 370, 131, 16))
        self.radioButton.setObjectName("radioButton")

    def makeGroup1Ui(self):
        self.group1Box = QtWidgets.QGroupBox(self.centralwidget)
        self.group1Box.setGeometry(QtCore.QRect(162, 410, 221, 111))
        self.group1Box.setObjectName("groupBox")
        self.group1Box.pushButton = QtWidgets.QPushButton(self.group1Box)
        self.group1Box.pushButton.setGeometry(QtCore.QRect(164, 50, 51, 23))
        self.group1Box.pushButton.setObjectName("startSelectRangeMode")

        self.group1Box.textEdits = []
        self.group1Box.textEdits.append(QtWidgets.QTextEdit(self.group1Box))
        self.group1Box.textEdits[0].setGeometry(QtCore.QRect(70, 30, 61, 25))
        self.group1Box.textEdits[0].setObjectName("startPostNumber")

        self.group1Box.textEdits.append(QtWidgets.QTextEdit(self.group1Box))
        self.group1Box.textEdits[1].setGeometry(QtCore.QRect(70, 70, 61, 25))
        self.group1Box.textEdits[1].setObjectName("endPostNumber")

        self.group1Box.labels = []

        self.group1Box.labels.append(QtWidgets.QLabel(self.group1Box))
        self.group1Box.labels[0].setGeometry(QtCore.QRect(10, 30, 51, 21))
        self.group1Box.labels[0].setObjectName("startPostNumber_label")

        self.group1Box.labels.append(QtWidgets.QLabel(self.group1Box))
        self.group1Box.labels[1].setGeometry(QtCore.QRect(10, 70, 51, 21))
        self.group1Box.labels[1].setObjectName("endPostNumber_label")

    def makeGroup2Ui(self):
        self.group2Box = QtWidgets.QGroupBox(self.centralwidget)
        self.group2Box.setGeometry(QtCore.QRect(420, 410, 201, 111))
        self.group2Box.setObjectName("groupBox_2")
        self.group2Box.pushButton = QtWidgets.QPushButton(self.group2Box)
        self.group2Box.pushButton.setGeometry(QtCore.QRect(70, 50, 51, 23))
        self.group2Box.pushButton.setObjectName("start_ui_mode")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(120, 20, 561, 531))
        self.listWidget.setObjectName("listWidget")

        self.makeDefaultSettingUi()
        self.makeGroup1Ui()
        self.makeGroup2Ui()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labels[0].setText(_translate("MainWindow", "게시판 URL"))
        self.labels[1].setText(_translate("MainWindow", "다운로드 폴더 경로"))
        self.labels[2].setText(_translate("MainWindow", "저장 폴더 경로"))
        self.labels[3].setText(_translate("MainWindow", "Chrome Driver 경로"))
        self.checkBox.setText(_translate("MainWindow", "개념글"))
        self.radioButton.setText(_translate("MainWindow", "존재 파일 건너뛰기"))
        self.group1Box.setTitle(_translate("MainWindow", "번호 지정 받기"))
        self.group1Box.pushButton.setText(_translate("MainWindow", "시작"))
        self.group1Box.labels[0].setText(_translate("MainWindow", "시작 번호"))
        self.group1Box.labels[1].setText(_translate("MainWindow", "끝 번호"))
        self.group2Box.setTitle(_translate("MainWindow", "선택 지정 모드"))
        self.group2Box.pushButton.setText(_translate("MainWindow", "시작"))

        setting = Setting(initSetting=True)
        self.textEdits[0].setText(setting.postListUrl)
        self.textEdits[1].setText(setting.downloadDirPath)
        self.textEdits[2].setText(setting.saveDirPath)
        self.textEdits[3].setText(setting.chromeDriverPath)
        self.checkBox.setChecked(setting.recommend)
        self.radioButton.setChecked(setting.passExistFile)

        self.group1Box.pushButton.clicked.connect(self.startSelectRangeMode)

    # 0 : postListUrl     / Url String
    # 1 : recommend       / True or False
    # 2 : downloadDirPath / Dir String
    # 3 : saveDirPath     / Dir String
    # 4 : chromeDriverPath/ Dir String
    # 5 : passExistFile   / True or False
    def startSelectRangeMode(self):
        postListUrl = self.textEdits[0].toPlainText().strip()
        recommend = self.checkBox.isChecked()
        downloadDirPath = self.textEdits[1].toPlainText().strip()
        saveDirPath = self.textEdits[2].toPlainText().strip()
        chromeDriverPath = self.textEdits[3].toPlainText().strip()
        passExistFile = self.radioButton.isChecked()
        setting = Setting(
            postListUrl=postListUrl,
            recommend=recommend,
            downloadDirPath=downloadDirPath,
            saveDirPath=saveDirPath,
            chromeDriverPath=chromeDriverPath,
            passExistFile=passExistFile,
            initSetting=False
        )
        setting.save()
        controller = Controller(setting)

        st = int(self.group1Box.textEdits[0].toPlainText().strip())
        en = int(self.group1Box.textEdits[1].toPlainText().strip())
        controller.chrollInRange(st,en)
        controller.__exit__()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

