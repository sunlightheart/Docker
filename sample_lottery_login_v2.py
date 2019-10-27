from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import datetime

# ファイル出力パス指定
out_path = r"C:\Users\HP\Desktop"

# 現在の日付を取得
now_date = datetime.datetime.now()
now_date_str = now_date.strftime("%y%m%d%S%f")
out_path = out_path + r"/IT1_" + now_date_str + r".png"

# ドライバ読み込み
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("https://cp.mizuhobank.co.jp/lucky_p_secure/p02001")
driver.find_element_by_id("memno").click()
driver.find_element_by_id("memno").clear()
driver.find_element_by_id("memno").send_keys("XXXXXXXX")
driver.find_element_by_id("ansyono").clear()
driver.find_element_by_id("ansyono").send_keys("XXXXXXX")
driver.find_element_by_id("login").click()
driver.find_element_by_id("lbl_rdLotoMini_3").click()
driver.find_element_by_id("doInput").click()
driver.find_element_by_id("number1").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='選択できる数字は5個までです。'])[1]/following::span[3]").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='選択できる数字は5個までです。'])[1]/following::span[7]").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='選択できる数字は5個までです。'])[1]/following::span[11]").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='選択できる数字は5個までです。'])[1]/following::span[15]").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='選択できる数字は5個までです。'])[1]/following::span[19]").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='選択できる数字は5個までです。'])[1]/following::input[34]").click()
driver.find_element_by_name("kuchisu").click()
Select(driver.find_element_by_name("kuchisu")).select_by_visible_text("3")
driver.find_element_by_name("kuchisu").click()
driver.find_element_by_name("kezokuKaisu").click()
Select(driver.find_element_by_name("kezokuKaisu")).select_by_visible_text("3")
driver.find_element_by_name("kezokuKaisu").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='数字選択式宝くじ 申込数字・口数・回数の入力'])[1]/following::div[1]").click()
driver.find_element_by_id("next").click()
sfile = driver.get_screenshot_as_file(out_path)

driver.refresh()
#driver.implicitly_wait(1)
#sfile = driver.save_screenshot(out_path)
#sfile = driver.get_screenshot_as_file(out_path)

driver.back()
#driver.implicitly_wait(1)
#sfile = driver.save_screenshot(out_path)
#sfile = driver.get_screenshot_as_file(out_path)

driver.close()
