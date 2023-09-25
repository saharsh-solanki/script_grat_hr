from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

    
driver = webdriver.Chrome(options = chrome_options)

driver.get("https://cubexo-software.greythr.com/")

username = driver.find_element_by_xpath("//input[@id='username']")
password = driver.find_element_by_xpath("//input[@id='password']")
login_button = driver.find_element_by_xpath("//button[text()=' Log in ']")

username.send_keys("CSS016")
password.send_keys("s@S7223889629")
login_button.click()

time.sleep(20)  # Wait for 20 seconds

# Morning Scenario: Log In
if time.localtime().tm_hour == 10:
    sign_in_button = driver.find_element_by_xpath("//button[text()='Sign In']")
    sign_in_button.click()

# Evening Scenario: Log Out
elif time.localtime().tm_hour == 20:
    sign_out_button = driver.find_element_by_xpath("//button[text()='Sign Out']")
    sign_out_button.click()

# Close the WebDriver
driver.quit()
