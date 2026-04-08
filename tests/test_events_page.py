import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class TestEventsPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.greencity.cx.ua/#/greenCity")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_events_button(self):
        driver = self.driver
        wait = self.wait

        # Знаходимо кнопку "Події" у хедері
        events_button_selector = (By.XPATH, "//header//a[contains(@class, 'url-name') and contains(., 'Події') or contains(., 'Events')]")
        events_button = driver.find_element(*events_button_selector)
        self.assertTrue(events_button.is_displayed(), "Кнопка 'Події' не відображається")
        events_button.click()
        sleep(2)

        # Перевіряємо, що заголовок "Події" видно на сторінці
        header_selector = (By.XPATH, "//p[contains(@class, 'main-header') and contains(., 'Події') or contains(., 'Events')]")
        header = driver.find_element(*header_selector)
        self.assertTrue(header.is_displayed(), "Сторінка подій не завантажилась після натискання кнопки")
        sleep(2)

if __name__ == "__main__":
    unittest.main()
