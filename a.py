from bs4 import BeautifulSoup
from urllib import request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime
import json

base_url = "https://economictimes.indiatimes.com"

def extract_news_text(link):
    news_list = []
    try:
        page = request.urlopen(link)
        soup = BeautifulSoup(page, "lxml")
        content = soup.find_all("section", class_="main_container pd0")
        if content:
            news = content[0].find_all("section", id="pageContent")
            if news:
                news = news[0].find_all("a")
                for n in news:
                    news_list.append(n.text.strip())
    except Exception as e:
        print(f"Failed to extract news from {link}: {e}")
    return news_list

def extract_news(month, year, max_days=3):
    driver = webdriver.Chrome()
    news_by_date = {}
    
    url = base_url + month
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    
    try:
        calendar = wait.until(EC.presence_of_element_located((By.ID, "calender")))
        links = calendar.find_elements(By.TAG_NAME, "a")
        
        for link in links:  
            date = link.text.strip()
            if not date:
                continue
            month_num = month.split(',')[1].split('-')[1].split('.')[0]
            full_date = f"{date} {month_num} {year}"
            formatted_date = datetime.strptime(full_date, "%d %m %Y").strftime("%Y-%m-%d")
            
            news_url = link.get_attribute("href")
            headlines = extract_news_text(news_url)
            
            news_by_date[formatted_date] = headlines
            
            print(f"Finished processing {formatted_date}")
    
    except Exception as e:
        print(f"Failed to process month {month}: {e}")
    finally:
        driver.quit()
    
    return news_by_date

def get_month_urls(year):
    months = [f'/archive/year-{year},month-{i}.cms' for i in range(1, 13)] # Change number of months here
    return months


years = [2023,2022,2021]




all_news_data = {}

for year in years:
    monthly_urls = get_month_urls(year)
    for month_url in monthly_urls:
        print(f"Processing month: {month_url}")
        news_data = extract_news(month_url, year)
        all_news_data.update(news_data)


df = pd.DataFrame([(date, json.dumps(headlines)) for date, headlines in all_news_data.items()],
                  columns=['Date', 'Headlines'])


df.to_csv(f"economic_times_news_{year}.csv", index=False)
print(f"Data extraction complete. CSV file created for the year {year}.")


print(df.head())
print(f"Total rows: {len(df)}")


if not df.empty:
    first_date = df.iloc[0]['Date']
    first_date_headlines = json.loads(df.iloc[0]['Headlines'])
    print(f"\nSample headlines for {first_date}:")
    for headline in first_date_headlines[:5]:
        print(f"- {headline}")
    print("...")
else:
    print("No data was extracted.")
