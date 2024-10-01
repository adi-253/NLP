from bs4 import BeautifulSoup
from urllib import request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd



base_url="https://economictimes.indiatimes.com"

url="https://economictimes.indiatimes.com/archive.cms"

front_page=request.urlopen(url)
front_html=BeautifulSoup(front_page,"lxml")

# extracting month and year link
def extract_links_year_month(front_html):
    content=front_html.find_all("section",class_="main_container pd0")

    table=content[0].find_all("table")
    date=table[0].find_all("a",class_="normtxt")
    news_day=[]
    for day in date:
        news_day.append(day.get("href"))
    news_day=news_day[:50]
    return news_day
    
months=extract_links_year_month(front_html) 

# for now taking 2021-2023 for easy  creation

months=months[9:-5]

print(months)

news=pd.DataFrame(columns=["Date","Headline"])

def extract_news_text(link):
    n=[]
    page=request.urlopen(link.get_attribute("href"))
    soup=BeautifulSoup(page,"lxml")
    content=soup.find_all("section",class_="main_container pd0")
    news=content[0].find_all("section",id=="pageContent")
    news=news[0].find_all("a")
    news
    for n in news:
        print(n.text)


def extract_news(months):
    driver = webdriver.Chrome()
   
    for m in months[:1]:
        url=base_url+m
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        calendar = wait.until(EC.presence_of_element_located((By.ID, "calender")))
        
        links = calendar.find_elements(By.TAG_NAME, "a")
        for link in links[:1]:
              extract_news_text(link)
    driver.quit()
        
        
        
extract_news(months)
    

