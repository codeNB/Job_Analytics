"""execute full analysis DO NOT USE"""
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from spiders.target_search import create_target_search
from spiders.scrape_post import create_followup


if __name__ == '__main__':
    
    TARGET = open('teacher.txt', 'r').readline()
    TS = create_target_search(TARGET, 'search_urls.txt')
    FU = create_followup('search_urls.txt', 'summary.txt')
    
    configure_logging()
    runner = CrawlerRunner()

    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(TS)
        yield runner.crawl(FU)
        reactor.stop()

    crawl()
    reactor.run()


