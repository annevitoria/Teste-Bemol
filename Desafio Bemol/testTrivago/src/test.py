import time
from selenium import webdriver
from pynput.keyboard import Key, Controller

chrome = webdriver.Chrome()
chrome.get('https://www.trivago.com.br/')
chrome.maximize_window()


inputCEP = chrome.find_element_by_id("querytext")
inputCEP.send_keys('Manaus')
time.sleep(5)

chrome.find_element_by_xpath(
    "/html/body/div[2]/div[2]/div[4]/div/div[1]/form/div/button[2]").click()

time.sleep(3)

chrome.find_element_by_xpath(
    "/html/body/div[2]/main/div[1]/div[1]/div[3]/div/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/div[1]").click()

time.sleep(3)


keyboard = Controller()
keyboard.press(Key.down)
keyboard.press(Key.enter)

time.sleep(6)

nome = chrome.find_element_by_xpath(
    "/html/body/div[2]/main/div[1]/div[1]/div[3]/div/div[1]/div[2]/div[1]/div/section/ol/li[1]/div/article/div[1]/div[2]/div/div/h3/span").text

avaliacao = chrome.find_element_by_xpath(
    "/html/body/div[2]/main/div[1]/div[1]/div[3]/div/div[1]/div[2]/div[1]/div/section/ol/li[1]/div/article/div[1]/div[2]/div/div/button/span[1]/span[2]/strong").text

nota = chrome.find_element_by_xpath(
    "/html/body/div[2]/main/div[1]/div[1]/div[3]/div/div[1]/div[2]/div[1]/div/section/ol/li[1]/div/article/div[1]/div[2]/div/div/button/span[1]/span[1]/span").text


valor = chrome.find_element_by_xpath(
    "/html/body/div[2]/main/div[1]/div[1]/div[3]/div/div[1]/div[2]/div[1]/div/section/ol/li[1]/div/article/div[1]/div[2]/section/div[1]/article/div/div[3]/div/div/div/strong").text

print("\nNome: ", nome)
print("Avaliacao: ", nota+" "+avaliacao)
print("Valor: ", valor)

chrome.close()
