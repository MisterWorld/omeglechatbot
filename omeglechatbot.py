from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException
import time



first = input("What is your first message?")
second = input("What is your second message?")

driver = webdriver.Firefox()
driver.get('https://www.omegle.com')
textbutton = driver.find_element_by_id('textbtn')
textbutton.click()



def omegleChat(firstMsg,secondMsg):
    i = 0
    while i < 200:
        i += 1
        try:

            chatbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "chatmsg")))
            chatbox.click()
            chatbox.send_keys(firstMsg)

            sendBtn = driver.find_element_by_class_name('sendbtn')
            sendBtn.click()
            time.sleep(2.5)

            chatbox.click()
            chatbox.send_keys(secondMsg)
            sendBtn.click()
            time.sleep(5)

            submitBtn = driver.find_element_by_class_name('disconnectbtn')
            submitBtn.click()
            submitBtn.click()
            submitBtn.click()

        except (StaleElementReferenceException, ElementNotInteractableException):
            submitBtn = driver.find_element_by_class_name('disconnectbtn')
            submitBtn.click()

omegleChat(firstMsg = first, secondMsg = second)
