from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

code = input("input code : ")

driver = webdriver.Chrome()

driver.get("https://izone.sunway.edu.my/login")

studentId = "test"
password = "pass"

idBox=driver.find_elements(By.XPATH, "//input[@id='student_uid']")
idBox[0].send_keys(studentId)

passwordBox = driver.find_elements(By.XPATH, "//input[@id='password']")
passwordBox[0].send_keys(password)


submit =driver.find_element(By.ID, "submit")
submit.click()

iCheckInBox = driver.find_element(By.XPATH,"//a[@id='iCheckInUrl']")
iCheckInBox.click()

codeBox = driver.find_elements(By.XPATH, "//input[@id='checkin_code']")
codeBox[0].send_keys(code)

submitCode =  driver.find_element(By.XPATH,"//a[@id='iCheckin']")
submitCode.click()

input("wait")