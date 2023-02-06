from page_objects.app.my_page import AppBasePage
from appium.webdriver.common.mobileby import MobileBy


class HomePage(AppBasePage):
    name = 'home页面'

    home_loc = (MobileBy.ID, "com.ddjk.client:id/tv_title_sub")

    def home_assert_page(self):
        return self.wait_element_is_visible(self.home_loc, '首页tab').get_elenmet_attribute('text')
