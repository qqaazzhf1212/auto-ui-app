class LoginPageLocator:
    '''
    页面的定位信息
    '''
    # 用户名输入框
    username_intut_locator = ('xpath', '//input[@type="text"]')
    # 密码输入框
    password_intut_locator = ('xpath', '//input[@type="password"]')
    # 登陆按钮
    login_btn_locator = ('xpath', '//span[text()="登 录"]')
    # 登陆区域的提示框
    login_password_tips = ('css selector', '.el-form-item__error')


class HomePageLocators:
    Home_info_locator = ('xpath', '//span[text()="首页"]')
