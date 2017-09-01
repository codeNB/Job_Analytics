# Job Analytics Project
Scrape Job Search engine for software jobs and analyze the results.
Using the Indeed job search engine, search for software related jobs within New Brunswick, Canada. Then crawl job postings pages to collect analytics data on each job.
Save to database and visualize with front-end interface.

## Getting python
Code in the base of this project is going to be done using python 3.6
Available for download [here](https://www.python.org/downloads/)

There are specific instructions based on your specific OS

## Setting up a virtual environment:
It is recommended that you create a virtual environment for projects like this, basically a 
local install of a python interpreter intended to be used only for that project.

```
python3 -m venv /path/to/new/virtual/environment
source /path/to/env/bin/activate
deactivate
```
(these are the Linux instructions)

#Current packages to install
## for data collection
```
pip install scrapy
pip install bs4
pip install selenium #not required yet
``` 
*note selenium also needs web drivers to work with particular web browsers*

## for data exploration, etc.
TBD

# Running the spider
Once the required packages are installed the following command will run the spider, and output the file to
SOME-FILE.json. Caution the current version of target_search will crawl through the entire search which will take a while.
```
scrapy runspider target_search.py -o SOME-FILE.json
```