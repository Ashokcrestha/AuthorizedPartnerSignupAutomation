# signup_automation_script.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Start browser maximized

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://authorized-partner.vercel.app/")

print("Website opened successfully. Page title:", driver.title)

import time
time.sleep(10)

driver.quit()
