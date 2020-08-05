def numbers(*args, **kwargs):

    print(args)
    print(kwargs)


gl_args = (1, 2, 3)
gl_dict = {"姓名": "小明", "age": "18"}

# numbers(gl_args,gl_dict)
numbers(*gl_args, **gl_dict)