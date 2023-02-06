import pytest

from test_cases.base_case import BaseCase
from test_datas.app.login_data import success_cases
from page_objects.app.login_page import LoginPage
from page_objects.app.home_page import HomePage

class TestLogin(BaseCase):
    name = '登录功能'

    @pytest.mark.parametrize('case', success_cases)
    def test_login_success(self, driver, case):
        self.logger.info('=========={}开始测试============'.format(case['title']))
        # 1、登录
        lp = LoginPage(driver)
        lp.login_perssion_manage()
        lp.login_app(**case['request_data'])
        # 3、获取错误信息断言
        try:
            assert '给你指数级健康呵护' == HomePage(driver).home_assert_page()
        except Exception as e:
            raise e
        finally:
        # 4、关闭登录页面
            lp.close_login_page()

    # @pytest.mark.parametrize('case', fail_cases)
    # def test_login_success(self, driver, case):
    #     self.logger.info('=========={}开始测试============'.format(case['title']))
    #     # 1、进入登录页面
    #     mp = MyPage(driver)
    #     mp.enter_login_page()
    #     # 2、登录
    #     lp = LoginPage(driver)
    #     lp.login(**case['request_data'])
    #     # 3、获取错误信息断言
    #     try:
    #         assert case['error_msg'] == lp.get_toat_msg()
    #     except Exception as e:
    #         raise e
    #     finally:
    #         # 4、关闭登录页面
    #         lp.close_login_page()
