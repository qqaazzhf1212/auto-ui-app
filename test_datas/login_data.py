import pytest

success_cases = [
    {
        'title': '登录成功',
        'request_data': {'username': 'admin', 'password': 123456}
    }

]

# 只执行这一条用例
# success_cases[0] = pytest.param(success_cases[0], marks=pytest.mark.first)

fail_cases = [
    {
        'title': '登录失败',
        'request_data': {'username': '', 'password': 123456},
        'error_tip': '用户名不能为空'
    },
    {
        'title': '登录失败',
        'request_data': {'username': 'admin', 'password': ''},
        'error_tip': '密码不能为空'
    }
]
