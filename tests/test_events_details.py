import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestEventDetails(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_event_details_navigation(self):
        driver = self.driver
        wait = self.wait
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//mat-card"))
        )

        first_more_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//div[contains(@class, 'btn-group')]//button[contains(text(), 'Більше') or contains(text(), 'More')])[1]")
            )
        )
        first_more_button.click()

        event_details = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'event-title')]")
            )
        )
        self.assertTrue(event_details.is_displayed(), "Event details page is not opened")

        driver.back()

        events_list = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//mat-card"))
        )
        self.assertTrue(len(events_list) > 0, "Events list is not displayed")

if __name__ == "__main__":
    unittest.main()
