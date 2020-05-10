from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np
import pandas as pd

path = 'Accounts/1.Jenny.csv'
URLs = pd.read_csv(path, encoding='iso-8859-1')
# encoding='iso-8859-1'
# Credentials = pd.read_csv('credentials.csv')
URLs.head()
# Credentials.head()

e_mail = URLs['email'][0]
password = URLs['password'][0]
message = URLs['message'][0]

print(e_mail)
print(password)
print(message)

class Linkedin:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.bot=webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        bot=self.bot
        bot.get("https://www.linkedin.com/uas/login")
        time.sleep(1.5)
        email=bot.find_element_by_id("username")
        email.send_keys(self.username)
        password=bot.find_element_by_id("password")
        password.send_keys(self.password)
        time.sleep(1.5)
        password.send_keys(Keys.RETURN)

    def send_request(self, URL):
        bot = self.bot
        # time.sleep(1)
        bot.get(URL)
        # time.sleep(1)

        try:
            try:
                connect_button = bot.find_element_by_xpath('/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/span[1]/div/button')
            except:
                connect_button = bot.find_element_by_xpath('/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/span[1]/div/button')        
            # /html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/span[1]/div/button
            # /html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/span[1]/div/button
            # /html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/span[1]/div/button
            connect_button.click()

        except:
            try:
                more_button = bot.find_element_by_xpath('/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div/div/button')
            except:
                more_button = bot.find_element_by_xpath('/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div/div/button')            
            more_button.click()
            # /html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div/div/button
            try:
                send_msg_button = bot.find_element_by_xpath('/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div/div/div/div/ul/li[4]/div/div')
            except:
                send_msg_button = bot.find_element_by_xpath('/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div/div/div/div/ul/li[4]/div/div')
            send_msg_button.click()
        
        try:
            direct_message_box = bot.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[1]/textarea')
            # /html/body/div[4]/div/div/div[2]/div[1]/textarea
            direct_message_box.send_keys(message)
            send_invitation_button = bot.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
            send_invitation_button.click()
            return 1

        except:
            add_note_button = bot.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]')
            add_note_button.click()
            message_box = bot.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/textarea')
            message_box.send_keys(message)
            done_button = bot.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
            done_button.click()
            return 1

        # time.sleep(1)

count = URLs['urls'].count()
load = Linkedin(e_mail, password)
load.login()

for i in range (0,count):
    if(URLs['sent'][i] == 0):
        try:
            x = load.send_request(URLs['urls'][i])
            if(x == 1):
                URLs['sent'][i] = 1
        except:
            continue
    else:
        continue

print("END OF LOOP")

URLs.to_csv(path, index=False)