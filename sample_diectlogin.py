from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://web.ib.mizuhobank.co.jp/servlet/LOGBNK0000000B.do")
sfile = driver.get_screenshot_as_file("sample1.png")

driver.find_element_by_id("txbCustNo").send_keys("XXXXXXXXXX")
sfile = driver.get_screenshot_as_file("sample2.png")
driver.find_element_by_id("txbCustNo").send_keys(Keys.ENTER)

driver.find_element_by_id("PASSWD_LoginPwdInput").send_keys("XXXXXXXXXX")
sfile = driver.get_screenshot_as_file("sample3.png")
driver.find_element_by_id("PASSWD_LoginPwdInput").send_keys(Keys.ENTER)

sfile = driver.get_screenshot_as_file("sample4.png")

driver.find_element_by_id("btnMenuMvRight").click()
sfile = driver.get_screenshot_as_file("sample5.png")

driver.find_element_by_id("btnMenuMvLeft").click()
sfile = driver.get_screenshot_as_file("sample6.png")

driver.find_element_by_id("btnRed").click()
sfile = driver.get_screenshot_as_file("sample7.png")

driver.find_element_by_id("btnPurple").click()
sfile = driver.get_screenshot_as_file("sample8.png")

driver.quit()
