import random
import time

import allure
from selenium.common.exceptions import UnexpectedAlertPresentException

from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalDialogsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    @allure.step('check opened new tab ')
    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

    @allure.step('check opened new window')
    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    @allure.step('get text from alert')
    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    @allure.step('check alert appear after 5 sec')
    def check_alert_appear_5_sec(self):
        self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        time.sleep(6)
        try:
            alert_window = self.driver.switch_to.alert
            return alert_window.text
        except UnexpectedAlertPresentException:
            alert_window = self.driver.switch_to.alert
            return alert_window.text

    @allure.step('check confirm alert')
    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    @allure.step('check prompt alert')
    def check_prompt_alert(self):
        text = f"autotest{random.randint(0, 999)}"
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_RESULT).text
        return text, text_result


class FramesPage(BasePage):
    locators = FramesPageLocators()

    @allure.step('check frame')
    def check_frame(self, frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]
        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    @allure.step('check nested frame')
    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()

    @allure.step('check modal dialogs')
    def check_modal_dialogs(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        title_small = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
        body_small_text = self.element_is_visible(self.locators.BODY_SMALL_MODAL).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        title_large = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text
        body_large_text = self.element_is_visible(self.locators.BODY_LARGE_MODAL).text
        return [title_small, len(body_small_text)], [title_large, len(body_large_text)]
