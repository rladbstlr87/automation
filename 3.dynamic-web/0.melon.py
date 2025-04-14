from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()
URL = 'https://www.melon.com/chart/index.htm'
driver.get(URL)

# song_info = driver.find_element(By.CSS_SELECTOR, 'a.btn.song_info')
# print(song_info.get_attribute('title'))

song_info = driver.find_elements(By.CSS_SELECTOR, 'a.btn.song_info')
# print(len(song_info))
song_list = []

for i in range(10): # range는 오름차순 순위 지정
    song_info[i].click()
    time.sleep(2)

    title = driver.find_element(By.CSS_SELECTOR, 'div.song_name').text
    artist = driver.find_element(By.CSS_SELECTOR, 'div.artist > a > span').text # 'div.artist span 과 같음
    
    # 여러개 찾은 다음 인덱스 접근
    # meta_data = driver.find_elements(By.CSS_SELECTOR, 'div.meta dd')

    # 발매일 정보를 특정
    publish_data = driver.find_element(By.CSS_SELECTOR, 'dl.list > dd:nth-of-type(2)').text
    like = driver.find_element(By.CSS_SELECTOR, '#d_like_count')

    song_list.append(
        [
            title,
            artist,
            publish_data,
            like
        ]
    )

    driver.back()

local_file_path = '/Users/m2/damf2/data/melon/'

def save_to_scv(song_list):
    with open(local_file_path + 'melon-top100.csv', 'w', encoding='utf-8') as file: # 정규화 해도 됨
        writer = csv.writer(file)
        writer.writerows(song_list)

save_to_csv(song_list)

