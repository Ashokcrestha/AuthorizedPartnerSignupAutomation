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

time.sleep(5)

print("Register page fully opened")

# ---------------- REGISTER PAGE AUTOMATION ----------------

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
    print("Terms & Conditions checkbox clicked")

except Exception as e:
    print("Checkbox click failed:", e)
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

    # ---------------- STEP 1: SET UP YOUR ACCOUNT ----------------

# Wait until Step 1 heading appears
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[contains(text(),'Set up your Account')]")
    )
)

time.sleep(3)  # visible pause

# ---- First Name ----
first_name = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//input[@placeholder='Enter Your First Name']")
    )
)
first_name.send_keys("Ashok")
time.sleep(1)

# ---- Last Name ----
last_name = driver.find_element(
    By.XPATH, "//input[@placeholder='Enter Your Last Name']"
)
last_name.send_keys("Shrestha")
time.sleep(1)

# ---- Email ----
email = driver.find_element(
    By.XPATH, "//input[@placeholder='Enter Your Email Address']"
)
email.send_keys("ashok.test@gmail.com")
time.sleep(1)

# ---- Phone Number (REACT-SAFE FIX) ----

# Wait until Phone Number label is visible
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[contains(text(),'Phone Number')]")
    )
)

time.sleep(2)

# Find the phone input inside the phone container
phone = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located(
        (By.XPATH, "//label[contains(text(),'Phone Number')]/following::input[1]")
    )
)

driver.execute_script(
    "arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
    phone
)
time.sleep(1)

driver.execute_script("arguments[0].focus();", phone)
time.sleep(1)

phone.clear()
phone.send_keys("9866397381")
time.sleep(2)

print("Phone number entered successfully")

# ---- Password ----
password = driver.find_element(
    By.XPATH, "//input[@type='password'][1]"
)
password.send_keys("Test@1234")
time.sleep(1)

# ---- Confirm Password ----
confirm_password = driver.find_element(
    By.XPATH, "(//input[@type='password'])[2]"
)
confirm_password.send_keys("Test@1234")
time.sleep(2)

# ---- Click Next ----
next_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Next')]")
    )
)

driver.execute_script(
    "arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
    next_button
)
time.sleep(2)

driver.execute_script("arguments[0].click();", next_button)
# ---- Click Next after user details ----
driver.execute_script("arguments[0].click();", next_button)
print("User details submitted")

time.sleep(3)

# ---------------- EMAIL OTP VERIFICATION (MOCK) ----------------

# Wait for Email Verification screen
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[contains(text(),'Email Verification')]")
    )
)

print("Email Verification screen opened")
time.sleep(3)

# Dummy OTP (mocked – backend validation not accessible)
mock_otp = "123456"

# Locate OTP input(s)
otp_inputs = driver.find_elements(
    By.XPATH, "//input[@inputmode='numeric' or @type='text']"
)

# Handle multi-box or single-box OTP UI
if len(otp_inputs) >= 6:
    for i in range(6):
        otp_inputs[i].clear()
        otp_inputs[i].send_keys(mock_otp[i])
        time.sleep(0.4)
else:
    otp_inputs[0].clear()
    otp_inputs[0].send_keys(mock_otp)

print("Mock OTP entered")
time.sleep(2)

# Click Verify button
verify_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Verify')]")
    )
)

driver.execute_script("arguments[0].click();", verify_button)
print("Verify button clicked")

# Validate error message (expected behavior)
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[contains(text(),'Invalid')]")
    )
)

print("OTP validation tested successfully (Invalid OTP shown as expected)")

# End test gracefully
time.sleep(4)
driver.quit()



# Final slow wait so you can see next page
time.sleep(6)
driver.quit()
