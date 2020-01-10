from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

from selenium.webdriver import ActionChains
from test_Browsers import *

class Entity_Conf_Locators():

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(self.driver, constant.WAIT_TIME)
        self.short_wait = WebDriverWait(self.driver, constant.SHORT_WAIT)
        self.long_wait = WebDriverWait(self.driver, constant.LONG_WAIT)
        self.CHOOSE_DATASOURCE_DROPDOWN = (By.CSS_SELECTOR, '[id="data-source-select"] input')
        self.ENTITY_TAB = (By.CSS_SELECTOR, '.navigation-bar a[href="/"]')
        self.SCHEDULE_TEXT = (By.CSS_SELECTOR, 'span[class="span-text-style span-text-font"]')
        # self.SCROLL_TILL_ELEMENT = 'a[aria-label="Manage Library Collection Statistic entity"]'
        self.SCROLL_TILL_ELEMENT = 'a[aria-label="Manage Library Branch entity"]'
        # TEXT_PRESENT = (By.XPATH, '//*[@id="app"]/div/div[1]/main/div/div/div[2]/div[2]/div[2]/div[1]/div/div[22]/div[1]/div[1]/div[1]/span/span[1]/span')
        self.TEXT_PRESENT = '.card-body .header .title span span'

        self.ENTITY_MANAGE_BUTTON = (By.CSS_SELECTOR, ' .table .card .card-footer a[aria-label="Manage Library Branch entity"]')
        self.RESET_NOTIFICATION = (By.CSS_SELECTOR, '.Toastify__toast-body .toast-body')
        self.TITLE_CHOOSE_DATASORUCE = (By.CSS_SELECTOR, 'div[class="index__datasource--3oIg-"] h2[class="text-center ds-heading"]')
        self.REMOVE_SELECTED_DATASOURCE = 'span[class="badge badge-secondary"] svg[data-icon="times-circle"]'
        # CHOOSE_DATASOURCE_VALUE = (By.CSS_SELECTOR, 'div[id="react-select-2-option-0"]')
        self.DATASOURCE_CONTINUE = (By.CSS_SELECTOR, 'button[aria-label="Continue"]')

        self.TEST_QUERY = (By.CSS_SELECTOR, 'button[aria-label="Test Query"]')
        self.CLOSE_NOTE = (By.CSS_SELECTOR, 'button[aria-label="Close"]')
        self.EXECUTE_STATUS = (By.CSS_SELECTOR, 'div[class="alert-container"] div[role="alert"]')
        self.QUERY_PAN = (By.CSS_SELECTOR, 'span[role="presentation"]')

        self.COLUMN1 = (By.CSS_SELECTOR, 'div[class="dropdown-header"] div[id="mapping-selectbranchid"]')
        self.COLUMN2 = (By.CSS_SELECTOR, 'div[id="mapping-selectrecordactivitydate"]')
        self.COLUMN3 = (By.CSS_SELECTOR, 'div[id="mapping-selectbranchname"]')
        self.COLUMN04 = (By.CSS_SELECTOR, 'div[id="mapping-selectbranchstatusraw"]')
        self.COLUMN5 = (By.CSS_SELECTOR, 'div[id="mapping-selectbranchstatus"]')
        self.COLUMN6 = (By.CSS_SELECTOR, 'div[id="mapping-selectiscentralormainbranch"]')
        self.COLUMN7 = (By.CSS_SELECTOR, 'div[id="mapping-selectisipedsreportable"]')
        self.COLUMN_VALUE = (By.CSS_SELECTOR, 'div[id^="react-select"]')

        self.ENUM_MAPPING1 = (By.CSS_SELECTOR, 'div[class="col-md-6"] select[id="branchStatusEnumDropDown0"]')
        self.ENUM_MAPPING2 = (By.CSS_SELECTOR, 'div[class="col-md-6"] select[id="branchStatusEnumDropDown1"]')
        self.COMPLETE_WIZARD = (By.CSS_SELECTOR, 'button[aria-label="Complete Wizard"]')
        self.PUBLISH_ENTITY = (By.CSS_SELECTOR, 'button[class="publish-btn btn btn-primary"]')
        self.CONFIRM_POPUP_TEXT = (By.CSS_SELECTOR, '.modal-content .modal-body')
        self.POPUP_PUBLISH_BUTTON = (By.CSS_SELECTOR, 'div[class="modal-content"] button[class="btn btn-primary"]')
        self.CLOSE_NOTIFICATION_POPUP = (By.CSS_SELECTOR, '.Toastify__close-button svg[aria-hidden="true"]')
        self.SPINNER = (By.CSS_SELECTOR, 'div[class="data-loader"] svg[data-icon="spinner"]')

        self.academic = (By.XPATH, '//*[@id="app"]/div/div[1]/main/div/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/a')
        self.RESET_ENTITY = (By.CSS_SELECTOR, 'div[class="footer secondary-footer"] button[aria-label="Reset Entity"]')
        self.POPUP_RESET_BUTTON = (By.CSS_SELECTOR, 'div[class="modal-content"] button[class="btn btn-primary"]')


class Entity_Configuration(Entity_Conf_Locators):

    def entity_dashboard(self):

        entity_tab = self.wait.until(ec.element_to_be_clickable(self.ENTITY_TAB))
        entity_tab.click()
        self.spinner_disappear()
        # time.sleep(3)
        self.wait.until(ec.visibility_of_element_located(self.SCHEDULE_TEXT))

    def entity_manage_button(self):

        act = ActionChains(self.driver)
        act.move_to_element(self.driver.find_element_by_css_selector(self.SCROLL_TILL_ELEMENT))
        act.send_keys(Keys.PAGE_DOWN).perform()
        for elem in (self.driver.find_elements_by_css_selector(self.TEXT_PRESENT)):
            if elem.text == 'Library Branch':
                print('We Want to Configure: ' + elem.text)
                break

        entity_detail = self.wait.until(ec.element_to_be_clickable(self.ENTITY_MANAGE_BUTTON))
        entity_detail.click()

    def entity_configured_or_not(self):
        try:
            self.spinner_disappear()
            print("spinner is disappeared on Detail page")
            reset_entity_button = self.short_wait.until(ec.visibility_of_element_located(self.RESET_ENTITY))
            if reset_entity_button.is_displayed():
                print('Data Source is configured already, we are going to click on Reset Entity button')
                self.reset_entity()
        except TimeoutException:
            print("Data Source was not configured already")

    def reset_entity(self):
        reset_entity_button = self.short_wait.until(ec.visibility_of_element_located(self.RESET_ENTITY))
        reset_entity_button.click()
        confirm_text = self.wait.until(ec.visibility_of_element_located(self.CONFIRM_POPUP_TEXT))
        assert confirm_text.text == 'Are you sure you want to reset this Entity?'
        print(confirm_text.text)
        reset_popup_button = self.wait.until(ec.element_to_be_clickable(self.POPUP_PUBLISH_BUTTON))
        reset_popup_button.click()
        self.confirm_entity_reset()

    def confirm_entity_reset(self):
        reset_notification = self.wait.until(ec.visibility_of_element_located(self.RESET_NOTIFICATION))
        print(reset_notification.text)
        assert reset_notification.text == 'Entity is reset.'

    def choose_datasource(self):
        try:
            self.spinner_disappear()
            remove_datasource = self.driver.find_element_by_css_selector(self.REMOVE_SELECTED_DATASOURCE)
            if remove_datasource.is_displayed():
                remove_datasource.click()  # this will remove the selected data source if it's already selected
                print('Selected data source is removed')

        except NoSuchElementException:
            print("Data Source was not selected already")

        choose_your_datasource = self.wait.until(ec.visibility_of_element_located(self.TITLE_CHOOSE_DATASORUCE))
        print(choose_your_datasource.text)
        assert choose_your_datasource.text == 'Choose your Data Source'
        time.sleep(120)
        choose_datasource_dropdown = self.wait.until(ec.visibility_of_element_located(self.CHOOSE_DATASOURCE_DROPDOWN))
        choose_datasource_dropdown.send_keys(constant.CSV_DATASOURCE)
        choose_datasource_dropdown.send_keys(Keys.ENTER)
        continue_button = self.wait.until(ec.visibility_of_element_located(self.DATASOURCE_CONTINUE))
        continue_button.click()

    def placeholder_query(self):

        query = self.wait.until(ec.visibility_of_element_located(self.QUERY_PAN))
        print(query.text)
        assert query.text == constant.CSV_QUERY

    def execute_query(self):

        query = self.wait.until(ec.element_to_be_clickable(self.TEST_QUERY))
        query.click()
        self.long_wait.until(ec.element_to_be_clickable(self.TEST_QUERY))
        execution_status = self.long_wait.until(ec.visibility_of_element_located(self.EXECUTE_STATUS))
        assert execution_status.text == '×\nSuccess\nQuery test ran successfully with no errors.'
        print(execution_status.text)
        notification_close = self.wait.until(ec.element_to_be_clickable(self.CLOSE_NOTE))
        notification_close.click()

    def column_mapping(self):

        column1 = self.wait.until(ec.visibility_of_element_located(self.COLUMN1))
        column1.click()
        value = self.wait.until(ec.visibility_of_all_elements_located(self.COLUMN_VALUE))
        value[1].click()

        column2 = self.wait.until(ec.visibility_of_element_located(self.COLUMN2))
        column2.click()
        value = self.wait.until(ec.visibility_of_all_elements_located(self.COLUMN_VALUE))
        value[2].click()

        column3 = self.wait.until(ec.visibility_of_element_located(self.COLUMN3))
        column3.click()
        time.sleep(2)
        value = self.wait.until(ec.visibility_of_all_elements_located(self.COLUMN_VALUE))
        value[3].click()

        column04 = self.wait.until(ec.visibility_of_element_located(self.COLUMN04))
        column04.click()
        value = self.wait.until(ec.visibility_of_all_elements_located(self.COLUMN_VALUE))
        value[0].click()

        column5 = self.wait.until(ec.visibility_of_element_located(self.COLUMN5))
        column5.click()
        value = self.wait.until(ec.visibility_of_all_elements_located(self.COLUMN_VALUE))
        value[4].click()

        column6 = self.wait.until(ec.visibility_of_element_located(self.COLUMN6))
        column6.click()
        value = self.wait.until(ec.visibility_of_all_elements_located(self.COLUMN_VALUE))
        value[5].click()

        column7 = self.wait.until(ec.visibility_of_element_located(self.COLUMN7))
        column7.click()
        value = self.wait.until(ec.visibility_of_all_elements_located(self.COLUMN_VALUE))
        value[6].click()

        continue_button = self.wait.until(ec.visibility_of_element_located(self.DATASOURCE_CONTINUE))
        continue_button.click()

    def enum_mapping(self):

        enum1 = Select(self.long_wait.until(ec.element_to_be_clickable(self.ENUM_MAPPING1)))
        enum1.select_by_value('Active')

        enum2 = Select(self.wait.until(ec.element_to_be_clickable(self.ENUM_MAPPING2)))
        enum2.select_by_value('Inactive')

        wizard_complete = self.wait.until(ec.visibility_of_element_located(self.COMPLETE_WIZARD))
        wizard_complete.click()

    def publish_entity(self):
        self.spinner_disappear()
        publish = self.wait.until(ec.element_to_be_clickable(self.PUBLISH_ENTITY))
        publish.click()
        confirm_text = self.wait.until(ec.visibility_of_element_located(self.CONFIRM_POPUP_TEXT))
        assert confirm_text.text == 'Are you sure you want to publish this Entity?'
        print(confirm_text.text)
        publish_popup_button = self.wait.until(ec.element_to_be_clickable(self.POPUP_PUBLISH_BUTTON))
        publish_popup_button.click()
        self.wait.until(ec.element_to_be_clickable(self.PUBLISH_ENTITY))
        self.close_notification_popup()
        self.entity_dashboard()

    def close_notification_popup(self):
        close_conn_popup = self.wait.until(ec.element_to_be_clickable(self.CLOSE_NOTIFICATION_POPUP))
        close_conn_popup.click()

    def spinner_disappear(self):
        time.sleep(2)
        try:
            self.wait.until(ec.invisibility_of_element_located(self.SPINNER))
        except NoSuchElementException:
            print("loader not present")