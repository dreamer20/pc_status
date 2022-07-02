from datetime import datetime
from pages import MainPage, SearchPage
from constants import URL_ROOT


last_record_in_database = {
    'cur_date': 1654345800.0,
    'cpu_temp': 50.9,
    'ssd_temp': 34.9,
    'cpu_fan': 2106,
    'add_fan': 868,
    'ram_total': 16310072,
    'ram_available': 13209540,
    'disk_space_total': 29,
    'disk_space_available': 9.1,
    'uptime': '27',
    'load_average': '0,03 0,19 0,27',
    'last_update': '2022-06-06 20:42:44',
    'volume_level': 58,
    'process_count': 306,
    'keyboard_layout': 'us'
}


def test_index(driver):
    driver.get(URL_ROOT)

    assert driver.title == 'Index page'


def test_MainPage(driver):
    expected_url = f'{URL_ROOT}/search/?from_date=2022-06-04&to_date=2022-06-04'
    expected_datetime = datetime.fromtimestamp(1654345800.0).strftime(
        "%Y.%m.%d в %H:%M")
    driver.get(URL_ROOT)
    main_page = MainPage(driver)

    assert main_page.get_cur_datetime() == expected_datetime
    assert (main_page.get_data('cpu_temp')
            == f"{last_record_in_database['cpu_temp']}℃")
    assert (main_page.get_data('ssd_temp')
            == f"{last_record_in_database['ssd_temp']}℃")
    assert (main_page.get_data('cpu_fan')
            == f"{last_record_in_database['cpu_fan']} RPM")
    assert (main_page.get_data('add_fan')
            == f"{last_record_in_database['add_fan']} RPM")
    assert (f"{last_record_in_database['ram_total']} KB /"
            in main_page.get_data('ram'))
    assert (f"{last_record_in_database['ram_available']} KB"
            in main_page.get_data('ram'))
    assert (f"{last_record_in_database['disk_space_total']} GB /"
            in main_page.get_data('disk_space'))
    assert (f"{last_record_in_database['disk_space_available']} GB"
            in main_page.get_data('disk_space'))
    assert (main_page.get_data('uptime')
            == f"{last_record_in_database['uptime']} мин.")
    assert (main_page.get_data('load_average')
            == f"{last_record_in_database['load_average']}")
    assert (main_page.get_data('volume_level')
            == f"{last_record_in_database['volume_level']}%")
    assert (main_page.get_data('process_count')
            == f"{last_record_in_database['process_count']}")
    assert (main_page.get_data('keyboard_layout')
            == f"{last_record_in_database['keyboard_layout']}")
    assert main_page.get_search_link_for_cur_date() == expected_url
    assert main_page.get_title() == 'Статус ПК'


def test_menu_link(driver):
    driver.get(URL_ROOT)
    main_page = MainPage(driver)

    search_page = main_page.to_SearchPage()
    assert search_page.driver.current_url == f'{URL_ROOT}/search/'

    main_page = search_page.to_MainPage()
    assert main_page.driver.current_url == f'{URL_ROOT}/'


def test_SearchPage(driver):
    driver.get(F'{URL_ROOT}/search/')
    search_page = SearchPage(driver)

    assert search_page.get_title() == 'Поиск данных'

    search_page.from_date = '2022-06-02'
    search_page.to_date = '2022-06-03'
    assert search_page.from_date == '2022-06-02'
    search_page = search_page.submit()
    assert '2022.06.02 00:00' in search_page.table.first_row.date
    assert '2022.06.03 12:30' in search_page.table.last_row.date
    assert '58%' in search_page.table.last_row.volume_level
    assert 'us' in search_page.table.last_row.keyboard_layout
    assert '2022.06.02 01:00' in search_page.table.get_row(3).date
