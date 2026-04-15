import unittest
from selenium import webdriver
from pages.events_page import EventsPage
from pages.event_details_page import EventDetailsPage

class TestEventDetails(unittest.TestCase):
    EVENTS_URL = "https://www.greencity.cx.ua/#/greenCity/events"
    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get(self.EVENTS_URL)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_event_details_navigation(self):

        events_page = EventsPage(self.driver)
        details_page = EventDetailsPage(self.driver)

        cards = events_page.get_cards()
        self.assertTrue(len(cards) > 0, "Events are not loaded")
        cards[0].click_more()

        self.assertTrue(
            details_page.is_event_title_displayed(),
            "Event details page is not opened"
        )

        current_url = self.driver.current_url
        self.assertIn("/events", current_url)
        self.driver.back()
        
        cards_after = events_page.get_cards()
        self.assertTrue(len(cards_after) > 0, "Events list is not displayed")

if __name__ == "__main__":
    unittest.main()
