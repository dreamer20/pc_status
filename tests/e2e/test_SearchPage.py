from .pages.search_page import SearchPage

URL_ROOT = 'http://localhost:5000/search/'


def test_data_table_row_count(driver):
    ''' Checks if data table has correct row count '''
    search_page = SearchPage(driver, URL_ROOT)
    search_page.open()

    expected_row_count = 21
    actual_row_count = search_page.get_data_table_row_count()

    assert expected_row_count == actual_row_count, "Row count doesn'n match"
