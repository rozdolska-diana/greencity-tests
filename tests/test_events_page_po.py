import unittest
from selenium import webdriver
from pages.base_page import BasePage
from pages.events_page import EventsPage

class TestEventsPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  
        self.driver.maximize_window()
        self.driver.get("https://www.greencity.cx.ua/#/greenCity")

    def tearDown(self):
        self.driver.quit()  

    def test_open_events_page(self):
        page = EventsPage(self.driver)
        page.navigate_to_events()  

        self.assertIn("events", self.driver.current_url.lower())

if __name__ == "__main__":
    unittest.main()
