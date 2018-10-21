from selenium import webdriver
from selenium.webdriver.common.by import By
# WebDriverWait는 Selenium 2.4.0 이후 부터 사용 가능합니다.
from selenium.webdriver.support.ui import WebDriverWait
# expected_conditions는 Selenium 2.26.0 이후 부터 사용 가능합니다.
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
import os
import re

## python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# PhantomJS의 경우 | 아까 받은 PhantomJS의 위치를 지정해준다.
#driver = webdriver.PhantomJS('./app/phantomjs')

#driver.implicitly_wait(20)
# url에 접근한다.
data = {}
def make_json_stock_price_data(url):
    # Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
    driver = webdriver.Chrome('./app/chromedriver')
    driver.get(url)

    pattern = re.compile(r'/quotes/(\w+).*data.realtime.trade.price[^>]+>([\d,]+).*class="pL".*/quotes/(\w+).*data.realtime.trade.price[^>]+>([\d,]+)', re.DOTALL)
    pattern2 = re.compile(r'/quotes/(\w+).*data.realtime.trade.price[^>]+>([\d,]+)', re.DOTALL)
    try:
        # WebDriverWait와 .until 옵션을 통해 우리가 찾고자 하는 HTML 요소를
        # 기다려 줄 수 있습니다.
        title = WebDriverWait(driver, 20) \
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.tableB a.txt")))

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        tr = soup.select('div.tableB tbody tr')
        #tr = driver.find_elements_by_css_selector('div.tableB tr')
        i=0
        for n in tr:
            res = pattern.search(str(n))
            if res :
                data[res.group(1)] = res.group(2)
                data[res.group(3)] = res.group(4)
                i=i+2
            else:
                res = pattern2.search(str(n))
                data[res.group(1)] = res.group(2)
                i=i+1
            #code = pattern.sub('', code.get_attribute('href'))
            #print(n.find_element_by_css_selector('a.txt'))
            #print(pattern.sub('',n.get_attribute('href')))
        print(i)
    finally:
        driver.quit()

make_json_stock_price_data('http://finance.daum.net/domestic/all_stocks?market=KOSPI')
make_json_stock_price_data('http://finance.daum.net/domestic/all_stocks?market=KOSDAQ')
with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)

#for n in notices:
#    print(n.text.strip())