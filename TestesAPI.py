from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://serverest.dev/#/Usu%C3%A1rios/post_usuarios')
sleep(1)
driver.find_element_by_xpath('/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[2]/div/div/div/span[2]/div/div[2]/div/div[2]/div[1]/div[2]/button').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="operations-Usuários-post_usuarios"]/div[2]/div/div[2]/div[2]/div/table/tbody/tr/td[2]/div/div/div/textarea').clear()
driver.find_element_by_xpath('//*[@id="operations-Usuários-post_usuarios"]/div[2]/div/div[2]/div[2]/div/table/tbody/tr/td[2]/div/div/div/textarea').send_keys("{ \"nome\": \"Ayrton\", \"email\": \"olhugol@qa.com.br\", \"password\": \"teste\", \"administrador\": \"true\"}")
driver.find_element_by_xpath('//*[@id="operations-Usuários-post_usuarios"]/div[2]/div/div[3]/button').click()
sleep(2)
idUser = driver.find_element_by_xpath('/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[2]/div/div/div/span[2]/div/div[2]/div/div[4]/div[2]/div/div/table/tbody/tr/td[2]/div[1]/div/pre/code/span[10]')
idUserText = idUser.text
driver.find_element_by_xpath('//*[@id="operations-Usuários-get_usuarios"]/div').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="operations-Usuários-get_usuarios"]/div[2]/div/div[1]/div[1]/div[2]/button').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="operations-Usuários-get_usuarios"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/input').clear()
driver.find_element_by_xpath('//*[@id="operations-Usuários-get_usuarios"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/input').send_keys(idUserText)
driver.find_element_by_xpath('//*[@id="operations-Usuários-get_usuarios"]/div[2]/div/div[2]/button').click()