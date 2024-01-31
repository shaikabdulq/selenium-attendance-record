import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

login_url = 'https://webprosindia.com/hitam'
success_url = 'https://webprosindia.com/hitam/StudentMaster.aspx'
attendance_record_url = 'https://webprosindia.com/hitam/Academics/studentacadamicregister.aspx'
attendance_link_text = "ACADAMIC REGISTER"
username = 'ENTER_USERNAME'
password = 'ENTER_PASSWORD'
path = r'PATH_TO_CHROMEDRIVER'

driver = webdriver.Chrome()
driver.get(login_url)
username_input = driver.find_element(By.NAME, value="txtId2")
password_input = driver.find_element(By.NAME, value="txtPwd2")
submit_button = driver.find_element(By.NAME, value="imgBtn2")
username_input.send_keys(username)
password_input.send_keys(password)
submit_button.click()
WebDriverWait(driver, timeout=600)


driver.execute_script('''window.open("https://webprosindia.com/hitam/Academics/studentacadamicregister.aspx","_blank");''')

time.sleep(15)

try:
    alert = driver.switch_to.alert
    alert.dismiss()
except:
    print("No alert present")

time.sleep(120)
driver.quit()
