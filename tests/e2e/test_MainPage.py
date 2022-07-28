from .pages.main_page import MainPage
from .pages.search_page import SearchPage

URL_ROOT = 'http://localhost:5000'


def test_MainPage_has_cur_date_link(driver):
    ''' Checks if MainPage has current date link '''
    main_page = MainPage(driver, URL_ROOT)
    main_page.open()

    assert main_page.has_cur_date_link(), 'Current date link is not present'


def test_user_can_go_to_SearchPage(driver):
    ''' Checks if user can go from MainPage to SearchPage '''
    main_page = MainPage(driver, URL_ROOT)
    main_page.open()

    main_page.to_search_page()
    search_page = SearchPage(driver, driver.current_url)

    assert search_page.url == f'{URL_ROOT}/search/', "Link doesn't lead to SearchPage"
