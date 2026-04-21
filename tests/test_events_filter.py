import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestEventFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_event_time_filter(self):
        driver = self.driver
        wait = self.wait

        events = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//mat-card"))
        )
        self.assertTrue(len(events) > 0, "Events are not loaded")

        filter_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//mat-label[contains(text(), 'Event time') or contains(text(), 'Час події')]")
            )
        )
        filter_button.click()

        option = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//mat-option[.//span[normalize-space()='Upcoming' or normalize-space()='Майбутні']]")
            )
        )
        option.click()

        filtered_events = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//mat-card"))
        )
        self.assertTrue(len(filtered_events) > 0, "Filtered events are not displayed")

if __name__ == "__main__":
    unittest.main()
