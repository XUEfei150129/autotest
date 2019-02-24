import unittest
import pprint
import requests
import time
import string, random
from datetime import datetime


class Web_interface():
	create_users = []

	def __init__(self):  # 定义一个初始化方法
		pass

	def login_api(self, url, username="admin_pretest", password="11111111"):
		"""登录函数，参数是url，缺省的是：username=admin_pretest, password=11111111"""
		values = {
			"username": username,
			"password": password,
			"url": "",
			"ismobile": "false",
			"rememberMe": "true"
		}

		res = requests.post(("%s" + "/api2/user/login") % url, data=values)
		session = res.cookies["PHPSESSID"]
		return session

	def list_number(self, url, sessionid):
		"""列出当页的所有数据，返回值是数据的id"""
		list_id = []
		values = {
			"params[paging][perPage]": 15,
			"params[paging][start]": 0,
			"params[appId]": "ShuJuChuFaShuJuTongZ",
			"params[tableId]": "shujuchufashujutongz",
			"params[labelId]": 5127
		}
		res = requests.post(("%s" + "/api2/view/data/information/label") % url,
		                    data=values,
		                    cookies={"PHPSESSID": sessionid})
		numbers = res.json()["result"]["data"]
		for number in numbers:
			list_id.append(number["id"])
		return list_id

	def del_number(self, url, a, sessionid):
		"""将列表里面数据的id，全部删掉"""
		values = {
			"appId": "ShuJuChuFaShuJuTongZ",
		}
		for index, n in enumerate(a):
			# li = ["a", "b", "c", "d", "e", "f"]
			#
			# for i in enumerate(li):
			# 	print(i)
			# (0, ‘a’)
			# (1, ‘b’)
			# (2, ‘c’)
			# (3, ‘d’)
			# (4, ‘e’)
			# (5, ‘f’)
			values["recordId[" + str(index) + "]"] = n

		res = requests.delete(
			("%s" + "/api/information/data/shujuchufashujutongz") % url, data=values, cookies={"PHPSESSID": sessionid})

	# print(res)

	def del_all(self, url, username, password):
		"""这个函数就是将上面登录列出删除的函数封装成一个函数"""
		session = self.login_api(url, username, password)
		a = self.list_number(url, session)
		if a != []:
			self.del_number(url, a, session)
			a = self.list_number(url, session)
			if a != []:
				raise Exception("删除所有数据的封装函数有问题")

# 下面是企业主页UI辅助接口

	def add_user(self, sessionid, url):
		"""添加一个用户"""
		headers = {
			"Cookie": "PHPSESSID=" + sessionid,
		}
		ran_str = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=10))
		ran_QQ = ''.join(random.choices(string.digits, k=8))
		# print(ran_str)
		self.create_users.append(ran_str)
		values = {
			'target_org_id': 26,
			'usermessage[login_user_id]': '%s' % ran_str,
			'usermessage[real_name]': '%s' % ran_str,
			'usermessage[password]': 11111111,
			'usermessage[birthday]': '1992-1-25',
			'usermessage[birth_type]': 0,
			'usermessage[entry]': '2016-06-11',
			'usermessage[phone]': '',
			'usermessage[email]': '%s@qq.com' % ran_QQ,
			'usermessage[sex]': 0,
			'usermessage[isSecurity]': 'false',
			'usermessage[qq]': '%s' % ran_QQ,
			'usermessage[ext]': '8003',
			'usermessage[idcard]': '3202811995%s' % ran_QQ,
			'usermessage[addr]': '南京',
			'usermessage[jobdesc]': '',
			'usermessage[main_job]': "一级部门10-云平台研发部998988-平台一组-组员",
			'userid': ran_str,
			'mainjob': 26,
			'appointment': '[]',
			'extra_id': 33,
			'leader': '',
			'entId': 'APICeShiQiYe',
			'userId': 'ApiTest'
		}

		sendrequest = requests.post(url + '/service_org/organization/user/user', data=values, headers=headers)
		#print(self.create_users)
		return self.create_users

	def add_users(self, url, number):
		"""添加多个用户的封装函数，检查添加的人数和多出的人数是不是一致"""
		sessionid = self.login_api(url)
		for i in range(0, int(number)):
			b = self.add_user(sessionid, url)
		if len(b) == int (number):
			print("添加的人数是 {} ，生成的人数是 {} 。数量正确".format(int (number),len(b)))
			return self.create_users
		else:
			raise Exception("添加的人数是 {} ，生成的人数是 {} 。".format(int (number),len(b)))


	def app_home(self,sessionid,url):
		"""为了能成为活跃用户，调用一下这个函数"""
		headers = {
			"Cookie": "PHPSESSID=" + sessionid,
		}
		res = requests.get(url + "/api2/home/entrance", headers=headers)
		return res.json()["status"]


	def active_people(self, url, number):
		"""这个函数实现创建用户，并将创建的用户登录，成为活跃用户"""
		values = {
			"password": "11111111",
			"url": "",
			"ismobile": "false",
			"rememberMe": "true"
		}
		d = self.add_users(url,number)
		for i in d:
			values['username'] = i
			res = requests.post(url + "/api2/user/login", data=values)
			sessionid = res.cookies["PHPSESSID"]
			status = self.app_home(sessionid,url)
			if status == 200:
				print("第{}个用户：{}成功登录。成为活跃用户".format(d.index(i) + 1, i))
			else:
				raise Exception("第{}个用户：{}成功失败".format(d.index(i) + 1, i))


	def list_style(self,url):
		sessionid = self.login_api(url)
		sendrequest = requests.get(url + '/api/admin/enterprise/stylesheet',cookies={"PHPSESSID": sessionid})
		style_test = str(sendrequest.text)
		return style_test

if __name__ == '__main__':
	wo = Web_interface()
	wo.add_users("https://www.qycloud.com.cn",2)


# def del_all(url,username,password):
#
# 	def login_api(url,username,password):
#
# 		values = {
# 			"username": username,
# 			"password": password,
# 			"url": "",
# 			"ismobile": "false",
# 			"rememberMe": "true"
# 		}
#
# 		res = requests.post(("%s" + "/api2/user/login")%url, data=values)
# 		session = res.cookies["PHPSESSID"]
# 		return session
#
# 	sessionid = login_api(url,username,password)
#
#
# 	def list_number(url,sessionid):
# 		list_id = []
# 		values = {
# 			"params[paging][perPage]": 15,
# 			"params[paging][start]": 0,
# 			"params[appId]": "ShuJuChuFaShuJuTongZ",
# 			"params[tableId]": "shujuchufashujutongz",
# 			"params[labelId]": 5127
# 		}
# 		res = requests.post(("%s"+"/api2/view/data/information/label")%url,
# 		                    data=values,
# 		                   cookies={"PHPSESSID": sessionid})
# 		numbers = res.json()["result"]["data"]
# 		for number in numbers:
# 			list_id.append(number["id"])
# 		return list_id
#
#
# 	a = list_number(url,sessionid)
# 	if a != []:
#
# 		def del_number(url,a,sessionid):
# 			values = {
# 				"appId": "ShuJuChuFaShuJuTongZ",
# 			}
# 			for index, n in enumerate(a):
# 				# li = ["a", "b", "c", "d", "e", "f"]
# 				#
# 				# for i in enumerate(li):
# 				# 	print(i)
# 				# (0, ‘a’)
# 				# (1, ‘b’)
# 				# (2, ‘c’)
# 				# (3, ‘d’)
# 				# (4, ‘e’)
# 				# (5, ‘f’)
# 				values["recordId["+str(index)+"]"] = n
#
# 			res = requests.delete(("%s" + "/api/information/data/shujuchufashujutongz")%url,
# 			                      data = values,
# 			                      cookies={"PHPSESSID": sessionid})
# 		del_number(url, a, sessionid)
#
#
# del_all("https://www.qycloud.com.cn","admin_pretest","11111111")
#
#


# if  __name__ == '__main__':
# 	def del_all():
# 		wo = web_interface()
# 		session = wo.login_api("https://www.qycloud.com.cn","admin_pretest","11111111")
# 		a = wo.list_number("https://www.qycloud.com.cn",session)
# 		if a != []:
# 			wo.del_number("https://www.qycloud.com.cn",a,session)
#
#
# 	del_all()
