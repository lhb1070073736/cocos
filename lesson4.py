# -*- coding: utf-8 -*-
# @Author   :   YaMeng
# @File :   lesson4.py
# @Software :   PyCharm
# @Time :   2020/8/20 9:20
# @company  :   湖南省零檬信息技术有限公司
'''
函数的定义：
     1) 具备某一功能的代码段
     2) 可以重复使用

函数定义语法：
def 函数名称():
    函数体(实现功能的代码段)

注意：函数体的缩进。

'''

# salary = 10000  #底薪
# bonus = 2000  # 奖金
# subsidy = 1000 # 补贴
#
# sum1 = salary + bonus + subsidy
# print(sum1)

# 无参函数
# def good_job():
#     (有些东西不小心删除了，不重要)

# 函数并不会自己运行
# 必须要调用函数才会去执行函数体的代码段
# good_job()

# 有参函数
# 必备参数： 定义了之后，必须要传入的参数
# def good_job(salary, bonus, subsidy):   # 只是定义了变量，并没有实际传参，所谓的形参
#     sum1 = salary + bonus + subsidy
#     print(sum1)
#
# good_job(12000, 5000, 3000)  # 调用函数，进行传参

# 默认参数
# 定义一个默认参数后，如果不传入参数，就会使用默认值，如果传入了参数，那么就使用传入的实际参数
# 规定：默认参数必须要在必备参数的后面
# def good_job(salary, bonus, bonus1, subsidy=500):
#     sum1 = salary + bonus + subsidy + bonus1
#     print(sum1)

# good_job(12000, 5000, 2000)
# good_job(12000, 5000)  # 调用函数，进行传参
# good_job(salary=10000, subsidy= 12300, bonus= 20000)
# good_job(9000, subsidy=20000, bonus= 15000, bonus1=1200)

# 不定长参数
# 可以传也可以不传。传的话，是可以传任意个数的参数
# 使用场景：不确定的参数个数，比如：年终奖，全勤奖，项目奖金，过节奖金。。。。
# *args
# 在必备参数和默认参数都接收完了之后，剩下的所有的参数都会被这个不定长参数接收，接收完了的数据是以元祖的形式保存
# def good_job(salary, bonus, subsidy=500, *args):   #  位置传参
#     print(args)
#     sum1 = salary + bonus + subsidy
#     for i in args:
#         sum1 += i
#     print(sum1)
#
# good_job(12000, 2000, 1000,500, 40000, 8000)

# **kwargs  也是不定长
# 在必备参数和默认参数都接收完了之后，剩下的所有的参数都会被这个不定长参数接收，接收完了的数据是以字典的形式保存
# def good_job(salary, bonus, subsidy=500, *args, **kwargs):  # 关键字传参
#     print(args)
#     print(kwargs)
#     sum1 = salary + bonus + subsidy
#     for i in args:
#             sum1 += i
#     for j in kwargs.values():   # j 取的是字典里的所有的value
#          # sum1 += kwargs.get(j)   #for j in kwargs():
#         #  sum1 += kwargs[j]       #for j in kwargs():
#         sum1 += j
#     print(sum1)
#
# kwargs = {'fuli': 1000, 'jiangjin': 20000, 'baoxiao': 1500}


# good_job(12000, 2000, 1000,500, 40000, 8000, fuli = 1000, jiangjin = 20000, baoxiao = 1500)

# 小总结：
# 定义的参数类型：必备参数，默认参数，不定长参数（*args, **kwargs）
# 传入参数的类型：位置传参（一一对应的顺序传参），关键字传参，混合传参


# 函数写完了，肯定是要给别人去用的。
# 函数的结果要提供出来别人用。
# 请注意。函数不加retuen是没有返回值的！！！！！
# 函数里面写print并不是返回值，只是让你看到结果而已。print只是让你看结果！！！！
# 如果要有返回值，就必须要加return
# return下面的代码都不会被执行了
# def good_job(salary, bonus, bonus1, subsidy=500):
#     sum1 = salary + bonus + subsidy + bonus1
#     return sum1, salary, bonus1
#
# result = good_job(9000, subsidy=20000, bonus= 15000, bonus1=1200)
# print(result)



# dict1 = {"name":"yezi","age":18,"gender":"male"}
# print(dict1.keys())  # 一次性就key全部都取出来
# print(dict1.values())  # 一次性把value全部都取出来
# print(dict1.items())  # 一次性把key和value当做一个整体取出来，一个一个的key：value











