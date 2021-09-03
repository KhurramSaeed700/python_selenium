import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# os.environ['PATH'] += r"D:/chromedriver"
driver = webdriver.Chrome('D:/chromedriver')
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
driver.implicitly_wait(5)


# code for handling with ad popup
try:
    no_button = driver.find_element_by_class_name('at-cm-no-button')
    no_button.click()
    print('ad skipped')
except:
    print('No ad popup')



sum1 = driver.find_element_by_id('sum1')
sum2 = driver.find_element_by_id('sum2')

sum1.send_keys(15)
sum2.send_keys(15)

# progress_element = driver.find_element_by_class_name('progress-label')
# print(f"{progress_element.text == 'Completed!'}")

# WebDriverWait(driver, 30).until(
#     EC.text_to_be_present_in_element(
#         (By.CLASS_NAME, 'progress-label'), 'Completed!'
#     )
# )