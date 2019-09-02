# -*- coding: utf-8 -*-
"""
Spyder Editor

program to download all excel files at a location. In this case, the Colorado Marijuana sales files.
"""
#required packages
import requests
from bs4 import BeautifulSoup

import re     #regex
import time   #for pausing execution

#website pages to scrape
page = "https://www.colorado.gov/pacific/revenue/colorado-marijuana-sales-reports"  #contains Colorado MJ business sales data

#get the sales webpage
resp = requests.get(page)

#get the webpage content
html = resp.content

#make pretty with bs4
soup = BeautifulSoup(html, 'html.parser')

#find all '<a>' tags (hyperlinks) 
urls = []
for link in soup.findAll('a', attrs={'href': re.compile("PUBLISH.xlsx")}):
    urls.append(link.get('href'))

#The first item is not necessary for my purposes so it is removed
del(urls[0])

#retrieve files and save to local directory
for link in urls: 
        #use regex to split out the date as a filename - only digits are needed
        filename = re.search(r'\d+', link)
        fileext = str('.xlsx')
  
        print("Downloading file:%s"%filename) 
          
        #create response object 
        r = requests.get(link, verify=False) 
          
        #write data to local directory 
        with open(filename.group(0)+'_sales'+fileext, 'wb') as output:
             output.write(r.content)
        
        print("%s downloaded!\n"%filename)
        time.sleep(30)  #avoid overwhelming the server
        
print("All excel files downloaded!")