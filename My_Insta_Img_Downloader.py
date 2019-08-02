__author__ = '91834'
from selenium import webdriver
import os
import requests
from bs4 import BeautifulSoup
from time import sleep
import shutil
class App:
    def __init__(self,UserName='7602061400',PassWord='pks99ing',Target='dona__das',Path='C:\\Users\\91834\\Desktop\\WebScraping'):
        self.UserName=UserName
        self.PassWord=PassWord
        self.Target=Target
        self.Main_url='https://www.instagram.com'
        self.Path=Path
        self.driver = webdriver.Chrome('C:\\Users\\91834\\Desktop\\Main\\WebScrapipng\\chromedriver')
        self.driver.get(self.Main_url)


        self.log_in()
        self.target_account()
        self.scroll_down()
        self.download()
        sleep(10)
        self.driver.close()

    def log_in(self):
        login_button=self.driver.find_element_by_xpath("//p[@class='izU2O']/a")
        login_button.click()
        sleep(2)
        user_name_input=self.driver.find_element_by_xpath("//input[@name='username']")
        user_name_input.send_keys(self.UserName)
        password_input=self.driver.find_element_by_xpath("//input[@name='password']")
        password_input.send_keys(self.PassWord)
        user_name_input.submit()
        sleep(3)
        try:
            pop_up=self.driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
            pop_up.click()
        except Exception:
            pass

    def target_account(self):
        sleep(3)
        search_bar=self.driver.find_element_by_xpath('//input[@class="XTCLo x3qfX "]')
        search_bar.send_keys(self.Target)
        target_url=self.Main_url + '/' + self.Target + '/'
        self.driver.get(target_url)
        sleep(3)
    def scroll_down(self):
        last_height=self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            sleep(3)
            new_height=self.driver.execute_script("return document.body.scrollHeight")
            if last_height != new_height:
                self.download()
            if new_height==last_height:
                break
            last_height=new_height
        sleep(5)
    def download(self):
        if not os.path.exists(self.Path):
            os.mkdir(self.Path)

        soup=BeautifulSoup(self.driver.page_source,'lxml')
        all_image=soup.find_all('div',class_="KL4Bh")
        for index,image in enumerate(all_image):
            filename='image' + str(index) + '.jpg'
            image_path=os.path.join(self.Path, filename)
            link=image.img['src']
            print("downloading.....")
            response=requests.get(link,stream=True)
            try:
                with open(image_path,'wb') as file:
                    shutil.copyfileobj(response.raw,file)
            except Exception as e:
                print(e)
                print("couldnot download")






if __name__ == '__main__':
    app = App()
