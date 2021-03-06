

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


class Url:
    postUrlPrefixs = 'https://gall.dcinside.com'

class Constant:
    MAX_TRY_COUNT = 3
    DEFAULT_WAIT_TIME = 0.5
    POST_LIST_COUNT = 50
    NOT_ALLOWED_CHARACTERS = ['?', '!', '<', '/', '>', '\\', '|', '*', '\"', '♥','✅','❤','★',':','.']
