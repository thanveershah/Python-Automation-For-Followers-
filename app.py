
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import openpyxl


wb = openpyxl.Workbook()

sheet = wb.active


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


test = TwitterBot("dapperman019", "sanooja10")
test.login()
test.startAction()


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# class TwitterBot:
#     def __init__(self):
#         self.username = ["Endro@bma-merdeka.com","bali@esmirada.com"]
#         self.bot = webdriver.Firefox()

#     def login(self):
#         bot = self.bot
#         bot.get("https://skmei.in/shop/skmei-1486-original-drum-wrist-watch-men/")
#         time.sleep(3)
#         for x in self.username:
#             username = bot.find_element_by_name("alert_email")
#             username.clear()
#             username.send_keys(x)
#             time.sleep(3)
#             bot.find_element_by_name("alert_button").click()
#             time.sleep(3)
#             bot.refresh()
#             time.sleep(3)

# test = TwitterBot()
# test.login()


# # distance = 50
# # pyautogui.FAILSAFE = True
# distance = 100

# while distance > 0:
#     time.sleep(2)
#     pyautogui.keyDown('ctrl')
#     pyautogui.keyDown('shift')
#     pyautogui.keyDown('s')
#     time.sleep(2)
#     pyautogui.click(pyautogui.locateCenterOnScreen('Capture.png'))
#     time.sleep(1)
#     pyautogui.typewrite("a")
#     time.sleep(1)
#     pyautogui.press("enter")
#     time.sleep(1)
#     pyautogui.click(pyautogui.locateCenterOnScreen('save.png'))
#     time.sleep(2)
#     pyautogui.click(pyautogui.locateCenterOnScreen('Capture2.png'))
#     time.sleep(2)
#     pyautogui.click(pyautogui.locateCenterOnScreen('file.png'))
#     time.sleep(2)
#     pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down'])
#     time.sleep(1)
#     pyautogui.press("enter")
#     time.sleep(1)

# time.sleep(3)
# pyautogui.click()
# distance = 200
# while distance > 0:
#     pyautogui.dragRel(distance, 0, duration=0.5)
#     distance -= 5
#     pyautogui.dragRel(0, distance, duration=0.5)
#     pyautogui.dragRel(-distance, 0, duration=0.5)
#     distance -= 5
#     pyautogui.dragRel(0, -distance, duration=0.5)
