import os
from PIL import Image                    # pip3 install pillow
from pytesseract import image_to_string  # pip3 install pytesseract (before install tesseract  with brew, apt-get, or windows installer)
from pdf2image import convert_from_path  # pip3 install pdf2image
from newspaper import Article            # pip3 install newspaper3k
from bs4 import BeautifulSoup as bs      # pip3 install beautifulsoup4
from urllib.request import urlopen
import pandas as pd

class XmlFileParser:
   """
   xml file parser
   """
   def __init__(self,xml_file):
      """
      parse xml file
      """
      self.xml_file=xml_file
      f=open(self.xml_file, "r")
      self.xml_content=bs(f.read(),"lxml")
      
   def get_tag_attributes(self,tag_name,attributes_list):
      """
      get tag attributes into a pandas dataframe
      """
      data=[]
      tag_data=self.xml_content.find_all(tag_name)
      for n in range(len(tag_data)):
         data_buffer={}
         for attribute in attributes_list:
            data_buffer[attribute]=tag_data[n].get(attribute)
         data.append(data_buffer)
      df=pd.DataFrame.from_dict(data)
      return df
   
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
 
def get_pdf_text(pdf_file,resolution=100,tmp_file="page.jpg"):
    """
    Get text from pdf file
    """
    print(f"Extracting text from page {pdf_file}")

    pdf_pages=convert_from_path(pdf_file, resolution)
    number_of_pages=len(pdf_pages)
    document=[None]*number_of_pages
    
    for counter,page in enumerate(pdf_pages):
        print(f"extracting page {counter+1}/{number_of_pages} as text")
        page.save(tmp_file,'JPEG')
        document[counter] = image_to_string(Image.open(tmp_file))
        
    if os.path.exists(tmp_file):
        os.remove(tmp_file)

    return document
