import re
from turtle import title

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from pages.components.event_card_components import EventCardComponent

class EventsPage(BasePage):

    main_header_locator = (By.XPATH, "//p[contains(@class, 'main-header')]")
    items_fount_locator = (By.XPATH, "//div[@class='active-filter-container']/p")
    cards_locator = (By.XPATH, "//mat-card")
    more_in_card_locator = (By.XPATH, ".//button[normalize-space()='More' or normalize-space()='Більше']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_main_header(self):
        return self.driver.find_element(*self.main_header_locator)
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
