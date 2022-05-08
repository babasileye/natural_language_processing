from newspaper import Article            # pip3 install newspaper3k
from bs4 import BeautifulSoup as bs      # pip3 install beautifulsoup4
from urllib.request import urlopen

def get_url_content(url,scrapper="article"):
   """
   get url content with article
   """
   if scrapper=="article":
      article = Article(url)
      article.download()
      article.parse()
      content = {
      "url":url,
      "title":article.title,
      "text":article.text
      }
   elif scrapper=="urllib_bs4":
      webpage=urlopen(url)
      html=webpage.read()
      soup=bs(html,'html.parser')
      content = {
      "url":url,
      "title":soup.title.text,
      "text":soup.get_text()
      }
   else:
      print('unkown scrapper')
      content={'url':'','title':'','text':''}
return content

