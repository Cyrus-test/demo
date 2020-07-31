# # 键值对的key 必须是不可变类型数据
# #
# # 键值对的value 可以是任意类型的数据
#
# In [1]: d = {}
#
# In [2]: d =  ["name":"xiaoming"]
#   File "<ipython-input-2-7155b50e0185>", line 1
#     d =  ["name":"xiaoming"]
#                 ^
# SyntaxError: invalid syntax
#
#
# In [3]: d["name"] = "xiaoming"
#
# In [4]: d
# Out[4]: {'name': 'xiaoming'}
#
# IIn [5]: d[1] = "打""
#   File "<ipython-input-5-87de4a38a93f>", line 1
#     d[1] = "打""
#                ^
# SyntaxError: EOL while scanning string literal
#
#
# In [6]: d[1] = "打"
#
# In [7]: d
# Out[7]: {'name': 'xiaoming', 1: '打'}
#
# In [8]: d[(1)] = "元组"
#
# In [9]: d
# Out[9]: {'name': 'xiaoming', 1: '元组'}
#
# In [10]: d[1, 2, 3] = "lpb"
#
# In [11]: d
# Out[11]: {'name': 'xiaoming', 1: '元组', (1, 2, 3): 'lpb'}
#
# In [12]: d[[1, 2, 3]] = "lpb"
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-12-417e73e316c6> in <module>
# ----> 1 d[[1, 2, 3]] = "lpb"
#
# TypeError: unhashable type: 'list'