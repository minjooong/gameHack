from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.service import Service

import time
import string
import re

service = Service(excutable_path='/Users/minjoong/code/geckodriver')
driver = webdriver.Firefox(service = service)

driver.get('http://realsangyun.pythonanywhere.com')

inputText = driver.find_element(By.CSS_SELECTOR, 'input#inputText')
submitButton = driver.find_element(By.CSS_SELECTOR, 'button')

def nowWord():
    ps = driver.find_elements(By.CSS_SELECTOR, 'p')
    thirdP = ps[2].text
    givenWord = thirdP.split()
    return givenWord[1][-1]


inputText.send_keys('식물')
submitButton.click()
lastLetter = nowWord()


driver.execute_script('window.open("");')
driver.switch_to.window( driver.window_handles[1] )
driver.get('https://stdict.korean.go.kr/search/searchDetailWords.do')

#검색할 던어
search = driver.find_element(By.CSS_SELECTOR, 'input#searchKeywords0')
search.send_keys(lastLetter)

#조건
condition = Select(driver.find_element(By.NAME, 'searchConditions'))
condition.select_by_index(2)

syllableStart = driver.find_element(By.CSS_SELECTOR, 'input#searchSyllableStart')
syllableStart.send_keys('2')

syllableEnd = driver.find_element(By.CSS_SELECTOR, 'input#searchSyllableEnd')
syllableEnd.send_keys('5')

# part = driver.find_element(By.CSS_SELECTOR, 'a.t_graybox_l.modal_btn')
# part.click()
# allPart = driver.find_element(By.CSS_SELECTOR, 'input#searchSpCode_all1')
# allPart.click()
# selectPart = driver.find_element(By.CSS_SELECTOR, 'input#searchSpCode2')
# selectPart.click()
# ok = driver.find_element(By.CSS_SELECTOR, 'a.remodal-close')
# ok.click()

#검색
searchButton = driver.find_element(By.CSS_SELECTOR, 'a.btn_search')
searchButton.click()


answer = driver.find_element(By.CSS_SELECTOR, 'a.t_blue1')
answer = answer.text

answer = answer.translate(str.maketrans('', '', string.punctuation))
answer = re.sub(r"[0-9]", "", answer)
print(answer)