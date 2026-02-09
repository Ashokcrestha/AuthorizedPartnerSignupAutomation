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

    # ---------------- CONFIRM REGISTER PAGE ----------------
WebDriverWait(driver, 20).until(
    EC.url_contains("/register")
)

# FORCE slow down AFTER navigation
time.sleep(5)

print("Register page fully opened")

# ---------------- REGISTER PAGE AUTOMATION ----------------

# Make sure Register page is fully loaded
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[contains(text(),'Register Your Agency')]")
    )
)

# Slow down so page is clearly visible
time.sleep(4)
# ---------- CLICK TERMS & CONDITIONS (FIXED) ----------

try:
    # Wait until the text is visible
    agree_label = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//label[contains(.,'I agree to the')]"
        ))
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
        agree_label
    )
    time.sleep(2)

    # Click the LABEL (not the input)
    driver.execute_script("arguments[0].click();", agree_label)
    print("✅ Terms & Conditions checkbox clicked")

except Exception as e:
    print("❌ Checkbox click failed:", e)
time.sleep(2)

# -------- Click Continue button --------
try:
    continue_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Continue')]")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
        continue_button
    )
    time.sleep(2)

    driver.execute_script("arguments[0].click();", continue_button)
    print("Continue button clicked.")

except Exception as e:
    print("Error clicking Continue:", e)

# Final slow wait so you can see next page
time.sleep(6)
driver.quit()
