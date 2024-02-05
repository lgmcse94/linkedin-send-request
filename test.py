from ast import keyword
from operator import truediv
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
while(True):
    keyword = "hyderabad software amazon"
    target_count = 1000

    geckodriver_path = 'geckodriver'
    os.environ['PATH'] += os.pathsep + os.path.dirname(geckodriver_path)
    options = webdriver.FirefoxOptions()
    options.binary_location = '/Applications/Firefox.app/Contents/MacOS/firefox-bin'  # Replace with the actual path to your Firefox binary
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.linkedin.com/login")

    username_field = driver.find_element(By.XPATH, '//*[@id="username"]')
    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')

    # Input text into the username and password fields
    time.sleep(2)
    username_field.send_keys("test@gmail.com")
    time.sleep(3)
    password_field.send_keys("Test123")
    time.sleep(2)
    submit_button = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[3]/button')
    page = 1
    submit_button.click()
    time.sleep(20)
    count = 0
    while(True):
        try:
            search_url = f"https://www.linkedin.com/search/results/people/?keywords={keyword}&page={page}"
            driver.get(search_url)
            time.sleep(5)
            connect_buttons = driver.find_elements(By.XPATH, '//*/span[text()="Connect"]')
            for button in connect_buttons:
                button.click()
                time.sleep(2)
                connect_button_ok = driver.find_element(By.XPATH, '//*/span[text()="Send without a note"]')
                connect_button_ok.click()
                count+=1
        except Exception as e:
            time.sleep(3)
        time.sleep(6)
        print("sent:",count)
        page = page+1
        if count >= target_count:
            driver.quit()
            break
    time.sleep(14400) #4 hrs
