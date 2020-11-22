from src import Constant
from enum import Enum

class PostList:
    def __init__(self, postListUrl):
        self.url = postListUrl
        self.posts = []

    def addPost(self, post):
        self.posts.append(post)

    def getPostsInRange(self):
        retPosts = []
        for post in self.posts:
            if int(post.number)<Constant.START_POST_NUMBER or int(post.number)>Constant.END_POST_NUMBER:
                continue
            retPosts.append(post)
        return retPosts

    def needToContinue(self):
        firstPost = self.posts[len(self.posts)-1]
        return not (int(firstPost.number) <= max(Constant.POST_LIST_COUNT ,Constant.START_POST_NUMBER))


class Post:
    def __init__(self, url='', number="00", title=""):
        self.url = url
        self.number = number
        self.title = title
        self.status = PostStatus(0)

    def getTitle(self):
        txt = '['+self.number+'] '+self.title
        ret = ""
        notAllowedCharacter = Constant.NOT_ALLOWED_CHARACTERS
        for c in txt:
            if c in notAllowedCharacter: pass
            else:
                ret += c
        return ret.strip()

    def build(self):
        pass

class PostStatus(Enum):
    ALREADY_EXIST = 0
    END_INITIALIZING = 1
    END_CHROLLING = 2
    END_MOVING_IMAGES = 3
    END_MAKING_HTML = 4
