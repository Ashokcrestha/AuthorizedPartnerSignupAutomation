# Signup Automation – Authorized Partner

## Tech Stack
- Language: Python 3.10+
- Automation Framework: Selenium WebDriver
- Browser: Google Chrome
- Driver Management: webdriver-manager
- OS Tested On: Windows 11

##  Setup Instructions
1. Install Python (3.10 or above)
2. Clone repository:
   git clone https://github.com/Ashokcrestha/AuthorizedPartnerSignupAutomation
3. Navigate to project folder:
cd AuthorizedPartnerSignupAutomation
4. Install dependencies:
   pip install -r requirements.txt

## How to Run
python signup_automation_script.py

## Environment
- OS: Windows
- Browser: Chrome (latest)
- Driver: Auto-managed via webdriver-manager
- Internet Required: Yes

## Test Data
- Email: ashok.test45@gmail.com
- Password: Test@1234
- Other Fields: Sample dummy test values

## OTP Handling Strategy
Since:
- OTP is dynamically generated
- OTP is sent to a real mobile/email
- No backend/API access is available

- Real OTP automation is not possible.

- Implemented Solution:
- A mock OTP value is entered automatically.
- The script attempts to submit the OTP form.
- Further progression depends on server-side validation.

## Demo Video
- Click below to watch the demo video:
[Demo Video](./demo_video.mp4)


##  Result
The signup process is automated up to the OTP verification stage without any manual intervention.
Further automation beyond OTP requires access to a test environment or static OTP support.