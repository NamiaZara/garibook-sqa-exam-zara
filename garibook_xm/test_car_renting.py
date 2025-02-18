import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def generate_random_phone_number():
    prefix = "015"  
    number = ''.join([str(random.randint(0, 9)) for _ in range(8)])  # Generate 8 random digits
    return prefix + number
phone_number = generate_random_phone_number()

driver = webdriver.Chrome()  
driver.get("http://fe.garibook.com/")
driver.maximize_window()
time.sleep(20)
driver.find_element(By.LINK_TEXT, "Log in").click()
time.sleep(10)
driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div[1]/div/input").send_keys(phone_number)
time.sleep(10)
driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div[2]/button").click()
time.sleep(10)
otp_element = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div[1]/div[1]")  # Change class if necessary
otp_code = otp_element.text
print("Extracted OTP:", otp_code)
driver.find_element(By.ID, "otp1").send_keys(otp_code)
time.sleep(10)
driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div[2]/button").click()
time.sleep(10)
driver.find_element(By.XPATH, "//*[@id='uncontrolled-tab-example-tabpane-carRental']/form/div[1]/label[1]").click()
driver.find_element(By.XPATH, "//*[@id='uncontrolled-tab-example-tabpane-carRental']/form/div[2]/div/div[1]/label/div").click()
# Scroll down by 1000 pixels
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(10)
driver.find_element(By.XPATH, "//*[@id='uncontrolled-tab-example-tabpane-carRental']/form/div[2]/div/div[7]/div/button").click()
time.sleep(20)
driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/div[2]/section[2]/div/div/div/div/div[2]/form/div[3]/div/input").send_keys("Khilgaon")
time.sleep(10)

# Get all dropdown options
dropdown_options = driver.find_elements(By.XPATH, "//*[@id='__next']/div[1]/div[2]/section[2]/div/div/div/div/div[2]/form/div[3]/ul/li")  # Replace with the actual XPath of the dropdown options

# Randomly select an option
if dropdown_options:
    random_option = random.choice(dropdown_options)
    time.sleep(10)
    random_option.click()
else:
    print("No dropdown options found for pickup location.")
driver.execute_script("window.scrollBy(0, 350);")
time.sleep(10)
driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/div[2]/section[2]/div/div/div/div/div[2]/form/div[5]/div/input").send_keys("Garibook")
time.sleep(10)

# Get all dropdown options
dropdown_options1 = driver.find_elements(By.XPATH, "//*[@id='__next']/div[1]/div[2]/section[2]/div/div/div/div/div[2]/form/div[5]/ul/li")  # Replace with the actual XPath of the dropdown options

# Randomly select an option
if dropdown_options:
    random_option1 = random.choice(dropdown_options1)
    time.sleep(10)
    random_option1.click()
else:
    print("No dropdown options found for pickup location.")

time.sleep(5)
#dare and time picker
driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/div[2]/section[2]/div/div/div/div/div[2]/form/div[6]/div/div[1]/div/input").click() 
time.sleep(5)

time_pick = driver.find_elements(By.XPATH, "//*[@id='__next']/div[1]/div[2]/section[2]/div/div/div/div/div[2]/form/div[6]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/ul/li") 
# Randomly select an option
if time_pick:
    random_pick = random.choice(time_pick)
    time.sleep(15)
    random_pick.click()
else:
    print("No dropdown options found for pickup location.")

time.sleep(10)
#promocode
driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/div[2]/section[2]/div/div/div/div/div[2]/form/div[7]/div/input").send_keys("Garibook101")
time.sleep(5)

driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/div[2]/section[2]/div/div/div/div/div[2]/form/div[9]/button").click() 

time.sleep(10)  # Wait before closing
driver.quit()
