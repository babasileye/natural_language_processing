import os
from PIL import Image # pip3 install pillow
from pytesseract import image_to_string  # pip3 install pytesseract (before install tesseract  with brew, apt-get, or windows installer)
from pdf2image import convert_from_path  # pip3 install pdf2image


class PdfTextExtractor:

   def __init__(self,pdf_file,resolution=100,tmp_file="page.jpg"):
      """
      """
      self.pdf_pages=convert_from_path(pdf_file, resolution)
      self.number_of_pages=len(pdf_pages)
      self.tmp_file=tmp_file
      
   def get_page_text(self,page_num,delete_tmp_file=True):
      """
      get text for a single page
      """
      self.pdf_pages[page_num].save(self.tmp_file,'JPEG')
      text=image_to_string(Image.open(self.tmp_file))
      if os.path.exists(tmp_file) and delete_tmp_file:
        os.remove(self.tmp_file) 
      return text
      
   def get_document_texts(self):
      """
      """
      document=[None]*self.number_of_pages
      for page_num,page in enumerate(pdf_pages):
        print(f"extracting page {page_num+1}/{number_of_pages} as text")
        document[counter]=self.get_page_text(self,page_num,delete_tmp_file=False)
        
      if os.path.exists(self.tmp_file):
         os.remove(tmp_file)

    return document

