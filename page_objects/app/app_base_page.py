from page_objects.base_page import BasePage


class AppBasePage(BasePage):
    name = 'app base 页面'

    # 获取设备大小
    def get_device_size(self):
        size = self.driver.get_window_size()
        return size['width'], size['height']

    # 获取错误信息
    # def get_toat_msg(self):
    #     '''
    #     获取错误信息
    #     '''
    #     loc = ("xpath", '//*[contains(@text,"{}")]'.format('手机号码不能为空'))
    #     action = '获取toast信息'
    #     msg = None
    #     try:
    #         msg = self.wait_element_is_presence(loc, action).get_elenmet_attr('text')
    #         print(msg)
    #     except Exception as e:
    #         raise e
    #     else:
    #         return msg

    # 滑动操作
    def touch_swipe(self, direction, distance=100):
        '''
        滑动操作
        direction:方向
        distance：距离
        '''
        width, height = self.get_device_size()
        if direction == 'up':
            start_x = width // 2
            start_y = height * 8 // 10
            end_x = start_x
            end_y = start_y - distance
        elif direction == 'down':
            start_x = width // 2
            start_y = height * 2 // 10
            end_x = start_x
            end_y = start_y + distance
        elif direction == 'left':
            start_x = width * 8 // 10
            start_y = height // 2
            end_x = start_x - distance
            end_y = start_y
        elif direction == 'right':
            start_x = width * 2 // 10
            start_y = height // 2
            end_x = start_x + distance
            end_y = start_y
        else:
            raise ValueError('请传入正确的方向字符串参数,up,down,left,right')
        self.driver.swipe(start_x, start_y, end_x, end_y, duration=500)

    # 切换原生和webview
    def switch_to_webview(self, webview_name):
        '''
        切换原生和webview
        '''
        contexts = self.driver.contexts
        if webview_name in contexts:
            self.driver.switch_to.context(webview_name)
        else:
            self.logger.warning('webview:{}没有找到'.format(webview_name))

    # 检查按钮是否存在
    def check_cancelBtn(self, cancelBtn):
        self.logger.info('==========检查是否发现{}按钮========='.format(cancelBtn))
        try:
            cancelBtn = self.driver.find_element(cancelBtn)
        except Exception:
            self.logger.info('==========没有发现{}按钮========='.format(cancelBtn))
        else:
            self.logger.info('============发现{}按钮=============='.format(cancelBtn))
            cancelBtn.click()


# if __name__ == '__main__':
#     from appium import webdriver
#
#     desired_caps = {
#         'platformName': 'Android',
#         'platformVersion': '6.0',
#         'deviceName': '127.0.0.1:7555',
#         'appPackage': 'com.tal.kaoyan',
#         'appActivity': 'com.tal.kaoyan.ui.activity.SplashActivity',
#         'noRest': 'true',
#         'newCommandTimeout': '300'
#     }
#
#     driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=desired_caps)
#     page = AppBasePage(driver)
#     from selenium.webdriver.common.by import By
#     cancelBtn = (By.ID, 'android:id/button2')
#     page.check_cancelBtn(cancelBtn)
