from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
import time

driver = webdriver.Chrome()
driver.get("https://google.com")

try:
    # Attempt to switch to an alert
    alert = Alert(driver)
    print("Alert text:", alert.text) #prints the alert text
    alert.accept()  # Or alert.dismiss() to cancel
    print("Alert accepted")
except NoAlertPresentException:
    print("No alert present")

# Continue with your test
# ...
time.sleep(2) #example wait time.
driver.quit()