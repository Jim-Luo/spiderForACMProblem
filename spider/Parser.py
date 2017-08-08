from bs4 import BeautifulSoup
import re
import urllib2
import urlparse
class Parser(object):
    def _getUrls(self,aUrl, soup):
        urlsPoolForBar=set()
        #<a href="/onlinejudge/showProblems.do?contestId=1&amp;pageNumber=1">Vol 1&nbsp;&nbsp;</a>
        linkForBar=soup.find_all('a',href=re.compile(r'/onlinejudge/showProblems\.do\?contestId=\d+&pageNumber=\d+$'))#bar tag
        for link in linkForBar:
            url=link['href']
            fullUrl=urlparse.urljoin(aUrl,url)
            urlsPoolForBar.add(fullUrl)
        return urlsPoolForBar
        # <a href="/onlinejudge/showProblem.do?problemCode=1101"><font color="blue">Gamblers</font></a>
        # <a href="/onlinejudge/showProblem.do?problemCode=1102"><font color="blue">Phylogenetic Trees Inherited</font></a>
        #linkForProblem=soup.find_all('a', href=re.compile(r'/onlinejudge/showProblem\.do\?problemCode=\d+'))#problem tag

    def _getData(self,aUrl,soup):
        urlsPoolForProblem=set()
        linkForProblem=soup.find_all('a', href=re.compile(r'/onlinejudge/showProblem\.do\?problemCode=\d+'))
        for link in linkForProblem:
            url=link['href']
            fullUrl=urlparse.urljoin(aUrl,url)
            urlsPoolForProblem.add(fullUrl)
        for subUrl in urlsPoolForProblem:
            data={}
            subRequest=urllib2.urlopen(subUrl)
            subContent=subRequest.read()
            subSoup=BeautifulSoup(subContent,'html.parser',from_encoding='utf-8')
            node=subSoup.find('td',id='content')
            data['text']=node.get_text()
            return data



    def parsing(self, aUrl, content):
        if aUrl is None:
            return
        soup=BeautifulSoup(content,'html.parser',from_encoding='utf-8')

        urls=self._getUrls(aUrl,soup)
        data=self._getData(aUrl,soup)
        return urls,data
