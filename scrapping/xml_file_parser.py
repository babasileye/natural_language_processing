from bs4 import BeautifulSoup as bs # pip3 install beautifulsoup4
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
