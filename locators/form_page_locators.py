import random

from selenium.webdriver.common.by import By


class FormPageLocators:
    FIRST_NAME = (By.CSS_SELECTOR, '#firstName')
    LAST_NAME = (By.CSS_SELECTOR, '#lastName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    GENDER = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='gender-radio-{random.randint(1, 3)}']")
    MOBILE = (By.CSS_SELECTOR, "input[id='userNumber']")
    DATE_OF_BIRTH = (By.CSS_SELECTOR, 'id="dateOfBirthInput"')
    SUBJECT = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')
    HOBBIES = (By.CSS_SELECTOR, f'div[class*="custom-control"] label[for="hobbies-checkbox-{random.randint(1, 3)}"]')
    FILE_INPUT = (By.CSS_SELECTOR, "input[id='uploadPicture']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    SELECT_STATE = (By.CSS_SELECTOR, 'div[id="state"]')
    STATE_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    SELECT_CITY = (By.CSS_SELECTOR, 'div[id="city"]')
    CITY_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
    SUBMIT = (By.CSS_SELECTOR, '#submit')

    # table result

    RESULT_TABLE = (By.XPATH, '//div[@class="table-responsive"]//td[2]')
