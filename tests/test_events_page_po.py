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

    def test_events_button_po(self):
        page = BasePage(self.driver)
        
        events_button = page.get_events_link()
        self.assertTrue(events_button.is_displayed(), "Events button is not displayed")
       
        page.navigate_to_events()

        events_page = EventsPage(self.driver)
        header = events_page.get_main_header()
        self.assertTrue(header.is_displayed(), "Events page is not opened")

if __name__ == "__main__":
    unittest.main()
