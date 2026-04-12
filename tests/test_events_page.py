import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

        events_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//header//a[contains(., 'Events') or contains(., 'Події')]")
            )
        )
        self.assertTrue(events_button.is_displayed(), "Events button is not displayed")
        events_button.click()

        header = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//p[contains(@class, 'main-header')]")
        )
    )
        self.assertTrue(header.is_displayed(), "Events page is not opened")

if __name__ == "__main__":
    unittest.main()
