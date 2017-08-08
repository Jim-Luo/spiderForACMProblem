from HtmlDownloader import HtmlDownloader
from Outputer import Outputer
from Parser import Parser
from UrlManager import UrlManager


class Spider(object):
    def __init__(self):
        self.urlManager=UrlManager()
        self.htmlDownloader=HtmlDownloader()
        self.parser=Parser()
        self.outputer=Outputer()
    def crawl(self,rootUrl):
        count=0
        self.urlManager.addUrl(rootUrl)
        while(self.urlManager.hasUrl()):
            try:
                aUrl=self.urlManager.getUrl()
                count+=1
                print 'NO. %d %s' %(count,aUrl)
                content=self.htmlDownloader.downloading(aUrl)
                urls,data=self.parser.parsing(aUrl,content)
                self.urlManager.addUrls(urls)
                self.outputer.collecting(data)
                if count==100:
                    break
            except:
                print 'crwal error'
        self.outputer.outputing()


if __name__=='__main__':
    rootUrl=r'''http://acm.zju.edu.cn/onlinejudge/showProblems.do?contestId=1&pageNumber=1'''
    objForSpider=Spider()
    objForSpider.crawl(rootUrl)
