from .pages.search_page import SearchPage


def test_data_table_row_count(driver, app_root_url):
    ''' Checks if data table has correct row count '''
    search_page = SearchPage(driver, f'{app_root_url}/search')
    search_page.open()

    expected_row_count = 21
    actual_row_count = search_page.get_data_table_row_count()

    assert expected_row_count == actual_row_count, "Row count doesn'n match"


def test_data_table_row_count2(driver, app_root_url):
    ''' Checks if data table has correct row count '''
    search_page = SearchPage(driver, f'{app_root_url}/search')
    search_page.open()

    expected_row_count = 21
    actual_row_count = search_page.get_data_table_row_count()

    assert expected_row_count == actual_row_count, "Row count doesn'n match"


def test_data_table_row_coun3(driver, app_root_url):
    ''' Checks if data table has correct row count '''
    search_page = SearchPage(driver, f'{app_root_url}/search')
    search_page.open()

    expected_row_count = 21
    actual_row_count = search_page.get_data_table_row_count()

    assert expected_row_count == actual_row_count, "Row count doesn'n match"


def test_data_table_row_count4(driver, app_root_url):
    ''' Checks if data table has correct row count '''
    search_page = SearchPage(driver, f'{app_root_url}/search')
    search_page.open()

    expected_row_count = 21
    actual_row_count = search_page.get_data_table_row_count()

    assert expected_row_count == actual_row_count, "Row count doesn'n match"


def test_data_table_row_count5(driver, app_root_url):
    ''' Checks if data table has correct row count '''
    search_page = SearchPage(driver, f'{app_root_url}/search')
    search_page.open()

    expected_row_count = 21
    actual_row_count = search_page.get_data_table_row_count()

    assert expected_row_count == actual_row_count, "Row count doesn'n match"
