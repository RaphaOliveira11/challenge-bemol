from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://www.correios.com.br')
driver.maximize_window()
sleep(2)
driver.find_element_by_xpath('//*[@id="btnCookie"]').click()
driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div/div/article/div[2]/div/div[2]/form/div[2]/input').send_keys("69005040")
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/form/div[2]/button/i').click()