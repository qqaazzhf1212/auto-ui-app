from page_objects.app.app_base_page import AppBasePage
from appium.webdriver.common.mobileby import MobileBy

class NavigationPage(AppBasePage):
    name = '导航栏'


    def switch_to_navigation(self,nav_name):
        '''
        切换到名字为nav_name的页面
        '''
        if nav_name=='主页':
            pass
        elif nav_name=='社区':
            pass
        elif nav_name == '商城':
            pass
        elif nav_name == '我的':
            pass
        else:
            raise ValueError('没有这个菜单')