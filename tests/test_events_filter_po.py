import unittest
from selenium import webdriver
from pages.events_page import EventsPage

class TestEventFilter(unittest.TestCase):

    EVENTS_URL = "https://www.greencity.cx.ua/#/greenCity/events"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get(self.EVENTS_URL)

    def tearDown(self):
        self.driver.quit()

    def test_event_time_filter(self):

        events_page = EventsPage(self.driver)
        events = events_page.get_cards()
        self.assertTrue(len(events) > 0, "Events are not loaded")

        events_page.click_event_time_filter()
        events_page.select_upcoming()

        filtered_events = events_page.get_cards()
        self.assertTrue(len(filtered_events) > 0, "Filtered events are not displayed")

if __name__ == "__main__":
    unittest.main()
