"""creates scrapy spider to get all job posts in query"""
import re
from time import sleep
import bs4 as bs
import scrapy
from scrapy.crawler import CrawlerProcess


def run_target_search(target:str, output:str):
    """ 'target' is the url of the job search. 
        'output' is the name of the output file. 
        
        Executes the spider dumping the results to output        
    """
    outfile = open(output, 'w')

    class Target_Search(scrapy.Spider):
        """subclass of scrapy.Spider for scraping indeed results"""
        name = 'job-posts'
        custom_settings = {'LOG_LEVEL': 'INFO'}
        start_urls = [
            target,
        ]

        def parse(self, response):
            """main method of the spider class collects input and new content"""
            # collect job posts
            print('Scraping ' + response.url + '...')
            soup = bs.BeautifulSoup(response.body, 'lxml') 

            for post in soup.find_all(attrs={'class': 'row'}): # loops through each tag with row class
                #get posting url
                url = post.a['href']

                print(url, file=outfile) # prints the url into the ouptut file

            sleep(2) # wait 2 sec to space out requests

            index = int(re.search(r'start=(\d+)', response.url).group(1)) # gets the offset of page

            # find all np tags (prev, next buttons)
            next_page = len(soup.find_all(attrs={'np'}))
            next_q = index + 10
            
            if next_page > 1 or index < 10: # after the first page stop if there is no next page
                next_page = response.url.replace(f'start={index}', f'start={next_q}') # construct URL
                return response.follow(next_page, self.parse)

    
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    })
    process.crawl(Target_Search)
    process.start()
    

if __name__ == "__main__":
    TARGET = open('../job_query.txt').readline()
    OUTPUT = 'post_urls.txt'
    run_target_search(TARGET, OUTPUT)