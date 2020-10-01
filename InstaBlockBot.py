from selenium import webdriver
from time import sleep

class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.instagram.com/')
        
        sleep(2)
        
        btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
        btn.click()

        sleep(2)
        
        username = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
        print('Enter Your username : ')
        un = input()
        username.send_keys(un)

        sleep(1)

        pwd = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
        print('Enter Your Password : ')
        password = input()
        pwd.send_keys(password)

        sleep(1)

        loginbtn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
        loginbtn.click()

        sleep(2)
        
        notnowbtn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        notnowbtn.click()

        sleep(2)

        
    def block(self):
        search = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        print('Enter Target Username : ' )
        target = input()
        search.send_keys(target)

        sleep(2)

        blockelement = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a/div')
        blockelement.click()
        sleep(2)

        options = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button/span')
        options.click()

        block = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/button[2]')
        block.click()

        confirm = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/button[1]')
        confirm.click()

        sleep(2)

        dismiss = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/button')
        dismiss.click()

        sleep(2)

        home = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div')
        home.click()

bot = Bot()
bot.login()
bot.block()
