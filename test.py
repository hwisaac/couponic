from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pyautogui as py
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

options = Options()
# options.add_argument('--start-maximized')
# options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
url = "https://wearebraindead.com/products/brain-dead-x-homeshake-horsie-lp-yellow?variant=44150010937475"
driver.get(url)  ## 사이트 접속

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
a = soup.find_all("section")
print(a[0].get_text())
