import pytest
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

# Login
def test_login():
    login.login_functionality()

# Data Source CRUD Operations
@pytest.mark.skip
def test_datasource():
    ds.datasource_tab()
    ds.add_csv_datasource()
    ds.add_banner_datasource()
    ds.check_connection()
    ds.edit_datasource()
    ds.delete_datasource()


# Entity Configurations
@pytest.mark.dependency()
@pytest.mark.xfail(reason="Entity Cannot be reset when ingestion is in progress")
def test_check_entity_configuration():
    Entity.entity_dashboard()
    Entity.entity_manage_button()
    Entity.entity_configured_or_not()


@pytest.mark.dependency(depends=["test_check_entity_configuration"])
def test_entity_configuration():
    Entity.choose_datasource()
    Entity.placeholder_query()
    Entity.execute_query()
    Entity.column_mapping()
    Entity.enum_mapping()
    Entity.publish_entity()

@pytest.mark.dependency(depends=["test_check_entity_configuration()"])
def test_schedule():

    Schedule.schedule_ingestion()
    Schedule.sync_data()
    # Schedule.timzone_assert()


