from elements import DataTable, DateInput
from selenium.webdriver.common.by import By


class MainPage():
    def __init__(self, driver):
        def find(selector, selector_type=By.CSS_SELECTOR):
            return driver.find_element(selector_type, selector)

        self.driver = driver
        self.title = find('.title')
        self.cur_date_link = find('.cur-date a')
        self.cur_datetime = find('.cur-date span')
        self.data = {
            'cpu_temp': find('.status-table__col:first-child \
                                .status-table__row:first-child span'),
            'ssd_temp': find(".status-table__col:first-child \
                                .status-table__row:nth-child(2) span"),
            'disk_space': find(".status-table__col:first-child \
                                    .status-table__row:nth-child(3) span"),
            'ram': find(".status-table__col:first-child \
                            .status-table__row:nth-child(4) span"),
            'process_count': find(".status-table__col:first-child \
                                    .status-table__row:nth-child(5) span"),
            'uptime': find(".status-table__col:first-child \
                                .status-table__row:nth-child(6) span"),
            'cpu_fan': find(".status-table__col:last-child \
                                .status-table__row:first-child span"),
            'add_fan': find(".status-table__col:last-child \
                                .status-table__row:nth-child(2) span"),
            'volume_level': find(".status-table__col:last-child \
                                    .status-table__row:nth-child(3) span"),
            'last_update': find(".status-table__col:last-child \
                                    .status-table__row:nth-child(4) span"),
            'load_average': find(".status-table__col:last-child \
                                    .status-table__row:nth-child(5) span"),
            'keyboard_layout': find(".status-table__col:last-child \
                                    .status-table__row:nth-child(6) span"),
        }
        self.menu = {
            'MainPage': find(".menu a[href='/']"),
            'SearchPage': find(".menu a[href='/search/']")
        }

    def get_data(self, data):
        return self.data[data].text

    def get_cur_datetime(self):
        return self.cur_datetime.text

    def get_title(self):
        return self.title.text

    def get_search_link_for_cur_date(self):
        return self.cur_date_link.get_attribute('href')

    def to_MainPage(self):
        self.menu['MainPage'].click()
        return MainPage(self.driver)

    def to_SearchPage(self):
        self.menu['SearchPage'].click()
        return SearchPage(self.driver)


class SearchPage():
    from_date = DateInput("input[name='from_date']")
    to_date = DateInput("input[name='to_date']")

    def __init__(self, driver):
        def find(selector, selector_type=By.CSS_SELECTOR):
            return driver.find_element(selector_type, selector)

        self.driver = driver
        self.title = self.driver.find_element(By.CSS_SELECTOR, '.title')
        self.submitButton = self.driver.find_element(
            By.CSS_SELECTOR,
            "input[type='submit'")
        self.table = DataTable(self.driver, '.data-table')
        self.menu = {
            'MainPage': find(".menu a[href='/']"),
            'SearchPage': find(".menu a[href='/search/']")
        }

    def get_title(self):
        return self.title.text

    def submit(self):
        self.submitButton.click()
        return SearchPage(self.driver)

    def to_MainPage(self):
        self.menu['MainPage'].click()
        return MainPage(self.driver)

    def to_SearchPage(self):
        self.menu['SearchPage'].click()
        return SearchPage(self.driver)
