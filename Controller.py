from driver import IDriver
from bs4 import BeautifulSoup
from util import FileManager, HtmlBuilder, Logger
from src import DirPath, Xpath, Url
from model import Post, PostList, PostStatus

class Controller:
    def __exit__(self):
        self.driver.closeDriver()

    def __init__(self, setting):
        try:
            self.logger = Logger(setting.saveDirPath)
            self.fm = FileManager(setting.saveDirPath, setting.downloadDirPath, self.logger)
            self.driver = IDriver(setting.chromeDriverPath)
            self.setting = setting
        except:
            raise('[error] setting is not valid')


    def chrollPostList(self, postListUrl):
        self.driver.movePage(postListUrl)
        postList = PostList(postListUrl)
        soup = BeautifulSoup(self.driver.getPageSource(), 'html.parser')
        trList = soup.find_all('tr',attrs={'class':'ub-content us-post'})

        soup.get('')
        for trElement in trList:
            if len(trElement.find_all('b'))>0: continue
            postList.addPost(self._initPost(trElement))
        self.logger.print('[done] ' + postListUrl +' 게시글 목록 chrolling 완료')
        return postList

    def chrollInRange(self, startPostNumber, endPostNumber):
        for pageIdx in range(1, 1000):
            postList = self.chrollPostList(self.setting.getPageUrl() % pageIdx)
            postsInRange = postList.getPostsInRange(startPostNumber, endPostNumber)
            for post in postsInRange:
                if self.setting.passExistFile and post.status == PostStatus.ALREADY_EXIST: continue
                self.chrollPost(post)

            for post in postsInRange:
                if post.status == PostStatus.END_CHROLLING:
                    self.moveImages(post)

                if post.status == PostStatus.END_MOVING_IMAGES:
                    self.makeHtml(post)

                self.logger.print('[END]  ' + post.getTitle() + ' 상태 :' + str(post.status))

            if not postList.needToContinue(startPostNumber):
                break

    def _initPost(self, trElement):
        aTagElement = trElement.find('td',attrs={'class':'gall_tit ub-word'}).find('a')
        postNumber = trElement.find('td',attrs={'class':'gall_num'}).text

        title = aTagElement.text.strip()
        url = aTagElement['href']

        post = Post(url=url, number=postNumber, title=title)
        if self.fm.existFile(DirPath.saveDirPath+post.getTitle()+'.html'):
            post.status = PostStatus.ALREADY_EXIST
        else:
            post.status = PostStatus.END_INITIALIZING

        return post

    def chrollPost(self, post):
        self.driver.movePage(Url.postUrlPrefixs+post.url)
        soup = BeautifulSoup(self.driver.getPageSource(), features='html.parser')

        readInnerHTML_script = "return arguments[0].innerHTML;"
        contents = self.driver.excecuteScriptToElement(readInnerHTML_script, self.driver.findElement(Xpath.postBody))

        post.writingTime = self.driver.findElement(Xpath.postWritingTime).getAttribute('title')
        post.bodySoup = BeautifulSoup(contents, 'html.parser')
        post.replySoup = soup.find('div',attrs={'class':'comment_wrap show'})

        emptyElement = self.driver.findElement(Xpath.emptyClickBox)
        emptyElement.click()

        downloadList = []
        for imageIndex in range(1,50):
            if(self.driver.notExistElement(Xpath.saveBtn%imageIndex)): break
            saveBtn = self.driver.findElement(Xpath.saveBtn%imageIndex)
            saveBtn.click()

            downloadFileName = saveBtn.getText().replace('~','_').replace('+',' ')
            downloadList.append(downloadFileName)

        post.downloadList = downloadList
        post.status = PostStatus.END_CHROLLING
        self.logger.print('[done] '+post.getTitle()+' 게시글 chrolling')

    def moveImages(self, post):
        try:
            post.imgList = []
            for file in post.downloadList:
                post.imgList.append(self.fm.moveFile2SaveDirectory(post.getTitle(), file))
            post.status = PostStatus.END_MOVING_IMAGES
        except:
            self.logger.error('[error] '+post.getTitle()+' image 파일 옮기는 과정에서 에러남')


    def makeHtml(self, post):
        try:
            hb = HtmlBuilder(DirPath.saveDirPath, post.getTitle(), post.writingTime, self.logger)
            self._mappingAttributes2SaveImages(post)
            hb.writeBody(str(post.bodySoup))
            hb.writeReply(str(post.replySoup))
            hb.close()
            post.status = PostStatus.END_MAKING_HTML
        except:
            self.logger.error('[error] '+post.getTitle()+' html 빌드 과정에서 에러남')

    def _mappingAttributes2SaveImages(self, post):
        imgTagElementsList = post.bodySoup.find_all('img')
        tagListSize = len(imgTagElementsList)
        downloadImgSize = len(post.downloadList)
        # if tagListSize != downloadImgSize:
        #     self.logger.error('[error] img tag의 갯수(%d)와 download img 갯수(%d)가 다름'%(tagListSize,downloadImgSize))
        # dc 이모티콘으로 인해 img 갯수가 많을 수 있습니다
        for i in range(downloadImgSize):
            filePath = './'+post.getTitle()+'/'+post.downloadList[i]
            element = imgTagElementsList[i]
            element['alt'] = ''
            element['onclick'] = ''
            element['src'] = filePath


