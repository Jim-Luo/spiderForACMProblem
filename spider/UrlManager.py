class UrlManager(object):
    def __init__(self):
        self.oldUrlPool=set()
        self.newUrlPool=set()
    def addUrl(self, rootUrl):
        if rootUrl is None :
            return
        if rootUrl not in self.oldUrlPool and rootUrl not  in self.newUrlPool:
            self.newUrlPool.add(rootUrl)

    def hasUrl(self):
        return len(self.newUrlPool)!=0

    def getUrl(self):
        temp=self.newUrlPool.pop()
        self.oldUrlPool.add(temp)
        return temp

    def addUrls(self, urls):
        if urls is None and len(urls)==0:
            return
        for url in urls:
            self.newUrlPool.add(url)
