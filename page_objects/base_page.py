import csv
import os
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common import logger
import settings


class BasePage:
    '''
    页面类的基类
    1、查找元素  等待--查找
    2、点击   等待--查找---点击
    3、输入    等待--查找--输入
    4、获取元素文本  等待--查找--获取文本
    5、获取元素属性  等待--查询--获取属性
    6、窗口切换
    7、失败截图
    '''
    name = 'base页面'
    logger = logger
    settings = settings

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.locator = None
        self.action = ''
        self.element = None

    # 延时操作
    def delay(self, second=0.5):
        '''
        延时操作
        second:支持浮点数
        :return:
        '''
        time.sleep(second)
        return self

    # 等待单个XX元素可见
    def wait_element_is_visible(self, locator, action='', **kwargs):
        '''
        等待元素可见
        :param locator: 定位信息
        :param action:  操作说明
        :param kwargs: timeout poll_frequency
        :return:
        '''
        # 传递locator和locator给下一个动作
        self.locator = locator
        self.locator = action

        try:
            timeout = kwargs.get('timeout', self.settings.DEFAULT_TIOMEOUT)
            poll_frequency = kwargs.get('poll_frequency', 0.5)
            self.element = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
                EC.visibility_of_element_located(locator)
            )
        except Exception as e:
            self.logger.exception(
                '在{}，{}操作的时候，等待{}元素可见【失败】'.format(self.name, action, locator)
            )
            # 失败了保存当前截图
            self.get_page_screenshot(action)
            raise e
        else:
            self.logger.info(
                '在{}，{}操作的时候，等待{}元素可见【成功】'.format(self.name, action, locator)
            )
            return self

    # 等待元素加载到dom中
    def wait_element_is_presence(self, locator, action='', **kwargs):
        '''
        等待元素加载到dom中
        :param locator: 定位信息
        :param action:  操作说明
        :param kwargs: timeout poll_frequency
        :return:
        '''
        # 传递locator和locator给下一个动作
        self.locator = locator
        self.locator = action

        try:
            timeout = kwargs.get('timeout', self.settings.DEFAULT_TIOMEOUT)
            poll_frequency = kwargs.get('poll_frequency', 0.5)
            self.element = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
                EC.presence_of_element_located(locator)
            )
        except Exception as e:
            self.logger.exception(
                '在{}，{}操作的时候，等待{}加载到dom中【失败】'.format(self.name, action, locator)
            )
            # 失败了保存当前截图
            self.get_page_screenshot(action)
            raise e
        else:
            self.logger.info(
                '在{}，{}操作的时候，等待{}加载到dom中【成功】'.format(self.name, action, locator)
            )
            return self

    # 等待多个XX元素可见
    def wait_elements_is_visible(self, locator, action='', **kwargs):
        '''
        等待元素可见
        :param locator: 定位信息
        :param action:  操作说明
        :param kwargs: timeout poll_frequency
        :return:
        '''
        # 传递locator和locator给下一个动作
        self.locator = locator
        self.locator = action

        try:
            timeout = kwargs.get('timeout', self.settings.DEFAULT_TIOMEOUT)
            poll_frequency = kwargs.get('poll_frequency', 0.5)
            self.element = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except Exception as e:
            self.logger.exception(
                '在{}，{}操作的时候，等待{}元素可见【失败】'.format(self.name, action, locator)
            )
            # 失败了保存当前截图
            self.get_page_screenshot(action)
            raise e
        else:
            self.logger.info(
                '在{}，{}操作的时候，等待{}元素可见【成功】'.format(self.name, action, locator)
            )
            return self

    # 截图
    def get_page_screenshot(self, action):
        # 命令规范: {XX时间_XX页面_XX操作}_截图时间.png
        cur_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        img_path = os.path.join(self.settings.SCREENSHOT_DIR, "{}_{}_{}.png".format(cur_time, self.name, action))
        if self.driver.save_screenshot(img_path):
            logger.info("生成错误截图：{}【成功】".format(img_path))
        else:
            logger.info("生成错误截图：{}【失败】".format(img_path))

    # 输入数据
    def input_text(self, content):
        '''
        输入字符串
        :return:
        '''
        if self.element is None:
            raise RuntimeError('不能在wait方法之前调用元素上的方法')
        try:
            self.element.clear()
            self.element.send_keys(content)
        except Exception as e:
            self.logger.exception(
                '在{}，{}操作的时候，对{}元素输入{}【失败】'.format(self.name, self.action, self.locator, content)
            )
            # 失败了保存当前截图
            self.get_page_screenshot(self.action)
            raise e
        else:
            self.logger.info(
                '在{}，{}操作的时候，对{}元素输入{}【成功】'.format(self.name, self.action, self.locator, content)
            )
        finally:
            self.__clear_cache()

    # 点击元素
    def click_element(self):
        '''
        点击元素
        :return:
        '''
        if self.element is None:
            raise RuntimeError('不能在wait方法之前调用元素上的方法')
        try:
            self.element.click()
        except Exception as e:
            self.logger.exception(
                '在{}，{}操作的时候，点击{}元素【失败】'.format(self.name, self.action, self.locator)
            )
            # 失败了保存当前截图
            self.get_page_screenshot(self.action)
            raise e
        else:
            self.logger.info(
                '在{}，{}操作的时候，点击{}元素【成功】'.format(self.name, self.action, self.locator)
            )
        finally:
            self.__clear_cache()

    # 通过js触发点击事件
    def click_element_by_js(self):
        '''
        通过js点击元素
        '''
        if self.element is None:
            raise RuntimeError('不能在wait方法之前调用元素上的方法')
        try:
            self.driver.execute_script('arguments[0].click()',self.element)
        except Exception as e:
            self.logger.exception(
                '在{}，{}操作的时候，点击{}元素【失败】'.format(self.name, self.action, self.locator)
            )
            # 失败了保存当前截图
            self.get_page_screenshot(self.action)
            raise e
        else:
            self.logger.info(
                '在{}，{}操作的时候，点击{}元素【成功】'.format(self.name, self.action, self.locator)
            )
        finally:
            self.__clear_cache()


    # 获取driver
    def get_elenmet(self):
        if self.element is None:
            raise RuntimeError('不能在wait方法之前调用元素上的方法')

        return self.element

    # 获取元素的属性
    def get_elenmet_attr(self, name):
        '''
        :param name:获取元素的属性
        :return:
        '''
        if self.element is None:
            raise RuntimeError('不能在wait方法之前调用元素上的方法')
        try:
            value = self.element.get_attribute(name)
        except Exception as e:
            self.logger.exception(
                '在{}，{}操作的时候，获取{}元素{}属性【失败】'.format(self.name, self.action, self.locator, name)
            )
            # 失败了保存当前截图
            self.get_page_screenshot(self.action)
            raise e
        else:
            self.logger.info(
                '在{}，{}操作的时候，获取{}元素{}属性【成功】'.format(self.name, self.action, self.locator, name)
            )
            return value
        finally:
            self.__clear_cache()

    # 获取元素的文本信息
    def get_elenmet_attribute(self,name):
        '''
        :return:
        '''
        if self.element is None:
            raise RuntimeError('不能在wait方法之前调用元素上的方法')
        try:
            value = self.element.get_attribute(name)
        except Exception as e:
            self.logger.exception(
                '在{}，{}操作的时候，获取{}元素的文本信息【失败】'.format(self.name, self.action, self.locator)
            )
            # 失败了保存当前截图
            self.get_page_screenshot(self.action)
            raise e
        else:
            self.logger.info(
                '在{}，{}操作的时候，获取{}元素的文本信息【成功】'.format(self.name, self.action, self.locator)
            )
            return value
        finally:
            self.__clear_cache()
    # 获取元素的文本信息
    def get_elenmet_text(self):
        '''
        :return:
        '''
        if self.element is None:
            raise RuntimeError('不能在wait方法之前调用元素上的方法')
        try:
            value = self.element.text
        except Exception as e:
            self.logger.exception(
                '在{}，{}操作的时候，获取{}元素的文本信息【失败】'.format(self.name, self.action, self.locator)
            )
            # 失败了保存当前截图
            self.get_page_screenshot(self.action)
            raise e
        else:
            self.logger.info(
                '在{}，{}操作的时候，获取{}元素的文本信息【成功】'.format(self.name, self.action, self.locator)
            )
            return value
        finally:
            self.__clear_cache()

    # 切换到新的窗口
    def switch_to_new_window(self, handle=None, action=''):
        '''
        :return:
        '''
        try:
            if handle:
                self.driver.switch_to.window(handle)
            else:
                old_window = self.driver.current_window_handle
                for handle in self.driver.window_handles:
                    if handle != old_window:
                        self.driver.switch_to.window(handle)
                        break

        except Exception as e:
            self.logger.exception(
                '在{}，{}操作的时候，切换到窗口{}【失败】'.format(self.name, self.action, handle)
            )
            # 失败了保存当前截图
            self.get_page_screenshot(self.action)
            raise e
        else:
            self.logger.info(
                '在{}，{}操作的时候，切换到窗口{}【成功】'.format(self.name, self.action, handle)
            )

    # 获取csv的数据
    def get_csv_data(self, csv_file, line):
        self.logger.info('=======获取csv的数据=========')
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

    # 清除缓存
    def __clear_cache(self):
        '''
        情况wait的缓存
        :return:
        '''
        self.locator = None
        self.action = ''
        self.element = None


