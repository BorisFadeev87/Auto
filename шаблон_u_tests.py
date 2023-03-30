from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time

class TestMainPage(unittest.TestCase):

    def setUp(self):#перед началом каждого теста
        # pass #заглушка
        self.driver = webdriver.Chrome()  # подключаю драйвер
        self.driver.get("https://www.python.org/")  # делаем запрос на открытие страницы

    def test_search(self):
        driver = self.driver
        driver.find_element(By.ID, "id-search-field").click()
        driver.find_element(By.ID, "id-search-field").clear()
        driver.find_element(By.ID, "id-search-field").send_keys("pycon")
        driver.find_element(By.ID, "submit").click()
        #self.assertEqual()
        time.sleep(3)

    def tearDown(self):# после каждого теста
        self.driver.close()#закрывает окно браузер
        #self.driver.quit()#закрывает вкладке браузер
