#列表 []
#列表里面是可以存放任意的数据类型(包含列表)
#列表里不同的元素之间用逗号分隔
#列表允许元素重复
#列表中的元素是可以被改变的
# list1=[1,1,2,333.33,'yezi',True,'yuer',[1,2,3,4,5]]
# print(list1)
# print(type(list1))

#列表取值  --切片
# print(list1[2])
# print(list1[0:7:1])
#参数取值
# print(list1[7][2])

#参数增加
# append() 将单个元素追加到list末尾
# list1=[1,1,2,333.33,'yezi',True,'yuer',[1,2,3,4,5]]
# list1.append('laoxu')
# print(list1)
# list1.append(['2',3])
# print(list1)

#extend      一次性的将列表里面的每个元素追加到列表末尾
# list1=[1,1,2,333.33,'yezi',True,'yuer',[1,2,3,4,5]]
# list1.extend([1,2,'feise'])
# print(list1)

#指定位置追加  单个元素
#insert
# list1=[1,1,2,333.33,'yezi',True,'yuer',[1,2,3,4,5]]
# list1.insert(3,['g',2])
# print(list1)

#删除
# pop 不带任何参数，默认删除最后一个元素
#pop 带索引  指定位置删除
# list1=[1,1,2,333.33,'yezi',True,'yuer',[1,2,3,4,5]]
# list1.pop()
# print(list1)
# list1.pop(3)
# print(list1)

#指定元素删除
#remove
#指定元素重复，只删除第一个
# list1=[1,1,2,333.33,333.33,'yezi',True,'yuer',[1,2,3,4,5]]
# list1.remove(333.33)
# print(list1)

#清空列表
# list1.clear()
# print(list1)

#改 通过重新赋值的方法
# list1=[1,1,2,333.33,333.33,'yezi',True,'yuer',[1,2,3,4,5]]
# list1[5]='na'
# print(list1)

#统计列表里的元素总数
#len()
# list1=[1,1,2,333.33,333.33,'yezi',True,'yuer',[1,2,3,4,5]]
# print(len(list1))

#统计列表里指定元素的个数
# list1=[1,1,2,333.33,333.33,'yezi',True,'yuer',[1,2,3,4,5]]
# print(list1.count(333.33))


#元组（）  tuple
# tuple1=()
# print(type(tuple1))

#元组里可以放任意数据类型
#元组里不同的元素直接用逗号隔开
#元组的元素不可变
# tuple1=(1,2,3,'tyezi',[2,3])
#元组用切片方式取值
# print(tuple1[2])
# print(tuple1[4][1])

#如果要改元组元素
#先将元组转为列表   修改  在从列表改为元组
# tuple1=(1,2,3,'tyezi',[2,3])
# list1=list(tuple1)
# list1[3]='c'
# print(list1)
# tuple1=tuple(list1)
# print(type(tuple1))
# print(tuple1)

#字典{}   dict
#字典里面的元素是键值对    key:value
#json格式只是一种格式，不是一种数据类型
#使用的场景：储存对象的一些属性：姓名等
#字典元素无序
# dict1={}
# print(type(dict1))

#key不能使用list，dict   value可以是任意的数据类型
#字典里的元素是可以被改变的==改变的其实是value值  而key是唯一的，不变的
#value随便，key不能重复也不能变
# dict1={"name":"yezi","age":"12","dender":"male","hobby":"篮球"}
# print(dict1)

#取值
#dict是没有索引的
#通过key取值
# print(dict1['name'])
#通过get()方式
# print(dict1.get('hobby'))

#增加
#update
# dict1={"name":"yezi","age":"12","dender":"male","hobby":"篮球"}
# dict1.update({"city":"hangzhou","hight":"180"})
# print(dict1)
#如果key存在则直接修改
# dict1.update({"city":"guangzhou"})
# print(dict1)

#删除  pop
# dict1={"name":"yezi","age":"12","dender":"male","hobby":"篮球"}
# dict1.pop('name')  #必须要有key才行
# print(dict1)

#集合  set
#元素是不能重复
#使用场景：一般都是给list去重
# list1=[1,1,2,2,3,3]
# set1=set(list1)
# print(list1)
# print(set1)

#控制流
#控制代码的走向：判断、循环
'''
if 条件1：      --> 满足条件1才会执行语句1
   执行语句1
elif 条件2
    执行语句2
...
'''
# money=int(input('请输入你的工资：'))
# if money >= 200000 :
#     print('我要去火星')
# elif money >= 15000 :
#     print('我去吃大餐')
# else:
#     print('搬砖去')

#for 循环
#将数据对象里的元素，依次赋值给到变量，循环的次数是由数据对象的长度决定的
#遍历这个数据对象的每个元素，然后依次取出
'''
for 变量名  in 数据对象：
    执行语句
'''
# str1='scb15期叶子是最棒的'
# for i in  str1:
#     print(i)

#循环时可以中断的
#continue  跳出本次循环，后续循环继续
# str1='scb15期叶子是最棒的'
# for i in  str1:
#     if i=='1':
#         continue
#     print(i)
#break  跳出本次循环，后续循环不执行
# str1='scb15期叶子是最棒的'
# for i in  str1:
#     if i=='1':
#         break
#     print(i)

# range() 生成整数数列
# range(开始,结束,步长)
# for a in range(1,10,1):
#     print(a)

#作业
# a=[1,2,'6','summer']
# print(a.index('i'))

# dict_1={"class_id":"45",'num':20}
# num=int(dict_1['num'])
# if num > 5:
#     print(num)

# list3=['囧囧','唐僧','旧模样','ouyang','Nacy','土豆江']
# list3[0]={"name":"囧囧","gender":"male","age":"12","city":"杭州"}
# list3[1]={"name":"唐僧","gender":"male","age":"1200","city":"广州"}
# list3[2]={"name":"旧模样","gender":"female","age":"18","city":"上海"}
# list3[3]={"name":"ouyang","gender":"male","age":"20","city":"长沙"}
# list3[4]={"name":"Nacy","gender":"male","age":"13","city":"火星"}
# list3[5]={"name":"土豆江","gender":"male","age":"120","city":"太阳"}
# print(list3)
# # dict1={}
# # dict1.update(list3)
# # print(dict1)