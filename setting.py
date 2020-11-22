import os
from enum import Enum
#0 : postListUrl     / Url String
#1 : recommend       / True or False
#2 : downloadDirPath / Dir String
#3 : saveDirPath     / Dir String
#4 : chromeDriverPath/ Dir String
#5 : passExistFile   / True or False

class Setting:
    def __init__(self
               , postListUrl = 'https://gall.dcinside.com/mgallery/board/lists/?id=rlatjsdn'
               , recommend = True
               , downloadDirPath = 'C:/Users/park/downloads/'
               , saveDirPath = 'C:/Users/park/PycharmProjects/dc-bob-chroller/save/'
               , chromeDriverPath = 'C:/Users/park/Downloads/chromedriver_win32/chromedriver.exe'
               , passExistFile = True
               ):
        self.postListUrl = postListUrl
        self.recommend = recommend
        self.downloadDirPath = downloadDirPath
        self.saveDirPath = saveDirPath
        self.chromeDriverPath = chromeDriverPath
        self.passExistFile = passExistFile

        settingFilePath = os.curdir + '/settings.txt'
        if not os.path.exists(settingFilePath):
            self.writeSettings()
        else:
            self.setSettings(self.readSettings())

    def readSettings(self):
        settingFilePath = os.curdir + '/settings.txt'
        f = open(settingFilePath, 'r', encoding='utf-8')
        sts = f.readlines()
        for i in range(len(sts)):
            sts[i] = sts[i].strip()
        f.close()
        return sts

    def writeSettings(self):
        settingFilePath = os.curdir + '/settings.txt'
        f = open(settingFilePath, 'w', encoding='utf-8')
        f.write(self.postListUrl+'\n')
        f.write(str(self.recommend)+'\n')
        f.write(self.downloadDirPath+'\n')
        f.write(self.saveDirPath+'\n')
        f.write(self.chromeDriverPath+'\n')
        f.write(str(self.passExistFile)+'\n')
        f.close()

    def setSettings(self, sts):
        self.postListUrl = sts[0]
        self.recommend = bool(sts[1])
        self.downloadDirPath = sts[2]
        self.saveDirPath = sts[3]
        self.chromeDriverPath = sts[4]
        self.passExistFile = bool(sts[5])

    def getPageUrl(self):
        return self.postListUrl+('&exception_mode=recommend' if self.recommend else '')+'&page=%d'

    def setMode(self, mode, st=1, en=100000):
        # todo
        pass


class Mode(Enum):
    # todo
    pass