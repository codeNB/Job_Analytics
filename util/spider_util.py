"""Utilities for custom spider classes (may refactor to class meathods in future)"""
from scrapy.crawler import CrawlerProcess

DEFAULT_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'

def run_spider(spider_class, user_agent=DEFAULT_USER_AGENT):
    """run a crawl for a spider object"""
    process = CrawlerProcess({
        'USER_AGENT': user_agent
    })

    inst = spider_class()
    process.crawl(inst)
    process.start()
