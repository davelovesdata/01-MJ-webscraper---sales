# MJ-webscraper---sales
scraper to retrieve marijuana sales files

This python file uses Beautifulsoup and regex to identify and download excel files containing county level marijuana sales data from the following public facing website: https://www.colorado.gov/pacific/revenue/colorado-marijuana-sales-reports.

Due to the number of files (65 at the time of this writing) and the wait time, socket errors occasionally and randomly occur. Requests.get() is set to verify=False to prevent the program from stopping. A 30 second wait is implemented to prevent overwhelming the colorado.gov server.

The file 'Web Scraper Sales.ipynb' is a jupyterLab notebook that I will be adding narrative as I get the chance. web scraper sales.py is the shortened script.

Files are saved in the format mmyy_sales.xlsx.

Resources:<br>
https://pythonspot.com/extract-links-from-webpage-beautifulsoup/<br>
https://www.geeksforgeeks.org/downloading-files-web-using-python/
