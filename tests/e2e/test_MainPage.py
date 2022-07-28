from .pages.main_page import MainPage
from .pages.search_page import SearchPage


def test_MainPage_has_cur_date_link(driver, app_root_url):
    ''' Checks if MainPage has current date link '''
    main_page = MainPage(driver, app_root_url)
    main_page.open()

    assert main_page.has_cur_date_link(), 'Current date link is not present'


def test_user_can_go_to_SearchPage(driver, app_root_url):
    ''' Checks if user can go from MainPage to SearchPage '''
    main_page = MainPage(driver, app_root_url)
    main_page.open()

    main_page.to_search_page()
    search_page = SearchPage(driver, driver.current_url)

    assert search_page.url == f'{app_root_url}/search/', "Link doesn't lead to SearchPage"
