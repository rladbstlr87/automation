import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

driver = webdriver.Chrome()

newbt_url = 'https://newbt.kr/문제/62306/'
driver.get(newbt_url)

res = requests.get(newbt_url)

next_question = driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-info')

for i in range(5):
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    h5 = soup.select_one('#main > div > div.col-sm-8.blog-main > div.blog-post.question > h5')
    for span in h5.find_all('span', class_='number'):
        span.extract()
    question = h5.get_text()
    
    li_list = soup.select('#main > div > div.col-sm-8.blog-main > div.blog-post.question > ul > li')
    options = [
        re.sub(r'^(①|②|③|④)(?!\s)', r'\1 ', li.get_text(strip=True))
        for li in li_list
    ]

    print('\n' + f'{question}\n' + '\n'.join(options))

    try:
        next_question = driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-info')
        next_question.click()
        time.sleep(5)
    except:
        break