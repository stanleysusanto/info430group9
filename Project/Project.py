import os
import requests
import time 

from bs4 import BeautifulSoup as bs 
import pandas as pd 
import pyodbc

urls = []
csv_filepath = os.path.join(os.path.dirname(__file__), 'output.csv')

def scrape_urls():
    books = []
    urls = ["https://hubres.uw.edu/hubcal/MasterCalendar.aspx?data=UHcG9WyGjKoO9WuaUlDYjg%3d%3d"]
    for url in urls:
        print('Scraping url', url)
        urlPage = requests.get(url)
        soup = bs(urlPage.content, 'html.parser')
        
        Name = ''
        try:
            Name = soup.find("span", attrs={"data-bind": "text:$data.isAllDay() ? $parent.formatDateTime($data, 'DateShort', $element) + ' (All day)' : $parent.formatDateTime($data, 'DateTimeShort', $element)"}).text
        except:
            print('Could not scrape url: ', url)
            continue

        books.append([Name])
        time.sleep(1)
    print(Name); 
    columns = ['Name']
    df = pd.DataFrame(books, columns=columns)
    
    df.to_csv(csv_filepath, index = False)

if __name__ == '__main__':
    # crawl_urls()
    scrape_urls()
    # Comment this out until you feel your data within your csv looks good, then push to your table