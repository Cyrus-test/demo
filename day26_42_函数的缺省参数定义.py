def print_info(name, gender=True):
    """

    :param name:班上同学的姓名
    :param gender:True是男生，false女生
    """

    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s 是 %s" % (name, gender_text))


# 假设班上的同学，男生居多
#  提示：在指定缺省参数的默认值时，应该使用最常见的值做为缺省参数的默认值！
print_info("小明", False)
print_info("小明")

