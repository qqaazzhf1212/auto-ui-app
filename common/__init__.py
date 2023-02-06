from .handler_log import get_logger
import settings

# 初始化log，可以直接使用，单例模式
logger = get_logger(**settings.LOG_CONFIG)

# 初始化db，可以直接使用，单例模式

