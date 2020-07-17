# In [1]: [1,2]*5
# Out[1]: [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
#
# In [2]: (1,2)*5
# Out[2]: (1, 2, 1, 2, 1, 2, 1, 2, 1, 2)
#
# In [3]: [1,2] +[3,4]
# Out[3]: [1, 2, 3, 4]
#
# In [4]: t_list =[1,2]
#
# In [5]: t_list.extend([5,6])
#
# In [6]: t_list
# Out[6]: [1, 2, 5, 6]
#
# In [7]: t_list.append(0)
#
# In [8]: t_list
# Out[8]: [1, 2, 5, 6, 0]
#
# In [9]: t_list.append([89,3])
#
# In [10]: t_list
# Out[10]: [1, 2, 5, 6, 0, [89, 3]]
#
# In [11]: "a" in "abdced"
# Out[11]: True
#
# In [12]: "a" not in "abdced"
# Out[12]: False
#
# In [13]: 1 in [12124242]
# Out[13]: False
#
# In [14]: 1 in [1,1,1,2,2,3,]
# Out[14]: True
#
# in和not in 只能判断字典的key
# In [15]: "a" in {"a" : "laowang"}
# Out[15]: True
#
# In [16]: "laowang" in {"a" : "laowang"}
# Out[16]: False