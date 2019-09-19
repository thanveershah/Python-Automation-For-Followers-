
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import openpyxl


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        username = bot.find_element_by_name("username")
        password = bot.find_element_by_name("password")
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)
        bot.find_element_by_class_name("HoLwm").click()

    def startAction(self):
        bot = self.bot
        time.sleep(3)
        bot.get("https://www.instagram.com/volume.qa/")
        time.sleep(4)
        newLink = bot.find_element_by_tag_name("a")
        newLink.click()
        time.sleep(3)
        for i in range(1, 500):
            tweets = bot.find_elements_by_class_name('wo9IH')
            time.sleep(2)
            links = [elem for elem in tweets]
            for link in links:
                followButton = link.find_element_by_class_name("L3NKy")
                if followButton.text == "Follow":
                    followButton.click()
                    peopleName = link.find_element_by_class_name("_0imsa")
                    print(peopleName.text)
                    time.sleep(50)
                else:
                    time.sleep(2)


test = TwitterBot("username", "password")
test.login()
test.startAction()
