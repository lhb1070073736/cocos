# -*- coding: utf-8 -*-
# @Author   :   YaMeng
# @File :   lesson5.py
# @Software :   PyCharm
# @Time :   2020/8/20 14:12
# @company  :   湖南省零檬信息技术有限公司


# python有非常丰富的第三方库
# 第三方库其实就是其他python工程师们写好了的代码。用来实现某一个功能的
# requests是一个第三方库，是用来发送请求的
# 当我们要去使用第三方库的时候，第一步应该是要去下载对应库吧
# pip install requests
# 第二步，把库导入进来
# import

import requests

# 实操，完成注册接口发送
# 第一步，先确定好用什么请求方式
# 第二步，明确接口测试要发送的参数，url、header、body、method顺便就把参数准备
# 第三步，发请求
# 第四步，接收请求返回结果
# ps：如果单单只是打印返回结果的话，那么返回的只是一个响应消息。200
# ps：我们做接口测试是肯定需要得到code，msg这些信息，
# ps：发送请求体，到底是用data还是用json，就需要你们通过接口文档去确认你们的请求格式了
# {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}
# url = 'http://api.lemonban.com/futureloan/member/register'
# requests_body = {"mobile_phone":"13613440102","pwd":"12345678","type":1}
# requests_header = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}
# res = requests.post(url=url,json=requests_body,headers=requests_header)
# print(res.json())
# print(res.text)

import jsonpath

# 登录请求
# url = 'http://api.lemonban.com/futureloan/member/login'
# requests_body = {"mobile_phone":"13613440102","pwd":"12345678"}
# requests_header = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}
# res = requests.post(url=url,json=requests_body,headers=requests_header)
# print(type(res))
# res_log = res.json()       #转换数据类型
# print(res.json())
# print(type(res_log))

#
# # 充值
# # member_id.token
# member_id = res_log['data']['id']
# token = res_log['data']['token_info']['token']
# print(member_id)
# print(token)
# member_id = jsonpath.jsonpath(res_log, '$.data.id')[0]
# token = jsonpath.jsonpath(res_log, '$.data.token_info.token')[0]
# $ 最外层  .. 表示匹配任意次数，把带有id参数名的值和带有token参数名的值，全都取出来，放在列表，根据后面的索引去决定使用哪个值
# member_id = jsonpath.jsonpath(res_log, '$..id')[0]
# token = jsonpath.jsonpath(res_log, '$..token')[0]
#
#
# print(member_id)
# print(token)
# print('*' * 60 + '这是一个分割线' + '*' * 40)
# print('*' * 60 + '这是一个分割线' + '*' * 40)
# print('*' * 60 + '这是一个分割线' + '*' * 40)
#
# url_rec = 'http://api.lemonban.com/futureloan/member/recharge'
# requests_body_rec = {"member_id":member_id,"amount":"10000"}
# requests_header_rec = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json","Authorization":"Bearer" + " " + token}
# res_rec = requests.post(url=url_rec,json=requests_body_rec,headers=requests_header_rec)
# print(res_rec.json())



# token取值
# 第一种：字典的嵌套取值  dict[][][][]
# 第二种：jsonpath， 注意：jsonpath取出来的值是列表的，所以要加索引才能取到列表里面的值
# 第三种：用jsonpath的递归搜索



# 把主要的功能给封装成函数
# url = 'http://api.lemonban.com/futureloan/member/login'
# requests_body = {"mobile_phone":"13613440102","pwd":"12345678"}
# requests_header = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}
# res = requests.post(url=url,json=requests_body,headers=requests_header)
# res_log = res.json()
# print(res.json())

#
# def func(url, res_body):
#     requests_header = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}
#     res = requests.post(url=url, json=res_body, headers=requests_header)
#     res_log = res.json()
#     return res_log
#
# url = 'http://api.lemonban.com/futureloan/member/login'
# requests_body = {"mobile_phone":"13613441102","pwd":"12345678"}
# res = func(url, requests_body)
# print(res)