from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:
    def __init__(self):
        self.bot = webdriver.Firefox()

    def startProcess(self):
        bot = self.bot
        bot.get("http://localhost:3001/admin")
        time.sleep(2)
        for x in bot.find_elements_by_class_name("form-control"):
            x.clear()
            x.send_keys("sss")


test = TwitterBot()
test.startProcess()
