from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class FormInput():

    def __init__(self):
        self.chrome_driver_path = "C:/Program Files/chromedriver.exe"
        self.google_link = "https://docs.google.com/forms/d/e/1FAIpQLScuU4QOqrPGvIOpHiAdXwZ6mDpfJ8viVfoU47L145KGUxmCFA/viewform?usp=sf_link"
        self.service = Service(self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.service)

    def input_info(self, housing_data):
        for info_tuple in housing_data:
            self.driver.get(self.google_link)
            time.sleep(2)
            submit_button = self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
            for i in range(len(info_tuple)):
                answer = info_tuple[i]
                input_answer = self.driver.find_element(By.XPATH, f"//*[@id='mG61Hd']/div[2]/div/div[2]/div[{i+1}]/div/div/div[2]/div/div[1]/div/div[1]/input")
                input_answer.send_keys(answer)
            submit_button.click()


