#整形 int
#type（） 打印变量的类型，直接打印类型出来
#isinstance（） 判断变量的类型、做校验、返回True或False

# a=12
# print(type(a))
# print(isinstance(a,int) )
# # 练习
c=18
print(type(c))
print(isinstance(c,int))


#浮点型 float 小数
# b=1.2134
# print(type(b))

#布尔值 bool  值为True或False
# c=True
# print(type(c))

#字符串str
# a='scb15期最厉害'
# print(type(a))
#字符串的引号三种 单引号' 双引号" 三引号'''
#引号和引号成对出现
#三引号所见即所得

#
# b='''叶子是最胖的
#        2131412'''
# print(b)
# print(type(b))

#字符串的切片  ==在字符串里面去取值
#字符串是有顺序、有长度的
#顺序：索引位置，从0开始
#切片：【索引头a：索引尾b：步长c】     索引头（从0开始） 左闭右开（去头不去为）
# 显示的字符： 从 a到b  每c个字符显示一个
# a='scb15期最棒！！！'
# print(a[6])       # 6位数据（第七个数据） 最
# print(a[0:6:2])   # 从0到6  每两个显示1个（最前的一个，不是随机）
# print(a[::])      #取所有值
# print(a[::-1])      #倒叙
# print(a[-1:-6:-1])  #倒叙


# len()                获取字符串长度
# print(len(a))

#替换字符串
# a='scb15期最棒！！！'
# str=a.replace("scb15期","叶子")
# print(str)

#获取索引
# index()
# 获取指定字符串开始的索引位置
#如果没有找到字符串，就会报错，后面的代码就不会继续执行了
# a='wohaobang'
# # print(a.index('h'))
# print(a.index('h'))

#find()
#如果没找到字符，不会报错，但是会返回-1
# a='wohaobang'
# print(a.find('b'))

#格式化输出  format()
#{}占位符
# name='yezi_liangbin'
# age=16
# gender='male'

# print('''
# -------------我的信基本-------------
# name={}
# age={}
# gengder={}
# '''.format(name,age,gender)
#       )

# print('''
# -------------我的信基本-------------
# name={0}
# age={1}
# gengder={2}
# '''.format(name,age,gender)
#       )

# 运算符
#运算符号 +-*/ %   （加减乘除 取余）


#+ 拼接字符串
# a='feise'
# # b='zuimei'
# # print(a+b)

#重复输出
# a='i love you\n'  #\n 是换行
# print(a*10)

#赋值运算符
# +  +=  -=
# a=12
# a+=12   # 相当于 a=a+12
# print(a)

# b=3
# b-=2 #相当于 b=b-2
# print(b)

#比较运算符
# # == >=  <=  < > !=
# a=2
# b=2
# print(a>=b)

#逻辑运算符
# and  not  or
#真真为真   假假为假
# print(10>2 and 3>2)
# print(not 10>5)

#成员运算符  in   not in

# a='ningmengban'
# print('j'in a)


# name=input('请输入你的名字：')
# age=int(input('请输入你的年龄：'))
# gender=input('请输入你的性别:')
# print('''
# *****************************
# name={0}
# gender={2}
# age={1}
# *****************************
# '''.format(name,age,gender)
#       )

str1='python hello aaa 123123aabb'
# print(str1[0:6])    #题目1
# print('o'in str1 and '7' in str1)
# print('o a'in str1)  #题目2  'o a'
# print('he'in str1)   #题目2  'he'
# print('ab'in str1)   #题目2  'ab'
# str2=str1.replace('python','lemon')  #题目3
# print(str2)   #题目3
# print(str1.find('aaa'))   #题目4
# print(str1.index('aaa'))   #题目4
