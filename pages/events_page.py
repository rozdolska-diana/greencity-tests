import re
from turtle import title
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.components.event_card_components import EventCardComponent

class EventsPage(BasePage):

    main_header_locator = (By.XPATH, "//p[contains(@class, 'main-header')]")
    items_fount_locator = (By.XPATH, "//div[@class='active-filter-container']/p")
    cards_locator = (By.XPATH, "//mat-card")
    more_in_card_locator = (By.XPATH, ".//button[normalize-space()='More' or normalize-space()='Більше']")
    event_time_filter_locator = (By.XPATH, "//mat-label[contains(text(), 'Event time') or contains(text(), 'Час події')]")
    upcoming_option_locator = (By.XPATH, "//mat-option[.//span[normalize-space()='Upcoming' or normalize-space()='Майбутні']]")

    def click_event_time_filter(self):
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.event_time_filter_locator)
    ).click()

    def select_upcoming(self):
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.upcoming_option_locator)
    ).click()

    def __init__(self, driver):
        super().__init__(driver)

    def get_main_header(self):
        return WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(self.main_header_locator)
    )
    def get_items_found(self):
        return self.driver.find_element(*self.items_fount_locator)
    
    def get_items_count(self):
        items_found = self.get_items_found()
        text = items_found.text

        match = re.search(r'\d+', text)
        
        if match:
            result = int(match.group())
            return result

    def get_cards(self)->list[EventCardComponent]:
        cards_web_elements = self.driver.find_elements(*self.cards_locator)
        cards = []
        for card_element in cards_web_elements:
            card = EventCardComponent(card_element)
            cards.append(card)

        return cards
