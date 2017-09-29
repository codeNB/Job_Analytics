from urllib.parse import urlparse
from collections import defaultdict
from time import sleep
import scrapy
from scrapy.crawler import CrawlerProcess



def merge_link(url:str) -> str:
    """merge url with https://www.indeed.ca/"""
    return 'https://www.indeed.ca' + url

def run_followup(post_urls, outfile):

    class FollowUp(scrapy.Spider):
        """spider to follow links in post_urls"""
        name = 'followup'
        domains = defaultdict(int) # default of domains['some key'] = 0

        start_urls = list(map(merge_link, open(post_urls, 'r'))) #creates list from POST_URLS

        def parse(self, response):
            sleep(2)
            dom = urlparse(response.url).netloc #gets the domain of the response
            self.domains[dom] += 1 # counts occurrences of that domain 

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    })
    dom_count = FollowUp()
    process.crawl(dom_count)
    process.start()
    log = open(outfile, 'w') 
    for key, value in dom_count.domains.items():
        print(key + ', ' + str(value), file = log) 

if __name__ == "__main__":
    POST_URLS = 'post_urls.txt'
    LOGFILE = 'domain_count.txt'
    run_followup(POST_URLS, LOGFILE)
