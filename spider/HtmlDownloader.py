import urllib2
class HtmlDownloader(object):
    def downloading(self, aUrl):
        response=urllib2.urlopen(aUrl,timeout=10)
        return response.read()