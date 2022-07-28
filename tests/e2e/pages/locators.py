from selenium.webdriver.common.by import By


class BasePageLocators:
    SEARCH_PAGE_LINK = (By.CSS_SELECTOR, ".menu a[href='/search/']")


class MainPageLocators:
    CUR_DATE_LINK = (By.CSS_SELECTOR, ".cur-date a")
    CUR_DATE = (By.CSS_SELECTOR, ".cur-date span")


class SearchPageLocators:
    FROM_DATE_INPUT = (By.CSS_SELECTOR, ".search-form__input[name='from_date']")
    TO_DATE_INPUT = (By.CSS_SELECTOR, ".search-form__input[name='to_date']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".search-form__submit")
    DATA_TABLE = (By.CSS_SELECTOR, ".data-table tbody")
    DATA_TABLE_ROWS = (By.CSS_SELECTOR, ".data-table tbody tr")
