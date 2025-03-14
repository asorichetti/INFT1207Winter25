# Name: Alex Sorichetti
# Assignment: Lab 4
# Description: A test file which tests a live website that calculates a persons BMI
# As tested with various inputs.

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

class TestDefaultSuite():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_femaleIsValid(self):
    self.driver.get("https://www.calculator.net/body-fat-calculator.html")
    self.driver.set_window_size(813, 912)
    self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(2) > .rbmark").click()
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").clear()
    self.driver.find_element(By.NAME, "cage").send_keys("28")
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").clear()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("99")
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.ID, "cheightmeter").clear()
    self.driver.find_element(By.ID, "cheightmeter").send_keys("190")
    self.driver.find_element(By.ID, "cneckmeter").click()
    self.driver.find_element(By.ID, "cneckmeter").clear()
    self.driver.find_element(By.ID, "cneckmeter").send_keys("47")
    self.driver.find_element(By.ID, "cwaistmeter").clear()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("99")
    self.driver.find_element(By.ID, "chipmeter").clear()
    self.driver.find_element(By.ID, "chipmeter").send_keys("90")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font > b").text == "Body Fat: 23.2%"
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").send_keys("99")
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("55")
    self.driver.find_element(By.ID, "cheightmeter").send_keys("176")
    self.driver.find_element(By.ID, "cneckmeter").send_keys("40")
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("88")
    self.driver.find_element(By.ID, "chipmeter").send_keys("68")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font > b").text == "Body Fat: 12.9%"
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").clear()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("10")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font > b").text == "Body Fat: 12.9%"
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
    self.driver.find_element(By.NAME, "cage").send_keys("99")
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("1")
    self.driver.find_element(By.ID, "chipmeter").click()
    self.driver.find_element(By.ID, "chipmeter").send_keys("60")
    self.driver.find_element(By.ID, "cwaistmeter").click()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("70")
    self.driver.find_element(By.ID, "cneckmeter").click()
    self.driver.find_element(By.ID, "cneckmeter").send_keys("30")
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.ID, "cheightmeter").send_keys("160")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font > b").text == "Body Fat: 7.1%"
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").send_keys("1")
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("33")
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.ID, "cheightmeter").send_keys("44")
    self.driver.find_element(By.ID, "cneckmeter").click()
    self.driver.find_element(By.ID, "cneckmeter").send_keys("18")
    self.driver.find_element(By.ID, "cwaistmeter").click()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("23")
    self.driver.find_element(By.ID, "chipmeter").click()
    self.driver.find_element(By.ID, "chipmeter").send_keys("22")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font > b").text == "Body Fat: 0.0%"
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").send_keys("22")
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("176")
    self.driver.find_element(By.ID, "cheightmeter").send_keys("54")
    self.driver.find_element(By.ID, "cneckmeter").send_keys("38")
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("99")
    self.driver.find_element(By.ID, "chipmeter").send_keys("96")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font > b").text == "Body Fat: 94.0%"
    self.driver.close()
  
  def test_femaleIsInvalid(self):
    self.driver.get("https://www.calculator.net/body-fat-calculator.html")
    self.driver.set_window_size(813, 912)
    self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(2) > .rbmark").click()
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").clear()
    self.driver.find_element(By.NAME, "cage").send_keys(" ")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Please provide a positive age."
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").clear()
    self.driver.find_element(By.NAME, "cage").send_keys("-25")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Please provide a positive age."
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").clear()
    self.driver.find_element(By.NAME, "cage").send_keys("p")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Please provide a positive age."
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").clear()
    self.driver.find_element(By.NAME, "cage").send_keys("25")
    self.driver.find_element(By.NAME, "cweightkgs").clear()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys(" ")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Please provide a positive weight."
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").clear()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("-110")
    self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(4) td").click()
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Please provide a positive weight."
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").clear()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("p")
    self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(4) td").click()
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Please provide a positive weight."
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").clear()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("110")
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.ID, "cheightmeter").clear()
    self.driver.find_element(By.ID, "cheightmeter").send_keys(" ")
    element = self.driver.find_element(By.NAME, "x")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Height need to be positive."
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.ID, "cheightmeter").clear()
    self.driver.find_element(By.ID, "cheightmeter").send_keys("p")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Height need to be positive."
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.ID, "cheightmeter").clear()
    self.driver.find_element(By.ID, "cheightmeter").send_keys("190")
    self.driver.find_element(By.ID, "cneckmeter").click()
    self.driver.find_element(By.ID, "cneckmeter").clear()
    self.driver.find_element(By.ID, "cneckmeter").send_keys(" ")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Neck need to be numeric."
    self.driver.find_element(By.ID, "cneckmeter").click()
    self.driver.find_element(By.ID, "cneckmeter").clear()
    self.driver.find_element(By.ID, "cneckmeter").send_keys("p")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Neck need to be numeric."
    self.driver.find_element(By.ID, "cneckmeter").click()
    self.driver.find_element(By.ID, "cneckmeter").clear()
    self.driver.find_element(By.ID, "cneckmeter").send_keys("-10")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Neck need to be numeric."
    self.driver.find_element(By.ID, "cneckmeter").click()
    self.driver.find_element(By.ID, "cneckmeter").clear()
    self.driver.find_element(By.ID, "cneckmeter").send_keys("30")
    self.driver.find_element(By.ID, "cwaistmeter").click()
    self.driver.find_element(By.ID, "cwaistmeter").clear()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys(" ")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Waist need to be numeric."
    self.driver.find_element(By.ID, "cwaistmeter").click()
    self.driver.find_element(By.ID, "cwaistmeter").clear()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("p")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Waist need to be numeric."
    self.driver.find_element(By.ID, "cwaistmeter").click()
    self.driver.find_element(By.ID, "cwaistmeter").clear()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("-10")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Waist need to be numeric."
    self.driver.find_element(By.ID, "cwaistmeter").click()
    self.driver.find_element(By.ID, "cwaistmeter").clear()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("93")
    self.driver.find_element(By.ID, "chipmeter").click()
    self.driver.find_element(By.ID, "chipmeter").clear()
    self.driver.find_element(By.ID, "chipmeter").send_keys(" ")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Hip need to be numeric."
    self.driver.find_element(By.ID, "chipmeter").click()
    self.driver.find_element(By.ID, "chipmeter").clear()
    self.driver.find_element(By.ID, "chipmeter").send_keys("p")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Hip need to be numeric."
    self.driver.find_element(By.ID, "chipmeter").click()
    self.driver.find_element(By.ID, "chipmeter").clear()
    self.driver.find_element(By.ID, "chipmeter").send_keys("-100")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Hip need to be numeric."
    self.driver.find_element(By.ID, "chipmeter").click()
    self.driver.find_element(By.ID, "chipmeter").clear()
    self.driver.find_element(By.ID, "chipmeter").send_keys("99")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font > b").text == "Body Fat: 32.5%"
    self.driver.close()
  
  def test_femaleIsSymbols(self):
    self.driver.get("https://www.calculator.net/body-fat-calculator.html")
    self.driver.set_window_size(765, 912)
    self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(2) > .rbmark").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").send_keys("-")
    self.driver.find_element(By.CSS_SELECTOR, "#metricheightweight tr:nth-child(2) > td:nth-child(1)").click()
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys(")")
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.ID, "cheightmeter").send_keys("+")
    self.driver.find_element(By.ID, "cneckmeter").click()
    self.driver.find_element(By.ID, "cneckmeter").send_keys("@")
    self.driver.find_element(By.ID, "cwaistmeter").click()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("<<")
    self.driver.find_element(By.ID, "chipmeter").click()
    self.driver.find_element(By.ID, "chipmeter").send_keys(">>")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > font").text == "Please provide a positive age."
    assert self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > font").text == "Please provide a positive weight."
    assert self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > font").text == "Height need to be positive."
    assert self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) > font").text == "Neck need to be numeric."
    assert self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(5) > font").text == "Waist need to be numeric."
    assert self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6) > font").text == "Hip need to be numeric."
    self.driver.close()
  
  def test_maleisInvalid(self):
    self.driver.get("https://www.calculator.net/body-fat-calculator.html")
    self.driver.set_window_size(765, 912)
    self.driver.find_element(By.CSS_SELECTOR, "tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").clear()
    self.driver.find_element(By.NAME, "cage").send_keys(" ")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Please provide a positive age."
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").clear()
    self.driver.find_element(By.NAME, "cage").send_keys("p")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Please provide a positive age."
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").clear()
    self.driver.find_element(By.NAME, "cage").send_keys("-10")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Please provide a positive age."
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").clear()
    self.driver.find_element(By.NAME, "cage").send_keys("25")
    self.driver.find_element(By.CSS_SELECTOR, "#metricheightweight tr:nth-child(1) > td:nth-child(1)").click()
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").clear()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys(" ")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Please provide a positive weight."
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").clear()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("-9")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Please provide a positive weight."
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").clear()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("p")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Please provide a positive weight."
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").clear()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("160")
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.ID, "cheightmeter").clear()
    self.driver.find_element(By.ID, "cheightmeter").send_keys(" ")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Height need to be positive."
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.ID, "cheightmeter").clear()
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.ID, "cheightmeter").send_keys("p")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Height need to be positive."
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.ID, "cheightmeter").clear()
    self.driver.find_element(By.ID, "cheightmeter").send_keys("-9")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Height need to be positive."
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.ID, "cheightmeter").clear()
    self.driver.find_element(By.ID, "cheightmeter").send_keys("178")
    self.driver.find_element(By.ID, "cneckmeter").click()
    self.driver.find_element(By.ID, "cneckmeter").clear()
    self.driver.find_element(By.ID, "cneckmeter").send_keys(" ")
    element = self.driver.find_element(By.NAME, "x")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Neck need to be numeric."
    self.driver.find_element(By.ID, "cneckmeter").click()
    self.driver.find_element(By.ID, "cneckmeter").clear()
    self.driver.find_element(By.ID, "cneckmeter").send_keys("p")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Neck need to be numeric."
    self.driver.find_element(By.ID, "cneckmeter").click()
    self.driver.find_element(By.ID, "cneckmeter").clear()
    self.driver.find_element(By.ID, "cneckmeter").send_keys("-9")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Neck need to be numeric."
    self.driver.find_element(By.ID, "cneckmeter").click()
    self.driver.find_element(By.ID, "cneckmeter").clear()
    self.driver.find_element(By.ID, "cneckmeter").send_keys("50")
    self.driver.find_element(By.CSS_SELECTOR, "#metricheightweight tr:nth-child(4) > td:nth-child(1)").click()
    self.driver.find_element(By.ID, "cwaistmeter").click()
    self.driver.find_element(By.ID, "cwaistmeter").clear()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys(" ")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Waist need to be numeric."
    self.driver.find_element(By.ID, "cwaistmeter").click()
    self.driver.find_element(By.ID, "cwaistmeter").clear()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("p")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Waist need to be numeric."
    self.driver.find_element(By.ID, "cwaistmeter").click()
    self.driver.find_element(By.ID, "cwaistmeter").clear()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("-9")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Waist need to be numeric."
    self.driver.find_element(By.ID, "cwaistmeter").click()
    self.driver.find_element(By.ID, "cwaistmeter").clear()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("90")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font > b").text == "Body Fat: 10.6%"
    self.driver.close()
  
  def test_maleisSymbols(self):
    self.driver.get("https://www.calculator.net/body-fat-calculator.html")
    self.driver.set_window_size(765, 912)
    self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").send_keys(")")
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("<<")
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.ID, "cheightmeter").send_keys(">>")
    self.driver.find_element(By.ID, "cneckmeter").click()
    self.driver.find_element(By.ID, "cneckmeter").send_keys("{}")
    self.driver.find_element(By.ID, "cwaistmeter").click()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("\":\":;")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > font").text == "Please provide a positive age."
    assert self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > font").text == "Please provide a positive weight."
    assert self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > font").text == "Height need to be positive."
    assert self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) > font").text == "Neck need to be numeric."
    assert self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(5) > font").text == "Waist need to be numeric."
    self.driver.close()
  
  def test_maleisValid(self):
    self.driver.get("https://www.calculator.net/body-fat-calculator.html")
    self.driver.set_window_size(813, 912)
    self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").send_keys("35")
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("110")
    self.driver.find_element(By.CSS_SELECTOR, "#metricheightweight tr:nth-child(2) > td:nth-child(1)").click()
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.ID, "cheightmeter").send_keys("188")
    self.driver.find_element(By.ID, "cneckmeter").click()
    self.driver.find_element(By.ID, "cneckmeter").send_keys("65")
    self.driver.find_element(By.CSS_SELECTOR, "#metricheightweight tr:nth-child(4) > td:nth-child(2)").click()
    self.driver.find_element(By.ID, "cwaistmeter").click()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("98")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font > b").text == "Body Fat: 2.4%"
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").send_keys("1")
    self.driver.find_element(By.CSS_SELECTOR, "#metricheightweight tr:nth-child(3) > td:nth-child(1)").click()
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("30")
    self.driver.find_element(By.CSS_SELECTOR, "#metricheightweight tr:nth-child(2) > td:nth-child(1)").click()
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.ID, "cheightmeter").send_keys("60")
    self.driver.find_element(By.CSS_SELECTOR, "#metricheightweight tr:nth-child(3) > td:nth-child(1)").click()
    self.driver.find_element(By.ID, "cneckmeter").click()
    self.driver.find_element(By.ID, "cneckmeter").send_keys("20")
    self.driver.find_element(By.ID, "cwaistmeter").click()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("40")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font > b").text == "Body Fat: 17.4%"
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").send_keys("99")
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("190")
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.ID, "cheightmeter").send_keys("180")
    self.driver.find_element(By.CSS_SELECTOR, ".panel2").click()
    self.driver.find_element(By.ID, "cneckmeter").click()
    self.driver.find_element(By.ID, "cneckmeter").send_keys("60")
    self.driver.find_element(By.ID, "cwaistmeter").click()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("90")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font > b").text == "Body Fat: 0.3%"
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").clear()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("400")
    self.driver.find_element(By.ID, "cwaistmeter").click()
    self.driver.find_element(By.ID, "cwaistmeter").clear()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("150")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font > b").text == "Body Fat: 41.0%"
    self.driver.close()