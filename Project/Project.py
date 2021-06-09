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
    url = 'https://indyschild.com/100-things-to-do-outside-this-summer-at-home/'
    print('Scraping url', url)
    urlPage = requests.get(url)
    soup = bs(urlPage.content, 'html.parser')
    temp = soup.find_all("li", attrs={"style": "font-weight 400;"})
    print(temp)
    Name = ''
    try:
        Name = soup.find("span", attrs={"style": "font-weight: 400;"}).text.strip()
    except:
        print('Could not scrape url: ', url)        

    books.append([Name])
    time.sleep(1)

    columns = ['Name']
    print(Name)
    df = pd.DataFrame(books, columns=columns)
    
    df.to_csv(csv_filepath, index = False)

def insert_to_db():
    # Read our csv we created earlier but tell Pandas to not mess with 'N/A' values
    df = pd.read_csv(csv_filepath, keep_default_na=False)

    server = 'is-info430.ischool.uw.edu'
    database = 'HW4'
    username = 'INFO430'
    password = 'SuperSafePassword1234'
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()
    for index, row in df.iterrows():
        cursor.execute("INSERT INTO dbo.jj_Books (Name,Price,UPC,InStock,Type) values(?,?,?,?,?)", row.Name, row.Price, row.UPC, row.InStock, row.Type)
    conn.commit()
    cursor.close()

if __name__ == '__main__':
    scrape_urls()
    # insert_to_db()