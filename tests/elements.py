from selenium.webdriver.common.by import By

class BasePageInputElement(object):
    def __set__(self, obj, value):
        driver = obj.driver

        elem = driver.find_element(By.CSS_SELECTOR, self.locator)
        elem.clear()
        elem.send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        elem = driver.find_element(By.CSS_SELECTOR, self.locator)
        return elem.get_property('value') or elem.get_attribute('value')


class BasePageElement(object):
    def __get__(self, obj, owner):
        driver = obj.driver
        elem = driver.find_element(By.CSS_SELECTOR, self.locator)
        return elem.text


class DateInput(BasePageInputElement):
    def __init__(self, locator):
        self.locator = locator


class TableData(BasePageElement):
    def __init__(self, locator):
        self.locator = locator


class TableRow():
    date = TableData('td:first-child')
    cpu_temp = TableData('td:nth-child(2)')
    ssd_temp = TableData('td:nth-child(3)')
    disk_space = TableData('td:nth-child(4)')
    ram = TableData('td:nth-child(5)')
    process_count = TableData('td:nth-child(6)')
    uptime = TableData('td:nth-child(7)')
    cpu_fan = TableData('td:nth-child(8)')
    add_fan = TableData('td:nth-child(9)')
    volume_level = TableData('td:nth-child(10)')
    last_update = TableData('td:nth-child(11)')
    load_average = TableData('td:nth-child(12)')
    keyboard_layout = TableData('td:last-child')


    def __init__(self, driver):
        self.driver = driver


class DataTable():
    def __init__(self, driver, selector):
        self.driver = driver
        self.first_row = TableRow(self.driver.find_element(
            By.CSS_SELECTOR,
            f'{selector} tbody tr:first-child'))
        self.last_row = TableRow(self.driver.find_element(
            By.CSS_SELECTOR,
            f'{selector} tbody tr:last-child'))

    def get_row(self, nth_child):
        return TableRow(self.driver.find_element(
            By.CSS_SELECTOR,
            f'.data-table tbody tr:nth-child({nth_child})'))