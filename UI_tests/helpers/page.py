import time
from contextlib import contextmanager

from selenium import webdriver
from selenium.common.exceptions import WebDriverException, TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.wait import WebDriverWait


import re
from playwright.sync_api import Playwright, sync_playwright, expect


class Page:
    def __init__(self, browser_context, url: str):
        self.browser_context = browser_context
        self.url = url

    def open(self):
        self.page = self.browser_context.new_page()
        self.page.goto(self.url)
        return self.page
    #     FIRSTNAME_FLD = 'input[name="FirstName"]'
    #     LASTNAME_FLD = 'input[name="LastName"]'
    # EMAIL_FLD = 'input[name="Email"]'
    # PHONE_FLD = 'input[name="Phone"]'
    #
    # GENDER_MAIL_CHBX = 'input[name="Gender"][value="Male"]'
    # GENDER_FEMAIL_CHBX = 'input[name="Gender"][value="Female"]'
    #
    # VACANCY_BX = 'select[name="Vacancy"]'
    # VACANCY_OPT = {'qa_engineer': 'QAA Engineer',
    #                'qa_engineer': 'QAA Engineer',
    #                'qa_engineer': 'QAA Engineer', }

    # def ajax_complete(self):
    #     try:
    #         return 0 == self.browser.execute_script("return jQuery.active")
    #     except WebDriverException:
    #         pass

    # @contextmanager
    # def wait_for_page_load(self, timeout=10):
    #     old_page = self.browser.find_element_by_id('application')
    #     yield
    #     WebDriverWait(self.browser, timeout).until(staleness_of(old_page))

    # def wait_for_spinner(self, timeout=10):
    #     if self.wait_for_element_present_by_locator(self.SPINNER, timeout=1) is not None:
    #         assert self.wait_for_element_hide_by_locator(self.SPINNER, timeout=timeout) is True
    #         return True
    #     else:
    #         return False

    # def wait_for_element_hide_by_locator(self, locator, timeout=10):
    #     wait = WebDriverWait(self.browser, timeout)
    #     try:
    #         wait.until(lambda driver: self.get_element(locator) is None)
    #         return True
    #     except TimeoutException:
    #         return False

    def close_session(self):
        self.browser.quit()

    def clear_field(self, locator):
        field = self.get_element(locator)
        field.clear()

    def send_param(self, locator, value):
        field = self.get_element(locator)
        field.send_keys(str(value))

    def send_param_with_clear(self, locator, value):
        self.clear_field(locator)
        self.send_param(locator, value)

    def get_element(self, locator):
        try:
            return self.browser.find_element(by=locator[0], value=locator[1])
        except NoSuchElementException:
            return None

    def get_elements_by_locator(self, tag, locator):
        element = self.get_element(locator)

        return self.get_elements_in_element(tag=tag, parent=element)

    @staticmethod
    def get_elements_in_element(tag, parent):
        list_of_elements = parent.find_elements_by_css_selector(tag)

        return list_of_elements if len(list_of_elements) != 0 else None

    @staticmethod
    def get_element_in_element(tag, parent):
        element = parent.find_element_by_css_selector(tag)

        return element if element else None

    def get_table_rows_by_locator(self, locator):
        return self.get_elements_by_locator(tag="tbody", locator=locator)

    def get_element_attribute(self, locator, attribute):
        return self.browser.find_element(by=locator[0], value=locator[1]).get_attribute(attribute)

    def wait_for_ajax(self):
        WebDriverWait(self.browser, 10).until(self.ajax_complete, "Timeout waiting for page to load")

    def is_element_present(self, locator):
        try:
            e = self.get_element(locator)
            return e is not None
        except NoSuchElementException:
            return False

    def refresh_page(self):
        self.browser.refresh()

    def wait_for_element_present_by_locator(self, locator, timeout=10):
        wait = WebDriverWait(self.browser, timeout)
        try:
            return wait.until(lambda driver: self.get_element(locator))
        except TimeoutException:
            return None

    def wait_table_rows_present(self, locator, timeout=10):
        wait = WebDriverWait(self.browser, timeout)
        try:
            return wait.until(lambda driver: self.get_table_rows_by_locator(locator))
        except TimeoutException:
            return None

    def wait_for_element_present_by_locator_with_page_refresh(self, locator, timeout=10):
        end_time = time.time() + timeout
        while time.time() < end_time:
            self.browser.refresh()
            self.wait_for_page_load()

            return self.get_element(locator)

    def click_element_by_locator(self, locator):
        element = self.wait_for_element_present_by_locator(locator)
        if element is None:
            raise Exception('Element is not present on page, locator: {}'.format(locator))
        element.click()

    def scroll_to_bottom(self):
        """решение временное, настранице авторизации не работает, так как там нет LOGOUT_BTN"""
        target_locator = self.LOGOUT_BTN
        self.scroll_to_locator(target_locator=target_locator)

    def scroll_to_locator(self, target_locator: tuple):
        target = self.browser.find_element(by=target_locator[0], value=target_locator[1])
        actions = ActionChains(self.browser)
        actions.move_to_element(target)
        actions.perform()

    def check_main_page_elements_present(self):
        assert self.is_element_present(self.LOGOUT_BTN) is True, 'Logout button was not present'
        assert self.is_element_present(self.PAGE_FOOTER) is True, 'Page footer was not present'
        assert self.is_element_present(self.NAVIGATION_BAR) is True, 'Navigation Bar was not present'

    def get_page_header(self):
        return self.get_element(self.PAGE_HEADER)

    def choose_in_pickapplet(self, locator, position=1):
        PICK_APPLET_MENU = (By.CLASS_NAME, 'Select-menu-outer')
        self.click_element_by_locator(locator)
        self.get_elements_by_locator(locator=PICK_APPLET_MENU, tag='div')[position].click()
