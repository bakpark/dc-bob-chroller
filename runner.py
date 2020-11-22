from util import Logger, Mode
from Controller import Controller
from src import Url, DirPath, Constant
from model import PostStatus, PostList

log = Logger(DirPath.saveDirPath)
log.print('============== BOB CHROLLER ============')

mode = Mode.EXIST_PASS
# mode = Mode.ALL_DOWNLOAD
url = Url.pageRecommendUrl
# url = Url.pageNormalUrl

controller = Controller(log)

for pageIdx in range(1, 1000):
    postList = controller.chrollPostList(url%pageIdx)
    postsInRange = postList.getPostsInRange()
    for post in postsInRange:
        if mode == Mode.EXIST_PASS and post.status == PostStatus.ALREADY_EXIST: continue
        controller.chrollPost(post)

    for post in postsInRange:
        if post.status == PostStatus.END_CHROLLING:
            controller.moveImages(post)

        if post.status == PostStatus.END_MOVING_IMAGES:
            controller.makeHtml(post)

        log.print('[END]  '+post.getTitle()+' 상태 :'+str(post.status))

    if not postList.needToContinue():
        break


