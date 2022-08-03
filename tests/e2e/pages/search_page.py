from .base_page import BasePage
from .locators import SearchPageLocators as SP_locators
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    def select_date(self, from_date=None, to_date=None):
        if from_date is not None:
            from_date_input = self.driver.find_element(
                *SP_locators.FROM_DATE_INPUT
            )
            from_date_input.clear()
            from_date_input.send_keys(from_date)

        if to_date is not None:
            to_date_input = self.driver.find_element(*SP_locators.TO_DATE_INPUT)
            to_date_input.clear()
            to_date_input.send_keys(to_date)

    def click_search_button(self):
        search_button = self.driver.find_element(*SP_locators.SEARCH_BUTTON)
        search_button.click()

    def get_data_table_row(self, row_index):
        data_table = self.driver.find_element(*SP_locators.DATA_TABLE)

        if row_index == 'first':
            row = data_table.find_element(By.CSS_SELECTOR, 'tr:first-child')
        elif row_index == 'last':
            row = data_table.find_element(By.CSS_SELECTOR, 'tr:last-child')
        else:
            row = data_table.find_element(
                By.CSS_SELECTOR,
                f'tr:nth-child({str(row_index)})'
            )

        return row

    def get_data_table_column_from_row(self, row, column_index):
        if column_index == 'first':
            column = row.find_element(By.CSS_SELECTOR, 'td:first-child')
        elif column_index == 'last':
            column = row.find_element(By.CSS_SELECTOR, 'td:last-child')
        else:
            column = row.find_element(
                By.CSS_SELECTOR,
                f'td:nth-child({str(column_index)})'
            )
        print(column)
        return column.text

    def get_data_table_row_count(self):
        rows = self.driver.find_elements(*SP_locators.DATA_TABLE_ROWS)

        return len(rows)
