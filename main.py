import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from PyQt5 import QtWidgets, uic
import pyperclip


URL = "https://blog.naver.com/gngjgm/"
driver = webdriver.Chrome('chromedriver')

userID = "gngjgm"
driver.get(url='https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
idBox = driver.find_element(By.ID, 'id')
idBox.click()
pyperclip.copy(userID)
idBox.send_keys(Keys.CONTROL, 'v')

pwBox = driver.find_element(By.ID, 'pw')
pwBox.click()

while (True):
    loginDone = driver.current_url
    if loginDone == 'https://www.naver.com/':
        break
    else:
        time.sleep(0.1)

driver.get(url=URL)
driver.switch_to.frame('mainFrame')

# u_likeit_list_btn 정보 찾기
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'u_likeit_list_btn')))
likeOfPost = driver.find_elements(By.CLASS_NAME, 'u_likeit_list_btn')
for j in range(len(likeOfPost)):
    if likeOfPost[j].aria_role == 'generic':
        if 'off' in likeOfPost[j].get_attribute('outerHTML').split('"')[1]:
            likeOfPost[j - 1].click()
            time.sleep(0.1)
print("Debug")