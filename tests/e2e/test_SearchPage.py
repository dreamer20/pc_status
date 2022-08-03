from .pages.search_page import SearchPage
import pytest


def test_data_table_row_count(driver, app_root_url):
    ''' Checks if data table has correct row count '''
    search_page = SearchPage(driver, f'{app_root_url}/search')
    search_page.open()

    expected_row_count = 21
    actual_row_count = search_page.get_data_table_row_count()

    assert expected_row_count == actual_row_count, "Row count doesn'n match"


search_date_test_data = [
    ('2022-06-01', '2022-06-01', '2022.06.01', '2022.06.01', 6),
    ('2022-06-01', '', '2022.06.01', '2022.06.04', 21),
    ('2022-06-02', '', '2022.06.02', '2022.06.04', 15),
    ('', '', '2022.06.01', '2022.06.04', 21),
    ('', '2022-06-03', '2022.06.01', '2022.06.03', 16),
]


@pytest.mark.parametrize(
    "from_date, to_date, "
    "expected_first_row_date, "
    "expected_last_row_date, "
    "expected_row_count",
    search_date_test_data
)
def test_search_date_from_to(driver,
                             app_root_url,
                             from_date,
                             to_date,
                             expected_first_row_date,
                             expected_last_row_date,
                             expected_row_count):
    ''' Checks if selected range returns the correct results '''
    search_page = SearchPage(driver, f'{app_root_url}/search')
    search_page.open()

    search_page.select_date(from_date=from_date, to_date=to_date)
    search_page.click_search_button()
    search_page = SearchPage(driver, driver.current_url)

    actual_row_count = search_page.get_data_table_row_count()
    first_row = search_page.get_data_table_row('first')
    last_row = search_page.get_data_table_row('last')
    actual_first_row_date = search_page.get_data_table_column_from_row(first_row, 'first')
    actual_last_row_date = search_page.get_data_table_column_from_row(last_row, 'first')

    assert expected_first_row_date in actual_first_row_date, "Date count doesn't match"
    assert expected_last_row_date in actual_last_row_date, "Date count doesn't match"
    assert expected_row_count == actual_row_count, "Row count doesn'n match"
