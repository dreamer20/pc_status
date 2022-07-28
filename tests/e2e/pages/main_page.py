from .base_page import BasePage
from .locators import MainPageLocators as MP_locators


class MainPage(BasePage):
    def has_cur_date_link(self):
        return self.is_element_present(MP_locators.CUR_DATE_LINK)

    def get_cur_date(self):
        date_link = self.driver.find_element(MP_locators.CUR_DATE_LINK)
        date = date_link.text()

        return date

    def get_cur_time(self):
        datetime = self.driver.find_element(MP_locators.CUR_DATE).text()
        time = datetime.split(' ')[2]

        return time
