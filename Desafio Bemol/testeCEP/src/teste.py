from selenium import webdriver
import time

chrome = webdriver.Chrome()                                   # start browser
chrome.get('http://www.buscacep.correios.com.br/')
chrome.maximize_window()

chrome.find_element_by_partial_link_text(
    "Busca CEP").click()  # Choose search option

inputCEP = chrome.find_element_by_id("endereco")
inputCEP.send_keys('69005-040')  # Insert data
time.sleep(3)
chrome.find_element_by_id("btn_pesquisar").click()

time.sleep(5)

chrome.find_element_by_id("btn_voltar").click()
inputCEP = chrome.find_element_by_id("endereco")  # Choose search option
inputCEP.send_keys('Lojas Bemol')  # Insert data
time.sleep(3)
chrome.find_element_by_id("btn_pesquisar").click()
time.sleep(5)
chrome.close()
