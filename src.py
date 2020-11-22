

class Xpath:
    post = "//*[@id='container']/section[1]/article[2]/div[2]/table/tbody/tr[%d]/td[3]/a"
    postNumber = "//*[@id='container']/section[1]/article[2]/div[2]/table/tbody/tr[%d]/td[1]"

    #in Post Page
    postTitle = "//span[@class='title_subject']"
    postWritingTime = "//span[@class='gall_date']"
    postBody = "//div[@class='writing_view_box']"

    emptyClickBox = "//div[@class='fl num_box']"
    fileCntBox = "//div[ @class ='appending_file_box']/strong/em"
    saveBtn = "//ul[@class='appending_file']/li[%d]/a"

class DirPath:
    chromeDriverPath = r"C:\Users\park\Downloads\chromedriver_win32\chromedriver.exe"
    saveDirPath = "C:\\Users\\park\\PycharmProjects\\dc-bob-chroller\\save\\"
    downloadDirPath = "C:\\Users\\park\\downloads\\"


class Url:
    pageRecommendUrl = "https://gall.dcinside.com/mgallery/board/lists/?id=rlatjsdn&page=%d&exception_mode=recommend"
    pageNormalUrl = "https://gall.dcinside.com/mgallery/board/lists/?id=rlatjsdn&page=%d"
    postUrlPrefixs = 'https://gall.dcinside.com'

class Constant:
    MAX_TRY_COUNT = 3
    DEFAULT_WAIT_TIME = 0.5
    POST_LIST_COUNT = 50
    NOT_ALLOWED_CHARACTERS = ['?', '!', '<', '/', '>', '\\', '|', '*', '\"', '♥','✅','❤','★',':','.']

    START_POST_NUMBER = 2790
    END_POST_NUMBER = 2890
