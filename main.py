import pytest

import settings
from common.tools import get_opts

if __name__ == '__main__':
    args = ['-s', '-v', '--clean-alluredir', '--alluredir=results/reports', settings.TEST_APP_CASE_DIR]

    arg = get_opts('-m')
    if arg:
        args.insert(0, '-m {}'.format(arg))

    arg = get_opts('--appium_port')
    if arg:
        args.insert(0, '--appium_port={}'.format(arg))

    arg = get_opts('--udid')
    if arg:
        args.insert(0, '--udid={}'.format(arg))
    print(args)
    pytest.main(args)
