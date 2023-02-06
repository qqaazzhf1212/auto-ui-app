from common import logger
import settings


class BaseCase:
    # 测试套的名称
    name = None
    logger = logger
    settings = settings

    # xunit风格的前置
    @classmethod
    def setup_class(cls):
        cls.logger.info('============{}测试开始============='.format(cls.name))

    # xunit风格的后置
    @classmethod
    def teardown_class(cls):
        cls.logger.info('============{}测试结束============='.format(cls.name))
