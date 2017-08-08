import re
from bs4 import BeautifulSoup
import urllib2
download=urllib2.urlopen('http://acm.zju.edu.cn/onlinejudge/showProblems.do?contestId=1&pageNumber=1')
text=download.read()
print text
soup=BeautifulSoup(text,'html.parser',from_encoding='utf-8')
res=soup.find_all('a',href=re.compile(r'/onlinejudge/showProblems\.do\?contestId=1&pageNumber=\d+'))
print res