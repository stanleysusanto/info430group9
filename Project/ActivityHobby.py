import os
import requests
import time

from bs4 import BeautifulSoup as bs 
import pandas as pd 
import pyodbc

csv_filepath = os.path.join(os.path.dirname(__file__), 'output.csv')    

def scrape_urls():
    ActivitiesHobby = []
    url = 'https://simplicable.com/en/hobbies'
    print('Scraping url', url)
    urlPage = requests.get(url)
    soup = bs(urlPage.content, 'html.parser')

    ActivityHobbyName = []
    try: 
        ActivityHobbyName = soup.find_all("td", attrs={"style": "width:40vw"})
    except:
        print("cant do it")   

    for i in range(len(ActivityHobbyName)):
        newString = ActivityHobbyName[i].text 
        ActivitiesHobby.append([newString])
        time.sleep(1)

    columns = ['ActivityHobbyName']
    df = pd.DataFrame(ActivitiesHobby, columns=columns)
    
    df.to_csv(csv_filepath, index = False)
    

def insert_to_db():
    # Read our csv we created earlier but tell Pandas to not mess with 'N/A' values
    df = pd.read_csv(csv_filepath, keep_default_na=False)

    server = 'info430group9.database.windows.net'
    database = 'INFO430_GROUP_PROEJCT'
    username = 'info430group9'
    password = 'group91234!'
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()
    for index, row in df.iterrows():
        cursor.execute("INSERT INTO dbo.ACTIVITY_HOBBY (ActivityHobbyName) values(?)", row.ActivityHobbyName)
    conn.commit()
    cursor.close()

if __name__ == '__main__':
    scrape_urls()
    #insert_to_db()
