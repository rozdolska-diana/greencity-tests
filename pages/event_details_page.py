from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class EventDetailsPage(BasePage):

    event_title = (By.XPATH, "//div[contains(@class, 'event-title')]")

    def is_event_title_displayed(self):
        wait = WebDriverWait(self.driver, 10) 

        element = wait.until(
            EC.visibility_of_element_located(self.event_title)
        )
        return element.is_displayed()
