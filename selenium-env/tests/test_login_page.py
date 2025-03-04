import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
  service = Service("C:/chromedriver-win64/chromedriver.exe")  # Use full path 
  driver = webdriver.Chrome(service=service)
  driver.implicitly_wait(10)
  yield driver
  driver.quit()

def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")

    login_btn = driver.find_element(By.ID, "login-button")
    login_btn.click()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    #@pytest.mark.parametrize: Runs the same test with multiple inputs (different usernames and passwords).

@pytest.mark.parametrize("username, password, error", [
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    ("invalidUser", "invalidPass", "Epic sadface: Username and password do not match any user in this service")
])
def test_invalid_login(driver, username, password, error):
    driver.get("https://www.saucedemo.com/")
    
    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)

    login_btn = driver.find_element(By.ID, "login-button")
    login_btn.click()

    error_msg_h3 = driver.find_element(By.TAG_NAME, "h3")
    assert error_msg_h3.text == error