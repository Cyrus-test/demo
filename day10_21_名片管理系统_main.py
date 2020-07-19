# for 循环是遍历列表
# while true 可以不停的循环，无限循环

while True:

    action_str = input("请选择希望执行的操作： ")

    print("您选择的操作是：【%s】" % action_str)

    # 1,2,3 针对名片的操作
    if action_str in ["1", "2", "3"]:

        pass


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