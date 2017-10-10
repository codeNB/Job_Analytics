"""Runs a followup spider that is run by the get_posts.py script"""

from pathlib import Path
from spiders.scrape_post import create_followup
from util.spider_util import run_spider

if __name__ == '__main__':
    URL_FILE = Path('data/search_urls.txt')

    if not URL_FILE.is_file():
        print('Please run "get_posts.py" first!')
    else:
        FOLLOWUP = create_followup('data/search_urls.txt', 'data/post_data.txt')
        run_spider(FOLLOWUP)