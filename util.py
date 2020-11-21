import os
import shutil
from src import DirPath
from datetime import datetime


class Logger:
    def __init__(self):
        nowTime = datetime.now().__str__().replace(':','').split('.')[0]
        logDirPath = DirPath.saveDirPath+'\\log\\'
        logFilePath = logDirPath + nowTime.__str__() + '.txt'
        try:
            os.makedirs(logDirPath)
        except:
            pass
        self.f = open(logFilePath, 'w')

    def print(self, str):
        print(str)
        self.f.write(str + '\n')

    def exit(self):
        self.f.close()

class FileManager:
    def __init__(self, logger):
        self.saveDirPath = DirPath.saveDirPath
        self.downloadDirPath = DirPath.downloadDirPath
        self.log = logger

    def existFile(self, filePath):
        return os.path.exists(filePath)

    def moveFile2SaveDirectory(self, title, fileName):
        try:
            os.makedirs(self.saveDirPath + title)
        except:
            pass
        src = self.downloadDirPath + fileName
        dist = self.saveDirPath + title + "\\" + fileName
        return self.moveFile(src, dist)

    def moveFile(self, srcPath, distPath):
        if self.existFile(srcPath):
            shutil.move(srcPath, distPath)
            return distPath
        else:
            self.log.print("There Not Exist : " + srcPath)
            return None


