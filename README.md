# Job Analytics Project
Scrape Job Search engine for software jobs and analyze the results.
Using the CareerJet job search engine, search for software related jobs within New Brunswick, Canada. Then crawl job postings pages to collect analytics data on each job.
Save to database and visualize with front-end interface.

## Getting python
Code in the base of this project is going to be done using python 3.6
Available for download [here](https://www.python.org/downloads/)

There are specific instructions based on your specific OS

## Setting up a virtual environment:
It is recomended that you create a virtual environment for projects like this, basically a 
local install of a python interpreter intended to be used only for that project.

```
python3 -m venv /path/to/new/virtual/environment
source /path/to/env/bin/activate
deactivate
```
(these are the linux instructions)

#Current packages to install
## for data collection
```
pip install scrapy
pip install beautifulsoup4
pip install selenium
``` 
*note selenium also needs webdrivers to work with particular webbrowsers*

## for data exploration, etc.
TBD





