from bs4 import BeautifulSoup

def remove_html_tags(raw_text):
    """
    function to remove html tags from an inut text 
    """
    text = BeautifulSoup(raw_text).get_text()
    return text