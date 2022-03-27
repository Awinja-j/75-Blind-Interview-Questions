import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

logging.basicConfig(filename='votes.log', level=logging.INFO)


class VoteVusiThembekwayo:

    def __init__(self):
        self.s =  Service('/Users/ingari/Desktop/DESKTOP/75-Blind-Interview-Questions/chromedriver 2')
        self.driver = webdriver.Chrome(service=self.s)
        self.url = 'https://pulsembed.eu/p2em/ym6fRvvNd/'



    def vote(self):
        self.driver.get(self.url)

        self.driver.maximize_window()


        self.driver.find_element(by=By.XPATH, value="//input[@type='radio' and @value='50785364']").click()


        self.driver.find_element(by=By.LINK_TEXT, value='Vote').click()

        time.sleep(2)


        self.driver.close()

        logging.info('voting succesful {}'.format(time.ctime()))


if __name__ == '__main__':
    loop = 100000
    count = 0
    while count < loop:
        count += 1
        logging.info('{} {}'.format(count, time.ctime()))
        v = VoteVusiThembekwayo()
        v.vote()

