import requests
# url_reg = 'http://api.lemonban.com/futureloan/member/register'
# requests_body = {"mobile_phone":"13858473621","pwd":"lemon123","type":1}
# requests_header = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}
# yezi = requests.post(url=url_reg,json=requests_body,headers=requests_header)
# res_log = yezi.json()
# print(res_log)


# url_login = 'http://api.lemonban.com/futureloan/member/login'
# requests_body = {"mobile_phone":"13858473621","pwd":"lemon123"}
# requests_header = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}
# yezi = requests.post(url=url_login,json=requests_body,headers=requests_header)
# res_log = yezi.json()
# print(res_log)


url_login = 'http://api.lemonban.com/futureloan/member/login'
requests_body1 = {"mobile_phone":"13858473001","pwd":"12345678"}
requests_header1 = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}
yezi = requests.post(url=url_login,json=requests_body1,headers=requests_header1)
res_log = yezi.json()

member_id = res_log['data']['id']
token = res_log['data']['token_info']['token']

url_rec = 'http://api.lemonban.com/futureloan/member/recharge'
requests_body2 = {"member_id":member_id,"amount":"10000"}
requests_header2 = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json","Authorization":"Bearer" + " " + token}
yezi2 = requests.post(url=url_rec,json=requests_body2,headers=requests_header2)
res_log = yezi2.json()
print(res_log)