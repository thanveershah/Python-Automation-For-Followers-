from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/")
        time.sleep(6)
        username = bot.find_element_by_name("username")
        password = bot.find_element_by_name("password")
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        bot.find_element_by_class_name("HoLwm").click()
        time.sleep(3)
        bot.get("https://www.instagram.com/explore/people/suggested/")
        time.sleep(3)
        for i in range(1, 3):
            tweets = bot.find_elements_by_class_name('ZUqME')
            links = [elem.find_element_by_class_name(
                'L3NKy') for elem in tweets]
            for link in links:
                link.click()
                time.sleep(2)


test = TwitterBot("xxxxx", "xxxxxxx")
test.login()
