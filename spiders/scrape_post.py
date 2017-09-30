from urllib.parse import urlparse
from collections import defaultdict
from time import sleep
import scrapy
from scrapy.crawler import CrawlerProcess

def merge_link(url:str) -> str:
    """merge url with https://www.indeed.ca/"""
    return 'https://www.indeed.ca' + url

def create_followup(post_urls, outfile):
    """creates followup spider obj"""

    class FollowUp(scrapy.Spider):
        """spider to follow links in post_urls"""
        name = 'followup'
        domains = defaultdict(int) # default of domains['some key'] = 0

        start_urls = list(map(merge_link, open(post_urls, 'r'))) #creates list from POST_URLS

        def parse(self, response):
            """defines spider behavior TODO change so that it extracts data from post pages"""
            sleep(2)
            dom = urlparse(response.url).netloc #gets the domain of the response
            self.domains[dom] += 1 # counts occurrences of that domain 

    return FollowUp