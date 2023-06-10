#周松霆
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget



# PATH = "C:/Users/user/Desktop/webdriver111.0.5563.64/chromedriver.exe"
# 周松霆
PATH = " your chromedriver location"
driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com/")

username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')

password.clear()

username.send_keys('your account name')
password.send_keys('pw') 

login.click() 
time.sleep(2)

time.sleep(2)
driver.find_element(By.XPATH,'//*[@type="button"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@class="_a9-- _a9_1"]').click()

time.sleep(1)
driver.find_elements_by_xpath('//*[@class="_ab6-"]')[1].click()
time.sleep(1)

search = driver.find_element_by_class_name("_aauy")
search.click()
keyword = "#cosplay"    #chose the words to search
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

time.sleep(1)
imgs = driver.find_elements_by_xpath('//*[@class="x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3"]')
# for img in imgs:
#      print(img.get_attribute("src"))  
path = os.path.join(keyword)
os.mkdir(path)

count = 0
for img in imgs:
    save_as = os.path.join(path, keyword +str(count) + '.jpg')
    # print(img.get_attribute("src"))
    wget.download(img.get_attribute("src"),save_as)
    count += 1
