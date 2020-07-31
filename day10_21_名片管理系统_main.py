#！ C:\Users\86159\AppData\Local\Microsoft\WindowsApps\python3

import day11_22_名片管理系统_tools

# for 循环是遍历列表
# while true 可以不停的循环，无限循环

while True:
    # 显示功能菜单
    day11_22_名片管理系统_tools.show_menu()
    action_str = input("请选择希望执行的操作： ")

    print("您选择的操作是：【%s】" % action_str)

    # 1,2,3 针对名片的操作
    if action_str in ["1", "2", "3"]:
        # 新增名片
        if action_str == "1":
            day11_22_名片管理系统_tools.new_card()

        # 显示全部
        elif action_str == "2":
            day11_22_名片管理系统_tools.show_all()
        # 查询名片
        elif action_str == "3":
            day11_22_名片管理系统_tools.search_card()

    # 0 退出系统

    elif action_str in ["0"]:
        print("欢迎再次使用【名片管理系统】")
        break
        # 如果在开发程序是，不希望立刻编写分支内部的代码，可以使用pass 关键字，表示一个占位符，
        # 能够保持程序代码的结构正确，程序运行时，pass运算符不进行任何操作
        # pass

    # 其他数据输入错误，需要提示用户重新输入

    else:
        print("您输入的不正确，请重新输入")