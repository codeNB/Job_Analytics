"""Runs a spider on the job_query for further data gathering"""
from spiders.target_search import create_target_search
from util.spider_util import run_spider

if __name__ == "__main__":
    URL = open('data/job_query.txt').readline()
    SEARCH = create_target_search(URL, 'data/search_urls.txt')
    run_spider(SEARCH)
