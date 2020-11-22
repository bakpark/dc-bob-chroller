import os
import shutil
from datetime import datetime
from enum import Enum

class Logger:
    def __init__(self, saveDirPath):
        nowTime = datetime.now().__str__().replace(':','').split('.')[0]
        logDirPath = saveDirPath+'\\log\\'
        self.logFilePath = logDirPath + nowTime.__str__() + '.txt'
        self.errorLogFilePath = logDirPath + nowTime.__str__() +' error.txt'
        try:
            os.makedirs(logDirPath)
        except:
            pass

    def print(self, str):
        print(str)
        with open(self.logFilePath, mode='a', encoding='utf-8') as lf:
            lf.write(str + '\n')

    def error(self, str):
        self.print(str)
        with open(self.errorLogFilePath, mode='a', encoding='utf-8') as ef:
            ef.write(str+'\n')

    def debug(self, str):
        self.print('-[DEBUG] '+str)

class FileManager:
    def __init__(self, saveDirPath, downloadDirPath, logger):
        self.saveDirPath = saveDirPath
        self.downloadDirPath = downloadDirPath
        self.logger = logger

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
            self.logger.error("[error] 다운로드 폴더에 파일 없음 : " + srcPath)
            raise Exception('There Not Exist : " + srcPath')

class HtmlBuilder:
    def __init__(self, dirPath, title, writingTime, logger):
        try:
            os.makedirs(dirPath)
        except:
            pass

        self.logger = logger
        self.nowTime = datetime.now().strftime("%y%m%d%H%M")
        self.writingTime = writingTime
        self.title = title

        self.dirPath = dirPath
        self.filePath = dirPath+"\\"+writingTime+".html"

        self.f = open(dirPath+"\\"+title+".html",mode='w',encoding='utf-8')

        self.f.write("<!DOCTYPE html><html><head><meta charset='utf-8'>")
        self.f.write('<link rel="stylesheet" type="text/css" href="https://nstatic.dcinside.com/dc/w/css/common.css?v=2004211415">')
        self.f.write("<title>"+ self.title + "</title></head><body>")
        self.f.write("<h1>"+self.title+"</h1>")
        self.f.write("<h5>"+self.writingTime+"</h5>")

    def writeBody(self, bodyString):
        # encodingBodyString = bodyString.encode("UTF-8")
        self.f.write(bodyString)

    def writeReply(self, replyString):
        self.f.write(replyString)

    def close(self):
        self.f.write("</body></html>")
        self.f.close()
        self.logger.print("[done] "+self.title+" html 빌드 완료")