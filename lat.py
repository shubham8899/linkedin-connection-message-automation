from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

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

    def send_request(self):
        bot = self.bot
        bot.get('https://linkedin.com/in/yuri-deary-00b6055a/')
        time.sleep(1)
        # connect_button = bot.find_element_by_xpath('/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/span[1]/div')
        # connect_button.click()
        # add_note_button = bot.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]')
        # add_note_button.click()
        # message_box = bot.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/textarea')
        # message_box.send_keys("Greetings from Moyyn! We have several open positions for Java Developers (Junior/Senior/Lead) for our partners in Berlin. Your profile seems very promising. If you are interested for new opportunities, please have a look at moyyn.com/jobs-germany and submit your application.\nQuarantined regards.")
        # done_button = bot.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        # done_button.click()
        try:
            more_button = bot.find_element_by_xpath('/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div/div/button')
        except:
            more_button = bot.find_element_by_xpath('/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div/div/button')            
        more_button.click()
        # /html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div/div/button
        send_msg_button = bot.find_element_by_xpath('/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div/div/div/div/ul/li[4]/div')
        send_msg_button.click()


# URLs = pd.read_csv('urls.csv')

load=Linkedin("arvi@moyyn.com","hellomoyyn123")
load.login()
load.send_request()

#/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/span[1]/div

