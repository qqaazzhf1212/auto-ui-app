fail_cases = [
    {
        'title': '用户名为空',
        'request_data': {'mobile': ''}
    },
    {
        'title': '短信验证码为空',
        'request_data': {'mobile': '18071750873', 'password': ''}
    },
    {
        'title': '手机号长度不正确',
        'request_data': {'mobile': 1807175087312}
    },
]
success_cases = [
    {
        'title': '正常登录',
        'request_data': {'mobile': 18071750873}
    }
]


