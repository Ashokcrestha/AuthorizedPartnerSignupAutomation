from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://authorized-partner.vercel.app/")
time.sleep(5)

try:
    login_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Login')]"))
    )

    driver.execute_script("arguments[0].click();", login_element)
    print("Login element clicked successfully.")
except Exception as e:
    print("Error clicking Login element:", e)

try:
    signup_element = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@class='text-primary hover:underline' and contains(text(),'Sign Up')]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", signup_element)
    driver.execute_script("arguments[0].click();", signup_element)
    print("Signup clicked successfully. Now on Register page.")
except Exception as e:
    print("Error clicking Signup:", e)


time.sleep(5)
driver.quit()
