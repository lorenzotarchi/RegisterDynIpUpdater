import time
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service 


def say_my_name():
  path = "chromedriver.exe"#Pathchromedriver
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_experimental_option("useAutomationExtension", False)
  chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
  driver = webdriver.Chrome(executable_path=path, options=chrome_options)
  url = 'https://controlpanel.register.it/welcome.html'
  driver.get(url)
  email = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.NAME,"userName"))) 
  password = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.NAME,"password")))
    

  email.send_keys('mail@gmail.com')#Email
  password.send_keys('123456789')#Password
  time.sleep(3)
  #accesso
  WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll']"))).click()
  WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='formLogin']/div[3]/button"))).click()
  url = 'https://controlpanel.register.it/domains/dnsAdvanced.html'
  driver.get(url)
  time.sleep(3)
  
  WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "dominio.it"))).click()#dominio
  WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='webapp_domain']/a"))).click()
  WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='dom_dns']/a"))).click()
  time.sleep(3)
  WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='DNS']/div[4]/div/table/tbody/tr[1]/td[4]/div/a"))).click()
  WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='modalDialog']/div/div[5]/div[2]/div/div/a[1]"))).click()
  time.sleep(60)
  WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='DNS']/div[4]/div/ul[1]/li/a[1]"))).click()
  
  
  
  #Dobbiamo inserire nuovo ip ma ancora non lo abbiamo sotto forma di variabile quindi : 
  url = 'http://ifconfig.me'
  response = requests.get(url)
  ip_address = response.text
  list_ = ip_address.split('.')
  print(list_[0])
  print(list_[1])
  print(list_[2])
  print(list_[3])

  #adesso lo andiamo ad inserire nei giusti campi

  primo = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='iip1']")))
  primo.send_keys(list_[0])

  secondo = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='iip2']")))
  secondo.send_keys(list_[1])

  terzo = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='iip3']")))
  terzo.send_keys(list_[2])

  quarto = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='iip4']")))
  quarto.send_keys(list_[3])
  #Procedi
  WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='modalDialog']/div/div[1]/div[2]/div/div/a[1]"))).click()
  
  print('Andato a buon FINE')
  time.sleep(15)
  
url = 'http://ifconfig.me'
response = requests.get(url)
ip_address = response.text

text_file = open('ifconfig.txt','r')
ciccio = text_file.read()
print (ciccio)
print(ip_address)

if ip_address != ciccio:
  print("Diverso")
  say_my_name()
  text_file = open('ifconfig.txt','w')
  text_file.write(ip_address)
  text_file.close()
else:
  print("Ip uguale, non cambiato")
  


