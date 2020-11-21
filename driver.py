from selenium import webdriver
from src import DirPath
from src import Constant


class IDriver:
    def __init__(self):
        self.driver = webdriver.Chrome(DirPath.chromeDriverPath)
        self.driver.maximize_window()

    def movePage(self,url):
        self.driver.get(url)

    def findElement(self, Xpath):
        for i in range(Constant.MAX_TRY_COUNT):
            try:
                return IElement(Xpath, self.driver.find_element_by_xpath(Xpath))
            except:
                self.wait(Constant.DEFAULT_WAIT_TIME)
        return None

    def existElement(self, Xpath):
        if self.findElement(Xpath) is None:
            return False
        else:
            return True

    def notExistElement(self, Xpath):
        return self.existElement(Xpath) is False

    def wait(self, time):
        self.driver.implicitly_wait(time)

    def backToPrevPage(self):
        self.driver.back()

    def closeDriver(self):
        self.driver.close()

    def excecuteScriptToElement(self, script, element):
        return self.driver.execute_script(script, element.element)


class IElement:
    def __init__(self, XPath, element):
        self.XPath = XPath
        self.element = element

    def click(self):
        self.element.click()

    def getTitle(self):
        txt = self.element.text
        ret = ""
        notAllowedCharacter = ['?','!','<','/','>','\\','|','*','\"','♥']
        for c in txt:
            if c in notAllowedCharacter:
                pass
            else:
                ret += c
        return ret

    def getText(self):
        return self.element.text

    def getAttribute(self,attr):
        return self.element.get_attribute(attr)
