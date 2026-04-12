from selenium.webdriver.common.by import By
from time import sleep



class BasePage:
    sign_in_button_locator = (By.CSS_SELECTOR, ".header_navigation-menu-right-list > .header_sign-in-link")
    language_switcher = (By.XPATH, "//ul[@aria-label='language switcher']")
    language_en_option = (By.XPATH, ".//span[contains(text(), 'En')]")
    language_ua_option = (By.XPATH, ".//span[contains(text(), 'Uk')]")

    eco_news_link_locator = (By.XPATH, "//header//a[contains(@class, 'url-name') and contains(., 'Еко новини') or contains(., 'Eco news')]")
    events_link_locator = (By.XPATH, "//header//a[contains(@class, 'url-name') and contains(., 'Події') or contains(., 'Events')]")
    def __init__(self, driver):
        self.driver = driver
    
    def get_sign_in_button(self):
        return self.driver.find_element(*self.sign_in_button_locator)

    def click_sign_in(self):
        sign_in_button = self.get_sign_in_button()
        sign_in_button.click()

    def get_language_switcher(self):
        return self.driver.find_element(*self.language_switcher)

    def switch_language(self, language):
        language_switcher = self.get_language_switcher()
        language_switcher.click()
        if language.lower() == "en":
            language_option = self.driver.find_element(*self.language_en_option)
        elif language.lower() == "ua":
            language_option = self.driver.find_element(*self.language_ua_option)
        else:
            raise ValueError("Unsupported language: {}".format(language))
        language_option.click()
        sleep(1)

    def get_eco_news_link(self):
        return self.driver.find_element(*self.eco_news_link_locator)
    
    def navigate_to_eco_news(self):
        eco_news_link = self.get_eco_news_link()
        eco_news_link.click()


    def get_events_link(self):
        return self.driver.find_element(*self.events_link_locator)
        
    def navigate_to_events(self):
        events_link = self.get_events_link()
        events_link.click()
