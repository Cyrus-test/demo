from distutils.core import setup

setup(name="day_67_message", # 包名
    version="1.0", # 版本
    description="发送和接收模块" # 描述信息
    long_description="完整的发送和接收消息模块"# 完整描述信息
    author="cyrus"# 作者
    author_email="402879338@qq.com"#作者邮箱
    url="www.baidu.com"#
    py_modules=["day67_message.send_message",
                "day67_message.receive_message"]# )
