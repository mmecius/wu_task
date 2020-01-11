from selenium import webdriver
from time import sleep  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

username_str = "Admin"
password_str = "admin123"

#Open website
browser = webdriver.Chrome()
browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials")

#Logins to website
user_login = browser.find_element_by_id("txtUsername").send_keys(username_str)
password_login = browser.find_element_by_id("txtPassword").send_keys(password_str)
sign_in = browser.find_element_by_id("btnLogin")
sign_in.click()

#Navigates to assign leave
assign_leave_menu = browser.find_element_by_link_text("Leave").click()
assign_leave_item = browser.find_element_by_link_text("Assign Leave").click()

#Filling forms
browser.find_element(By.ID,"assignleave_txtEmployee_empName").send_keys("Jasmine Morgan")
browser.find_element(By.ID,"assignleave_txtLeaveType").send_keys("Vocation US")
browser.find_element(By.ID,"assignleave_txtFromDate").send_keys(Keys.BACKSPACE*10)
browser.find_element(By.ID,"assignleave_txtFromDate").send_keys("2020-03-23")
browser.find_element(By.ID,"assignleave_txtToDate").send_keys(Keys.BACKSPACE*10)
browser.find_element(By.ID,"assignleave_txtToDate").send_keys("2020-03-30")
browser.find_element(By.ID,"assignleave_txtComment").send_keys("-Not required-")

#Submit
assign_Btn = browser.find_element(By.ID,"assignBtn").click()

#Assign leave
assign_Btn = browser.find_element(By.ID,"welcome")
assign_Btn.click()

#Logout from system
#btn_leave_site = browser.find_element_by_xpath("//div@welcome-menu/ul/li[1]")
#btn_leave_site.click()

#Close browser
browser.close()