from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://www.trivago.com.br/')
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="querytext"]').send_keys("Manaus")
sleep(2)
driver.find_element_by_xpath('//*[@id="js-homepage-title"]/h1/span').click()
driver.find_element_by_xpath('//*[@id="js-fullscreen-hero"]/div[1]/div[2]/form/div/button[2]').click()
sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/main/div[1]/div[1]/div[3]/div/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/select').click()
driver.find_element_by_xpath('/html/body/div[2]/main/div[1]/div[1]/div[3]/div/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/select/option[2]').click()
sleep(3)
NameFirst = driver.find_element_by_xpath('/html/body/div[2]/main/div[1]/div[1]/div[3]/div/div[1]/div[2]/div[1]/div/section/ol/li[1]/div/article/div[1]/div[2]/div/div/h3/span')
NameFirstText = NameFirst.text
print(NameFirstText)
Avaliacao = driver.find_element_by_xpath('//*[@id="1476461"]/div/article/div[1]/div[2]/div/div/button/span[1]/span[2]/strong')
AvaliacaoText = Avaliacao.text
print(AvaliacaoText)
Valor = driver.find_element_by_xpath('//*[@id="1476461"]/div/article/div[1]/div[2]/section/div[2]/article/div/button/span/span[1]')
ValorText = Valor.text
print(ValorText)