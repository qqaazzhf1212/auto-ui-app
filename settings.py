import os

# --------------------------全局-------------------------
# 根项目目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ------------------------app---------------------------
# APP测试用例路径
TEST_APP_CASE_DIR = os.path.join(BASE_DIR, 'test_cases/app')
# print(TEST_APP_CASE_DIR)

# 错误图片位置
SCREENSHOT_DIR = os.path.join(BASE_DIR, 'results/screenshot/app')

# App的host
APPIUM_SERVER_HOST = 'http://127.0.0.1:4723/wd/hub'

# App的配置
DES_CAPS = {
    'platformName': 'Android',
    'platformVersion': '6.0',
    'deviceName': '127.0.0.1:7555',
    'appname': 'kaoyan3.1.0.apk',
    'appPackage': 'com.ddjk.client',
    # 'appPackage': 'com.tal.kaoyan',
    # 'appActivity': 'com.tal.kaoyan.ui.activity.SplashActivity',
    'appActivity': 'com.jk.modulelogin.activitys.SplashActivity',
    'noRest': 'False',
    # 'chromedriverExecutable': os.path.join(BASE_DIR, 'drivers', 'chromedriver_103.exe'),
    # 'newCommandTimeout': '3000',
    'unicodeKeyboard': 'true',
    'resetKeyboard': 'true'
}

# App的测试号码
TEST_NORMAL_MOBILE = 18071750873

# --------------------web----------------------
# 项目域名
PROJECT_HOST = 'http://zhushuju.test.jk.com/'

# 登录配置
INTESTFACE = {
    'login': 'login'
}

# 日志配置
LOG_CONFIG = {
    'name': 'pyui',
    'filename': os.path.join(BASE_DIR, 'results/logs/pyui.log'),
    'mode': 'a',
    'encoding': 'utf-8',
    'debug': True
}

# 账号信息
TEST_NORMAL_USERNAME = 'admin'
TEST_NORMAL_PASSWRRD = 123456

# 全局查找元素等等时间
DEFAULT_TIOMEOUT = 5

BROWSER_DRIVER = {
    'chrome': os.path.join(BASE_DIR, 'drivers', 'chromedriver_103.exe'),
    'firefox': os.path.join(BASE_DIR, 'drivers', 'geckodriver_102.exe'),
    'edge': os.path.join(BASE_DIR, 'drivers', 'msedgedriver_103.exe')
}

# =========================app==========================
