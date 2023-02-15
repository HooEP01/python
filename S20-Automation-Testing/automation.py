from selenium import webdriver
from selenium.webdriver.chrome.service import Service
     
service = Service(executable_path='./chromedriver')

chrome_browser = webdriver.Chrome(service=service)

chrome_browser.maximize_window
chrome_browser.get('https://demo.seleniumeasy.com/')
print('Selenium Easy - Best Demo website to practice Selenium Webdriver Online' in chrome_browser.title)

button_text = chrome_browser.find_element_by_class_name('btn-default')
print(button_text.getAttribute('innerHTML'))