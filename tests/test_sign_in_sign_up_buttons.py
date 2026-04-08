import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class TestSignInSignUpButtons(unittest.TestCase):
    BASE_URL = "https://www.greencity.cx.ua/#/greenCity"
    modal_xpath = "//app-auth-modal"
    def setUp(self):

        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(1)
        self.driver.maximize_window()
        self.driver.get(self.BASE_URL)
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_sign_in_button(self):
        driver = self.driver
        wait = self.wait

        sign_in_selector = ".header_navigation-menu-right-list > .header_sign-in-link"
        sign_in_button = driver.find_element(By.CSS_SELECTOR, sign_in_selector)
        self.assertTrue(sign_in_button.is_displayed())
        sign_in_button.click()
        sleep(5)
    
    
        modal = driver.find_element(By.XPATH, "//app-auth-modal")
        self.assertTrue(modal.is_displayed(), "Login modal is not displayed")

        email_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "password")
        self.assertTrue(email_input.is_displayed(),  "Email input is not displayed")
        self.assertTrue(password_input.is_displayed(), "Password input is not displayed")
        sleep(5)


    def test_sign_up_button(self):
        driver = self.driver
        wait = self.wait
        
        sign_up_selector = ".header_navigation-menu-right-list > .header_sign-up-link"
        sign_up_button = driver.find_element(By.CSS_SELECTOR, sign_up_selector)
        self.assertTrue(sign_up_button.is_displayed())
        sign_up_button.click()
        sleep(2)
        modal = driver.find_element(By.XPATH, "//app-auth-modal")
        self.assertTrue(modal.is_displayed(), "sign up modal is not displayed")
        
        email_input = driver.find_element(By.ID, "email")
        user_name_input = driver.find_element(By.ID, "firstName")
        password_input = driver.find_element(By.ID, "password")
        repeat_password_input = driver.find_element(By.ID, "repeatPassword")
        
        self.assertTrue(email_input.is_displayed(), "Email input is not displayed")
        self.assertTrue(user_name_input.is_displayed(), "Name input is not displayed")
        self.assertTrue(password_input.is_displayed(), "Password input is not displayed")
        self.assertTrue(repeat_password_input.is_displayed(), "Repeat Password input is not displayed")


if __name__ == "__main__":
    unittest.main()
