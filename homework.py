# str1='yezi'
# list1=list(str1)
# print(list1)
# list2=str1.split()
# print(list2)

# x=0
# for i in range(1,50,6):
#     x+=i
# print(x)

# str1='yezii'
# dict1={'name':'ouyang'}
# list1=('yezifei',2,3,4,5)
# a=len(str1)
# b=len(dict1 ['name'])
# c=len(list1)
# # print(c)
# if a > 5:
#     print(True)
# else:
#     print(False)
# if b > 5:
#     print(True)
# else:
#     print(False)
# if c > 5:
#     print(True)
# else:
#     print(False)

# name=input('请输入姓名:')
# age=input('请输入年龄:')
# gender=input('请输入性别:')
# print('''************************************
# 姓名：{0}
# 性别：{1}
# 年龄：{2}
# ************************************
# '''.format(name,gender,age))


# i=int(input('请输入一个数值:'))
# j=i%2
# if j==1:
#     print('False')
# else:
#     print('Ture')

# li=['hello','scb11','!']
# li[1]='python18'
# str=str(li[0]+li[1]+li[2])
# print(str)

# str1='python hello aaa 123123aabb'
# a=str1.count('a')
# print(a)
# print(str1.find('123'))
# print('o a'in str1)
# print('he' in str1)
# print('ab' in str1)

# best_language='PHP is the  best programming language in the world!'
# best_language1=best_language.replace('PHP','Python')
# best_language=best_language1
# print(best_language)

# a=int(input('请输入数字1-7：'))
# if a == 6 or a == 7 :
#     print('今天是周末')
# elif a == 5:
#     print('今天是周五')
# elif a == 4:
#     print('今天是周四')
# elif a == 3:
#     print('今天是周三')
# elif a ==2:
#     print('今天是周二')
# elif a==1:
#     print('今天是周一')
# else:
#     print('输入错误，请重新输入数字1-7')

# num =int(input('请输入1-7之间的数字：'))
# if num == 1:
#     print('今天是周一')
# elif num == 2:
#     print('今天是周二')
# elif num == 3:
#     print('今天是周三')
# elif num == 4:
#     print('今天是周四')
# elif num == 5:
#     print('今天是周五')
# elif num == 6 or num == 7:
#     print('今天是周末')

# li=[1,2,3,4,5,6,7,8,9]
# print(li[2:9:3])
# s='python java php'
# print(s[7:11])
# tu=['a','b','c','d','e','f','g','h']
# print(tu[-2:-8:-5])

#第9题
# name=input('请输入姓名:')
# age=input('请输入年龄:')
# gender=input('请输入性别:')
# dict1={'name':name,'age':age,'gender':gender}
#
# # print('''
# # 我的名字是{}，今年{}岁,性别{},喜欢敲代码
# # '''.format(name,age,gender))
# a=str(dict1.get('name'))
# b=str(dict1.get('age'))
# c=str(dict1.get('gender'))
# print(c)
# print('我的名字'+a+',今年'+b+'岁，性别'+c+',喜欢敲代码')
#
# # dict1={'city':'hangzhou'}
# high=input('请输入您的身高：')
# phone=input('请输入您的联系方式:')
# dict1.update({'high':high,'phone':phone})
# # print(dict1)
#
# dict1.pop('phone')
# # print(dict1)
#
# dict1.update({'city':'hangzhou','qq':'666666','hobby':'ping-pong'})

#第10题
# member=int(input('请输入数额：'))
# if member > 100:
#     m=member*0.8
#     n=str(m)
#     print('折扣20%，最终价格'+n)
# elif member>=50:
#     m=member*0.9
#     n = str(m)
#     print('折扣10%，最终价格'+n)
# else:
#     m = str(member)
#     print('无折扣，最终价格'+m)

#第11题
# member=input('请输入一个5位数：')
# a=member[0]
# b=member[4]
# c=member[1]
# d=member[3]
# e=len(member)
# if e==5:
#     if a==b and c==d:
#         print('这个数字是回文数')
#     else:
#         print('这个数字不是回文数')
# else:
#     print('输入错误，请重新输入一个5位数字：')

# 第12题
# dict1={'name':'小明','age':'18','occup':'students','teacher':{'语文':'李老师','数学':'王老师','英语':'张老师'}}
# print(dict1.get('name'))
# print(dict1.get('teacher').get('数学'))

#第13题
# a=[]
# sum=0
# for i in range(0,100,2):
#     a.append(i)
#     sum+=i
# print(sum)
# print(a)

#第14题
# for i in range(1,10):
#     for x in range(1,i+1):
#         y=i*x
#         # print(type(i))
#         # print(type(x))
#         print('{}*{}={}'.format(i,x,y),end="  ") #end=""控制换行操作
#     print()

#第15题
# num=0
# for i in range(1,5):
#     for x in range(1,5):
#         for y in range(1,5):
#             if i!=x and i!=y and y!=x:
#                 num +=1
#                 z=i*100+x*10+y
#                 print(z)
# print('总共{}个互不相同无重复数字'.format(num))

#第16题
# def jjcc(shuzi1,shuzi2,method):
#     if method ==1:
#         num=shuzi1+shuzi2
#         return num
#     elif method ==2:
#         num = shuzi1 - shuzi2
#         return num
#     elif method==3:
#         num = shuzi1 * shuzi2
#         return num
#     elif method==4:
#         num=shuzi1/shuzi2
#         return num
#     else:
#         print(函数选择输入错误)
# shuzi1=int(input('请输入数字1：'))
# shuzi2=int(input('请输入数字2：'))
# method=int(input('加【1】\n减【2】\n乘【3】\n除【4】\n请选择使用函数:'))
# a=jjcc(shuzi1,shuzi2,method)
# print(a)

for i in range(2,200):
    k=True
    for j in range(2,i):#for j in range(2,i/2+1)
       if(i%j==0):
         k = False
         break
    if(k==True):
       print(i)

# for i in range(1,10,1):
#     print(i)