import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestValid():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testValid(self):
    self.driver.get("https://demo.guru99.com/test/newtours/")
    self.driver.set_window_size(860, 912)
    self.driver.find_element(By.LINK_TEXT, "REGISTER").click()
    self.driver.find_element(By.NAME, "firstName").click()
    self.driver.find_element(By.NAME, "firstName").send_keys("Alex")
    self.driver.find_element(By.NAME, "lastName").send_keys("Sorichetti")
    self.driver.find_element(By.NAME, "phone").send_keys("9059999999")
    self.driver.find_element(By.ID, "userName").send_keys("alexander.sorichetti@dcmail.ca")
    self.driver.find_element(By.NAME, "address1").send_keys("88 A-Road")
    self.driver.find_element(By.NAME, "city").click()
    self.driver.find_element(By.NAME, "city").send_keys("Town")
    self.driver.find_element(By.NAME, "state").click()
    self.driver.find_element(By.NAME, "state").send_keys("Ontario")
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(9) > td:nth-child(1)").click()
    self.driver.find_element(By.NAME, "postalCode").click()
    self.driver.find_element(By.NAME, "postalCode").send_keys("O2I 0J8")
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(9) > td:nth-child(1)").click()
    self.driver.find_element(By.NAME, "country").click()
    dropdown = self.driver.find_element(By.NAME, "country")
    dropdown.find_element(By.XPATH, "//option[. = 'CANADA']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(42)").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("alex")
    self.driver.find_element(By.NAME, "password").send_keys("alex")
    self.driver.find_element(By.NAME, "confirmPassword").send_keys("alex")
    self.driver.find_element(By.NAME, "submit").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(2) > font").text == "Thank you for registering. You may now sign-in using the user name and password you've just entered."
    self.driver.find_element(By.LINK_TEXT, "sign-in").click()
    self.driver.find_element(By.NAME, "userName").click()
    self.driver.find_element(By.NAME, "userName").send_keys("alex")
    self.driver.find_element(By.NAME, "password").send_keys("alex")
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) b").click()
    self.driver.find_element(By.NAME, "submit").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "h3").text == "Login Successfully"
    self.driver.find_element(By.LINK_TEXT, "SIGN-OFF").click()
    self.driver.find_element(By.NAME, "userName").click()
    self.driver.find_element(By.NAME, "userName").send_keys("tutorial")
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("tutorial")
    self.driver.find_element(By.NAME, "submit").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "h3").text == "Login Successfully"

  def test_Tutorial(self):
    self.driver.get("https://demo.guru99.com/test/newtours/")
    self.driver.set_window_size(860, 912)
    self.driver.find_element(By.NAME, "userName").click()
    self.driver.find_element(By.NAME, "userName").send_keys("tutorial")
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("tutorial")
    self.driver.find_element(By.NAME, "submit").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "h3").text == "Login Successfully"