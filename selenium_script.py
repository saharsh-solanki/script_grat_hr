from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import platform
import os 


print("Running script")
# Configure the Selenium WebDriver with ChromeDriverManager

# Get the operating system
os_name = platform.system()

# Determine the appropriate platform string based on the system
platform_string = None
if os_name == "Windows":
    platform_string = "win64"
elif os_name == "Linux" and os_name == "Darwin":
    platform_string = "linux64"
else :
    platform_string = "mac-x64"

print("os_name",os_name)

chrome_path = {
    "win64":"chroms/window",
     "mac-x64":"chroms/mac"
}

path_ex = os.getcwd() +"/"+chrome_path[platform_string]

print("platform_string",path_ex)
driver = webdriver.Chrome()

driver.get("https://cubexo-software.greythr.com/")
import pdb;pdb.set_trace()

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
