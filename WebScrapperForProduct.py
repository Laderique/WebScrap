#import libraries 
from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib
#excel
import csv
import pandas as pd


# connect to website: 1. URL 2. https://httpbin.org/get
URL = 'https://www.brooksrunning.com/en_us/adrenaline-gts-23-mens-cushioned-running-shoe/110391.html'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

page = requests.get(URL, headers=headers)

#pulling in Doc Type HTML (information) from URL
soup1 = BeautifulSoup(page.content, 'html.parser')

#Making HTML structured with '.prettify()'
soup2= BeautifulSoup(soup1.prettify(), 'html.parser')
#print(soup2)

title= soup2.find('title').get_text()

price= soup2.find('div', attrs={"class":"m-buy-box-header__price"}).get_text()

#cleaning up data 
price = price.strip()[1:4]
title = title.strip()[0:18]
today = datetime.date.today()
header = ['Title','Price','Date']
data = [title, price, today]

#If need to know data type
#type(data)

#'w'=write newline= inserting data no space between csv
with open('BrooksWebScrapperDataSet.csv', 'w', newline='', encoding='UTF8') as f:
    #creating csv
    writer = csv.writer(f)
    #inserting data in csv 
    writer.writerow(header)
    writer.writerow(data) 
    
df = pd.read_csv(r'C:\Users\Laderique\BrooksWebScrapperDataSet.csv')

print(df)

#updating data to the csv

with open('BrooksWebScrapperDataSet.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)   
    
#automate

def check_price():
    URL = 'https://www.brooksrunning.com/en_us/adrenaline-gts-23-mens-cushioned-running-shoe/110391.html'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')

    soup2= BeautifulSoup(soup1.prettify(), 'html.parser')

    title= soup2.find('title').get_text()

    price= soup2.find('div', attrs={"class":"m-buy-box-header__price"}).get_text()
    
    price = price.strip()[1:4]
    
    title = title.strip()[0:18]
    
    import datetime
    today = datetime.date.today()
    
    import csv
    header = ['Title','Price','Date']
    data = [title, price, today]
    
    with open('BrooksWebScrapperDataSet.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data) 
        
    if (price <120):
        send_mail()
while(True):
    check_price()
    time.sleep(86400)

df = pd.read_csv(r'C:\Users\Laderique\BrooksWebScrapperDataSet.csv')

print(df)
#send to email
#def send_mail():
    server = smtplib.SMTP_SSL('smt.gmail.com', 465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('xxxxx@gmail.com','xxxxxxxx')
    
    subject = "The Shoes are below wanted price"
    body = "Go buy shoes now! If they are in Budget."
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'xxxxx@gmail.com',
        msg
    )