#Cisco Networking Academy'nin sistemine otomatik giriş yapacağız.
from tkinter import *
from PIL import ImageTk, Image
from selenium import webdriver
import kullanici
import time
import selenium.webdriver.support.ui as ui


browser = webdriver.Firefox()
wait = ui.WebDriverWait(browser, 10)

browser.get("https://www.netacad.com")

time.sleep(3)

login1 = browser.find_element_by_xpath("/html/body/header/div/div[5]/nav/div[1]/section/ul/li/a")
login1.click()
login2 = browser.find_element_by_xpath("/html/body/header/div/div[5]/nav/div[1]/section/ul/li/ul/li[1]/a")
login2.click()

time.sleep(2)

username = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/form/div/div/div[3]/div/div[2]/div/input[1]")
username.send_keys(kullanici.username)

nextbuton = browser.find_element_by_xpath("//*[@id='btn']")
nextbuton.click()
time.sleep(2)
wait.until( lambda browser: browser.find_element_by_xpath('//*[@id="password"]'))  # parolayı görmesi için geerekli kod
parola = browser.find_element_by_xpath('//*[@id="password"]')
parola.send_keys(kullanici.password)
time.sleep(2)

login3 = browser.find_element_by_xpath("//*[@id='kc-login']")
login3.click()
time.sleep(2)

wait.until(lambda browser: browser.find_element_by_xpath("/html/body/main/div/div/div[3]/section/div/div[2]/div/div[1]/div[3]/div[2]/div/div/div[3]/div[2]/ul/li[1]/a/span"))  # parolayı görmesi için geerekli kod
detay = browser.find_element_by_xpath("/html/body/main/div/div/div[3]/section/div/div[2]/div/div[1]/div[3]/div[2]/div/div/div[3]/div[2]/ul/li[1]/a/span")
detay.click()

time.sleep(2)


sinif = browser.find_elements_by_css_selector(".netacad_class_instance_title")

for metin in sinif:
    a = "HOŞÇA KALIN  " + metin.text
    print(a)

time.sleep(2)

browser.close()



