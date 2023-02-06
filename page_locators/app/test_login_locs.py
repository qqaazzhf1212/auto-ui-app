from appium.webdriver.common.mobileby import MobileBy


class LoginPageLocator:
    '''
    页面的定位信息
    '''
    # 用户名输入框

    # 密码输入框

    # 登陆按钮

    # 登陆区域的提示框
    login_password_tips = ('css selector', '.el-form-item__error')
    mobile_input_loc = (MobileBy.ID, 'com.ddjk.client:id/mLoginPhonenumEt')
    clear_input_loc = (MobileBy.ID, 'com.ddjk.client:id/scanel')
    subimt_input_loc = (MobileBy.ID, 'com.ddjk.client:id/fl_base_cover')
    check_agreement_loc = (MobileBy.ID, 'com.ddjk.client:id/checkbox')




