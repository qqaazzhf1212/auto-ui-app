from page_objects.app.my_page import AppBasePage
from appium.webdriver.common.mobileby import MobileBy


class LoginPage(AppBasePage):
    name = '登录页面'
    mobile_input_loc = (MobileBy.ID, 'com.ddjk.client:id/mLoginPhonenumEt')
    clear_input_loc = (MobileBy.ID, 'com.ddjk.client:id/scanel')
    subimt_input_loc = (MobileBy.ID, 'com.ddjk.client:id/mLoginBtn')
    check_agreement_loc = (MobileBy.ID, 'com.ddjk.client:id/checkbox')

    argee_loc = (MobileBy.ID, "com.ddjk.client:id/tv_agree")
    enter_loc = (MobileBy.ID, "android:id/button1")
    picture_perssion_loc = (MobileBy.ID, "com.android.packageinstaller:id/permission_allow_button")
    tlak_perssion_loc = (MobileBy.ID, "com.android.packageinstaller:id/permission_allow_button")
    video_perssion_loc = (MobileBy.ID, "com.android.packageinstaller:id/permission_allow_button")

    gointoapp_loc = (MobileBy.ID, "com.ddjk.client:id/tv_agree")

    num1_loc = (MobileBy.ID, "com.ddjk.client:id/num_in1_et")
    num2_loc = (MobileBy.ID, "com.ddjk.client:id/num_in2_et")
    num3_loc = (MobileBy.ID, "com.ddjk.client:id/num_in3_et")
    num4_loc = (MobileBy.ID, "com.ddjk.client:id/num_in4_et")
    num5_loc = (MobileBy.ID, "com.ddjk.client:id/num_in5_et")
    num6_loc = (MobileBy.ID, "com.ddjk.client:id/num_in6_et")




    def login_perssion_manage(self):
        self.wait_element_is_visible(self.argee_loc, '同意进入幂健康').click_element()
        self.wait_element_is_visible(self.enter_loc, 'App权限获取').click_element()
        self.wait_element_is_visible(self.picture_perssion_loc, '图片权限获取').click_element()
        self.wait_element_is_visible(self.tlak_perssion_loc, '通讯录权限获取').click_element()
        self.wait_element_is_visible(self.video_perssion_loc, '录音权限获取').click_element()
        self.touch_swipe('left')
        self.wait_element_is_visible(self.gointoapp_loc, '进入App的登录页面').click_element()

    def login_app(self, mobile):
        '''
        登录功能
        '''
        self.wait_element_is_visible(self.mobile_input_loc, '输入手机号').input_text(mobile)
        self.wait_element_is_visible(self.check_agreement_loc, '勾选协议').click_element()
        self.wait_element_is_visible(self.subimt_input_loc, '点击获取验证码按钮').click_element()
        self.wait_element_is_visible(self.num1_loc, '输入按钮1').input_text(1)
        self.wait_element_is_visible(self.num2_loc, '输入按钮2').input_text(2)
        self.wait_element_is_visible(self.num3_loc, '输入按钮3').input_text(3)
        self.wait_element_is_visible(self.num4_loc, '输入按钮4').input_text(4)
        self.wait_element_is_visible(self.num5_loc, '输入按钮5').input_text(5)
        self.wait_element_is_visible(self.num6_loc, '输入按钮6').input_text(6)


    def close_login_page(self):
        '''
        关闭登录页面
        '''
        self.driver.close_app()
