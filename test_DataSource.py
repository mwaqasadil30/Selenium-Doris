from selenium.webdriver.common.by import By
from test_Constant_Elements import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from test_Browsers import *
import os


class DataSource_Locators():

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(self.driver, constant.WAIT_TIME)
        self.short_wait = WebDriverWait(self.driver, constant.SHORT_WAIT)
        self.long_wait = WebDriverWait(self.driver, constant.LONG_WAIT)

        self.DATASOURCE_BUTTON = (By.CSS_SELECTOR, 'a[href="/data-sources"] svg[data-icon="database"]')
        self.ADD_BUTTON = (By.CSS_SELECTOR, '.float-right .btn')

        self.DATASOURCE_NAME = (By.CSS_SELECTOR, 'input[name="name"]')
        self.DATASOURCE_CSV_RADIO = (By.CSS_SELECTOR, 'input[id="CSV"]')
        self.BROWSE_CSV = 'csvFile'
        self.UPLOAD = (By.CSS_SELECTOR, 'div[class="col-12"] button[aria-disabled="false"]')
        self.NOT_UPLOADED_TEXT = (By.CSS_SELECTOR, 'span[id="upload-message"]')
        self.UPLOADED_TEXT = (By.CSS_SELECTOR, 'span[class="connection-status"]')
        # (// *[contains( @ aria-label, "close")])[]

        self.DATASOURCE_COLLEAGUE_RADIO = 'input[value="Colleague"]'
        self.HOST_NAME = 'host'
        self.PORT_NAME = 'port'
        self.SID_NAME = 'sid'
        self.USER_NAME = 'dbUsername'
        self.PASSWORD = 'dbPassword'
        self.SHOW_PASSWORD = 'showPassword'
        self.CONNECTION_BUTTON = 'connection-btn'
        self.CONNECTION_SUCCESS_TEXT = (By.CLASS_NAME, 'connection-status')
        self.CONNECTION_SUCCESS_POPUP = (By.CSS_SELECTOR,'div[class="toast-body"]')
        self.CREATE_BUTTON = (By.ID,'submit')

        self.EDIT_LINK = (By.CSS_SELECTOR,'div[class="text-center"] a[class="benton-sans-medium"]')
        self.SAVE_CHANGES_DS = (By.CSS_SELECTOR,'.form-footer button[type="submit"]')
        self.DELETE_BUTTON = (By.CSS_SELECTOR, '.form-footer button[aria-disabled="false"]')
        self.DELETE_POPUP_WINDOW = (By.CSS_SELECTOR, '.modal-content .modal-footer .btn-danger')

        self.SPINNER = (By.CSS_SELECTOR, 'div[class="data-loader"] svg[data-icon="spinner"]')
        # self.CLOSE_NOTIFICATION_POPUP = (By.CSS_SELECTOR, '.Toastify__close-button svg[aria-hidden="true"]')
        # (// *[contains( @ aria-label, "close")])[]
        # self.CLOSE_NOTIFICATION_POPUP = '//*[contains(@aria-label, close'


class DataSource_Implementation(DataSource_Locators):

    def datasource_tab(self):
        datasource_tab = self.wait.until(ec.visibility_of_element_located(self.DATASOURCE_BUTTON))
        datasource_tab.click()

    def add_csv_datasource(self):
        # spinner = wait.until(ec.invisibility_of_element_located(obj_locator_datasource.SPINNER))
        self.click_add_button()  # calling function for add new button
        # self.spinner_disappear()

        name_dataSource = self.wait.until(ec.visibility_of_element_located(self.DATASOURCE_NAME))
        name_dataSource.send_keys(constant.CSV_DATASOURCE)
        csv_radio_button = self.wait.until(ec.visibility_of_element_located(self.DATASOURCE_CSV_RADIO))
        csv_radio_button.click()
        browse_file = self.driver.find_element_by_id(self.BROWSE_CSV)
        browse_file.send_keys(os.getcwd() + "/LibraryBranch-QA.csv")
        self.upload_file()
        # self.click_create_button()
        # file_not_uploaded = self.wait.until(ec.visibility_of_element_located(self.NOT_UPLOADED_TEXT))
        # assert file_not_uploaded.text == 'File not uploaded'
        # time.sleep(5)
        # csv_radio_button.click()
        self.click_create_button()
        self.spinner_disappear()

    def upload_file(self):
        upload_file = self.wait.until(ec.element_to_be_clickable(self.UPLOAD))
        upload_file.click()
        self.assert_upload()

    def assert_upload(self):
        try:

            message_upload = self.short_wait.until(ec.visibility_of_element_located(self.UPLOADED_TEXT))
            if message_upload.is_displayed():

                print(message_upload.text)
                assert message_upload.text == 'File Uploaded!'
        except TimeoutException:
            print('File not uploaded on first try')
            self.upload_file()


    def add_banner_datasource(self):
        self.click_add_button()
        name_dataSource = self.wait.until(ec.visibility_of_element_located(self.DATASOURCE_NAME))
        name_dataSource.send_keys("Banner Doris")
        data_source_radio = self.driver.find_element_by_css_selector(self.DATASOURCE_COLLEAGUE_RADIO)
        data_source_radio.click()

        host = self.driver.find_element_by_name(self.HOST_NAME)
        host.send_keys(constant.HOST_NAME)
        port = self.driver.find_element_by_name(self.PORT_NAME)
        port.send_keys(constant.PORT)
        sid = self.driver.find_element_by_name(self.SID_NAME)
        sid.send_keys(constant.SID)
        user = self.driver.find_element_by_name(self.USER_NAME)
        user.send_keys(constant.USER_NAME)
        password = self.driver.find_element_by_name(self.PASSWORD)
        password.send_keys(constant.USER_PSWRD)
        showPassword = self.driver.find_element_by_name(self.SHOW_PASSWORD)
        showPassword.click()

    def check_connection(self):
        connection_button = self.driver.find_element_by_class_name(self.CONNECTION_BUTTON)
        connection_button.click()

        message = self.wait.until(ec.visibility_of_element_located(self.CONNECTION_SUCCESS_TEXT))
        print(message.text)
        assert message.text == 'Connection Successful!'
        self.click_create_button()
        self.spinner_disappear()


    def edit_datasource(self):
        self.spinner_disappear()
        edit_link = self.wait.until(ec.visibility_of_all_elements_located(self.EDIT_LINK))
        edit_link[0].click()
        self.spinner_disappear()
        port = self.driver.find_element_by_name(self.PORT_NAME)
        port.send_keys(Keys.CONTROL, 'a')
        port.send_keys(Keys.BACKSPACE)
        port.send_keys("1234")
        ds_saveChanges = self.wait.until(ec.visibility_of_element_located(self.SAVE_CHANGES_DS))
        ds_saveChanges.click()

    def delete_datasource(self):
        self.spinner_disappear()
        edit_link = self.wait.until(ec.visibility_of_all_elements_located(self.EDIT_LINK))
        edit_link[0].click()
        self.spinner_disappear()
        delete_button = self.wait.until(ec.visibility_of_element_located(self.DELETE_BUTTON))
        delete_button.click()
        delete_window = self.wait.until(ec.visibility_of_element_located(self.DELETE_POPUP_WINDOW))
        delete_window.click()
        self.spinner_disappear()
        self.close_notification_popup()

    def click_create_button(self):
        self.create_button = self.wait.until(ec.visibility_of_element_located(self.CREATE_BUTTON))
        self.create_button.click()

    def click_add_button(self):
        add_button = self.wait.until(ec.visibility_of_element_located(self.ADD_BUTTON))
        add_button.click()

    def close_notification_popup(self):


        popup_list = self.driver.find_elements_by_xpath("//*[contains(@aria-label,'close')]")
        # popup_list = self.driver.find_elements_by_xpath(self.CLOSE_NOTIFICATION_POPUP)
        for i in range(len(popup_list)):
            x = i + 1
            #  we use x x+1 to start from the 1st element in the list of xpath axis
            popup = self.driver.find_element_by_xpath("(//*[contains(@aria-label,'close')])[" + str(x) + "]")
            print(popup.text)
            popup.click()
            # self.driver.find_element_by_xpath("(self.CLOSE_NOTIFICATION_POPUP)[" + str(x) + "]").click()
            # # self.CLOSE_NOTIFICATION_POPUP

        # while self.short_wait.until(ec.invisibility_of_element_located(self.CLOSE_NOTIFICATION_POPUP)):
        #     # time.sleep(3)
        #     try:
        #         close_conn_popup = self.short_wait.until(ec.element_to_be_clickable(self.CLOSE_NOTIFICATION_POPUP))
        #         close_conn_popup.click()
        #     except TimeoutException:
        #         print("No more Notifications left")
        #         break

    def spinner_disappear(self):
        time.sleep(2)
        try:
            self.wait.until(ec.invisibility_of_element_located(self.SPINNER))
        except NoSuchElementException:
            print("loader not present")


    # def spinner_aappear(self):
    #     # time.sleep(2)
    #     try:
    #         self.driver.find_element_by_css_selector('div[class="data-loader"] svg[data-icon="spinner"]')
    #         self.spinner_aappear()
    #     except NoSuchElementException:
    #         print("wait for loader to be appeared")
    #         self.spinner_aappear()

