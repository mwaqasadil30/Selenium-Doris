import pytest
import allure
from test_Browsers import *
from test_DataSource import *
from test_Login import *
from test_Entity_Conf import *
from test_Schedule import *

browser = Browser()
driver=browser.chrome()

login = Login_Implement(driver)
ds = DataSource_Implementation(driver)
Entity = Entity_Configuration(driver)
Schedule = Schedule_Impelementation(driver)


@allure.feature("Login")
@allure.title("Login Functionality")
def test_login():
    login.login_functionality()


@allure.feature("Data Source")
@allure.title("Click on Data Source Tab")
@pytest.mark.dependency
def test_datasource_tab_click():
    ds.datasource_tab()

@allure.feature("Data Source")
@allure.title("Create CSV Data Source Tab")
@pytest.mark.dependency(depends=["test_datasource_tab_click"])
def test_csv_datasource():
    ds.add_csv_datasource()

@allure.feature("Data Source")
@allure.title("Create Banner Data Source Tab")
@pytest.mark.dependency(depends=["test_csv_datasource"])
def test_banner_datasource():
    ds.add_banner_datasource()
    ds.check_connection()

@allure.feature("Data Source")
@allure.title("Edit Banner Data Source Tab")
@pytest.mark.dependency(depends=["test_banner_datasource"])
def test_edit_banner_datasource():
    ds.edit_datasource()

@allure.feature("Data Source")
@allure.title("Delete Banner Data Source Tab")
@pytest.mark.dependency(depends=["test_edit_banner_datasource"])
def test_delete_banner_datasource():
    ds.delete_datasource()


@allure.feature("Entity Dashboard")
@allure.title("Click on Manage button of Library Branch Entity")
@pytest.mark.dependency()
def test_entity_manage_button():
    Entity.entity_dashboard()
    Entity.entity_manage_button()

@allure.feature("Entity Configuration")
@allure.title("Reset the entity if already configured")
@pytest.mark.dependency(depends=["test_entity_manage_button"])
@pytest.mark.xfail(reason="Entity Cannot be reset when ingestion is in progress")
def test_reset_entity_if_configured():
    Entity.entity_configured_or_not()

@allure.feature("Entity Configuration")
@allure.title("Choose CSV Data Source")
@pytest.mark.dependency(depends=["test_reset_entity_if_configured"])
def test_entity_datasource():
    Entity.choose_datasource()

@allure.feature("Entity Configuration")
@allure.title("Assert Placeholder Query and Execute It")
@pytest.mark.dependency(depends=["test_entity_datasource"])
def test_query_execution():
    Entity.placeholder_query()
    Entity.execute_query()

@allure.feature("Entity Configuration")
@allure.title("Column Mapping")
@pytest.mark.dependency(depends=["test_query_execution"])
def test_column_mapping():
    Entity.column_mapping()

@allure.feature("Entity Configuration")
@allure.title("Enum Mapping")
@pytest.mark.dependency(depends=["test_column_mapping"])
def test_enum_mapping():
    Entity.enum_mapping()

@allure.feature("Entity Configuration")
@allure.title("Publsih the Entity")
@pytest.mark.dependency(depends=["test_enum_mapping"])
def test_entity_publish():
    Entity.publish_entity()

# @pytest.mark.dependency(depends=["test_check_entity_configuration"])
def test_schedule():

    Schedule.schedule_ingestion()
    Schedule.sync_data()
    # Schedule.timzone_assert()


