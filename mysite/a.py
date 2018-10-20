from selenium import webdriver
from selenium.webdriver.common.by import By
# WebDriverWait는 Selenium 2.4.0 이후 부터 사용 가능합니다.
from selenium.webdriver.support.ui import WebDriverWait
# expected_conditions는 Selenium 2.26.0 이후 부터 사용 가능합니다.
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome('./app/chromedriver')
# PhantomJS의 경우 | 아까 받은 PhantomJS의 위치를 지정해준다.
#driver = webdriver.PhantomJS('./app/phantomjs')

#driver.implicitly_wait(20)
# url에 접근한다.
driver.get('http://finance.daum.net/domestic/all_stocks?market=KOSPI')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('div.tableB a.txt')



try:
    # WebDriverWait와 .until 옵션을 통해 우리가 찾고자 하는 HTML 요소를
    # 기다려 줄 수 있습니다.
    title = WebDriverWait(driver, 20) \
        .until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.tableB a.txt")))
    small_titles = driver.find_elements_by_css_selector('div.tableB a.txt')
    for n in small_titles:
        print(n.text)
finally:
    driver.quit()

#for n in notices:
#    print(n.text.strip())