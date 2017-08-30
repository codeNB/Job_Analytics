import scrapy

TARGET = open('job_query.txt').readline()

class spider(scrapy.Spider):
    name = 'job-posts'
    start_urls = [
        TARGET,
    ]

    def parse(self, response):
        pass