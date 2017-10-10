"""Second spider to run, gathers text from job post entries"""
from urllib.parse import urlparse
from time import sleep
from bs4 import BeautifulSoup
from bs4.element import Comment
import scrapy

def merge_link(url: str) -> str:
    """merge url with https://www.indeed.ca/"""
    return 'https://www.indeed.ca' + url

def tag_visible(element):
    """tests if element is a visible element on webpage"""
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    elif isinstance(element, Comment):
        return False
    else:
        return True

def text_from_html(body: str):
    """selects visible text from html"""
    soup = BeautifulSoup(body, 'html.parser')
    text = soup.findAll(text=True)
    visible_text = filter(tag_visible, text)
    return u' '.join(t.strip() for t in visible_text) 

def create_followup(post_urls: str, outfile: str):
    """creates followup spider obj
        post_urls: file name of a file containing links to jobposts
        outfile: desired name of output file

        Uses a spider to gather data from the results of the target_search spider.

    """
    out = open(outfile, mode='w')

    class FollowUp(scrapy.Spider):
        """spider to follow links in post_urls"""
        name = 'followup'
        
        start_urls = list(map(merge_link, open(post_urls, 'r'))) #creates list from POST_URLS

        def parse(self, response):
            """defines spider behavior TODO change so that it extracts data from post pages"""
            sleep(2)
            print(text_from_html(response.body), file=out)
            

    return FollowUp