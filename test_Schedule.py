from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from test_Browsers import *
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

class Schedule_Locators():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, constant.WAIT_TIME)
        self.long_wait = WebDriverWait(self.driver, constant.LONG_WAIT)
        self.ENTITY_TAB = (By.CSS_SELECTOR, '.navigation-bar a[href="/"]')
        self.SCHEDULE_TEXT = (By.CSS_SELECTOR, 'span[class="span-text-style"]')
        self.EDIT_SCHEDULE = (By.CSS_SELECTOR,'.schedule-btn-text-container button[aria-label="Edit Schedule"]')
        self.SCHEDULE_POPUP_TEXT = (By.CSS_SELECTOR,'.modal-content .modal-title')
        self.ENABLE_CHECKBOX = (By.CSS_SELECTOR, '.form-check input[name="Enable Schedule"]')
        self.TIMEZONE = (By.CSS_SELECTOR, 'div[class="select__value-container css-1hwfws3"]')
        self.TIMEZONE_lIST = (By.CSS_SELECTOR, 'div[class="select__value-container css-1hwfws3"] div[class="select__input"] input[id="react-select-2-input"]')
        self.REPEAT_DRODOWN = (By.CSS_SELECTOR, '.form-group select[name="scheduleSelect"]')
        # self.REPEAT_DRODOWN = '.form-group select[name="scheduleSelect"]'
        self.SAVE_BUTTON = (By.CSS_SELECTOR, '.modal-footer .btn-primary')
        self.TIMEZONE_TEXT = (By.CSS_SELECTOR , '.schedule-btn-text-container span span')
        # self.SYNC_DATA_DISABLED = (By.CSS_SELECTOR, 'div[class="actions"] button[class="disabled btn btn-primary"]')
        self.SYNC_DATA_DISABLED = 'div[class="actions"] button[class="disabled btn btn-primary"]'
        self.SYNC_DATA_ENABLED = (By.CSS_SELECTOR, 'div[class="actions"] button[class="btn btn-primary"]')
        # self.SYNC_DATA_ENABLED = 'div[class="actions"] button[class="btn btn-primary"]'
        self.ENTITY_STATUS = (By.CSS_SELECTOR, '.table .card-body .status-container .index__status--2E3LL span')
        # self.ENTITY_STATUS = '.table .card-body .status-container .index__status--2E3LL span'
        self.CLOSE_NOTIFICATION_POPUP = (By.CSS_SELECTOR, '.Toastify__close-button svg[aria-hidden="true"]')
        self.SPINNER = (By.CSS_SELECTOR, 'div[class="data-loader"] svg[data-icon="spinner"]')

class Schedule_Impelementation(Schedule_Locators):

    def schedule_ingestion(self):
        # entity_tab = self.wait.until(ec.element_to_be_clickable(self.ENTITY_TAB))
        # entity_tab.click()
        self.spinner_disappear()
        # self.wait.until(ec.visibility_of_element_located(self.SCHEDULE_TEXT))
        schedule = self.wait.until(ec.visibility_of_element_located(self.EDIT_SCHEDULE))
        schedule.click()

        schedule_popup = self.wait.until(ec.visibility_of_element_located(self.SCHEDULE_POPUP_TEXT))
        assert schedule_popup.text == 'Edit Schedule'
        print(schedule_popup.text)

        enable_checkbox = self.wait.until(ec.visibility_of_element_located(self.ENABLE_CHECKBOX))
        if enable_checkbox.is_selected():
            print('Enable checkbox is selected')
        else:
            enable_checkbox.click()

        timezone_select = self.wait.until(ec.visibility_of_element_located(self.TIMEZONE))
        timezone_select.click()
        timezonelist = self.wait.until(ec.visibility_of_element_located(self.TIMEZONE_lIST))
        timezonelist.send_keys('pak')
        timezonelist.send_keys(Keys.ENTER)
        # repeat_day = Select(self.driver.find_element_by_css_selector(self.REPEAT_DRODOWN))
        repeat_day = Select(self.wait.until(ec.visibility_of_element_located(self.REPEAT_DRODOWN)))
        repeat_day.select_by_index('0')
        save_changes = self.wait.until(ec.visibility_of_element_located(self.SAVE_BUTTON))
        save_changes.click()
        self.close_notification_popup()

    # def timzone_assert(self):
    #     timzone_text = self.wait.until(ec.visibility_of_element_located(self.TIMEZONE_TEXT))
    #     try:
    #         assert timzone_text.text == 'Asia/Karachi'
    #     except AssertionError:
    #         print(timzone_text.text)
    #         self.schedule_again()

    # def schedule_again(self):
    #     schedule = self.wait.until(ec.visibility_of_element_located(self.EDIT_SCHEDULE))
    #     schedule.click()

    def sync_data(self):
        try:
            sync_en = self.wait.until(ec.visibility_of_element_located(self.SYNC_DATA_ENABLED))
            if sync_en.is_displayed():
             print('Button is Ensabled')
             sync_en.click()
             self.ingestion_status()
        except TimeoutException:
            if self.driver.find_element_by_css_selector(self.SYNC_DATA_DISABLED).is_displayed():
                print('Ingestion is already In Progress')

    def ingestion_status(self):
        time.sleep(10)
        status = self.wait.until(ec.visibility_of_all_elements_located(self.ENTITY_STATUS))
        status_is = status[23].text
        print('Ingestion is started and Status of Entity is: '+ status_is)
        assert status_is == ' In Progress'

    def close_notification_popup(self):
        close_conn_popup = self.wait.until(ec.element_to_be_clickable(self.CLOSE_NOTIFICATION_POPUP))
        close_conn_popup.click()

    def spinner_disappear(self):
        time.sleep(2)
        self.wait.until(ec.invisibility_of_element_located(self.SPINNER))
