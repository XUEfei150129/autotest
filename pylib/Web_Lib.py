from selenium import webdriver
from cfg import *
from pylib.Web_interface import *
import time
import pprint
from selenium.webdriver.common.action_chains import ActionChains  # 悬停的操作
from selenium.webdriver.support.ui import Select
import string, random
from datetime import datetime
import win32com.client
import os


class Web_Lib():
	ROBOT_LIBRARY_SCOPE = 'GLOBAL'

	def __init__(self):
		pass

	# 方便导入库的时候，传入参数

	def open_browser(self):
		self.wd = webdriver.Chrome()
		self.wd.maximize_window()  # 最大化窗口
		self.wd.implicitly_wait(15)

	def close_browser(self):
		self.wd.quit()

	def user_login(self, environment, nsername="admin_pretest", password="11111111", enterprise="pre测试企业"):  # 用户登录
		self.wd.get(environment + home_login)  # 输入网址
		time.sleep(1)
		self.wd.find_element_by_id("userid").send_keys(nsername)
		self.wd.find_element_by_id("password").send_keys(password)
		loginele = self.wd.find_element_by_class_name("loginButton")
		time.sleep(1)
		loginele.click()  # 登录企业
		time.sleep(3)
		self.wd.get(environment + appcenter)
		# print(driver.title)
		b = self.wd.title
		if enterprise in b:
			print("成功登录到" + enterprise)
		else:
			entele = self.wd.find_element_by_css_selector("i.icon-xiala- ")  # 选中头像右侧的下拉按钮
			time.sleep(2)
			entele.click()  # 点击头像右侧的下拉按钮
			enttitle = self.wd.find_element_by_css_selector("li .ent-switcher")  # 选中企业切换按钮
			ActionChains(self.wd).move_to_element(enttitle).perform()  # 悬停至企业切换按钮
			time.sleep(1)
			ents = self.wd.find_elements_by_css_selector('li .ent-switcher ul li')  # 选中要切换的企业，并进入
			for ent in ents:
				if enterprise == ent.text:
					ent.click()
					time.sleep(2)
					c = self.wd.title
					if enterprise in c:
						print("成功切换到" + enterprise)
					break

	def find_Element(self, row, number, type):  # 封装的from的页面元素
		if type == "字符串" or type == "数字" or type == "日期时间" or type == "编号":
			self.ele_front = "div:nth-child(2)>div:nth-child(%s)>div:nth-child(%s)>div>" % (row, number * 2)
			self.ele_back = "div>div>input"
			self.ele = self.ele_front + self.ele_back

		elif type == "用户信息" or type == "文本":
			self.ele_front = "div:nth-child(2)>div:nth-child(%s)>div:nth-child(%s)>div>" % (row, number * 2)
			self.ele_back = "div>div>textarea"
			self.ele = self.ele_front + self.ele_back

		elif type == "经纬度":
			self.ele_front = "div:nth-child(2)>div:nth-child(%s)>div:nth-child(%s)>div>" % (row, number * 2)
			self.ele_back = "div"
			self.ele = self.ele_front + self.ele_back

		elif type == "地区":
			self.ele_front = "div:nth-child(2)>div:nth-child(%s)>div:nth-child(%s)>div>" % (row, number * 2)
			self.ele_back = "div>span>div>input"
			self.ele = self.ele_front + self.ele_back

		elif type == "单选" or type == "多选" or type == "数据源":
			self.ele_front = "div:nth-child(2)>div:nth-child(%s)>div:nth-child(%s)>div>" % (row, number * 2)
			self.ele_back = "div>div>div>input"
			self.ele = self.ele_front + self.ele_back

		elif type == "附件":
			self.ele_front = "div:nth-child(2)>div:nth-child(%s)>div:nth-child(%s)>div>" % (row, number * 2)
			self.ele_back = "div>div>div>button"
			self.ele = self.ele_front + self.ele_back


		else:
			raise Exception("cannot find any Element!!")

		return str(self.ele)

	def wf_to_df(self, environment):
		self.wd.get(environment + wf_to_df_01)  # 输入网址
		time.sleep(3)
		self.wd.find_element_by_css_selector("[class*=el-button][class*=view-btn-add]").click()  # 点击添加流程
		time.sleep(2.5)
		self.wd.find_element_by_css_selector(self.find_Element(1, 1, "字符串")).send_keys("123")  # 字符串字段里面输入123
		# self.wd.find_element_by_css_selector(self.find_Element(1,2,"用户信息")).click()  # 点击用户信息字段，选择管理员，点击保存
		# ele = self.wd.find_element_by_css_selector('[data-id*="admin_pretest"]')  # 选择管理员，点击保存
		# ele.click()
		# time.sleep(2)
		# ele1 = self.wd.find_element_by_css_selector(".ui-helper-clearfix.ui-dialog-buttonpane>div>button"
		#                                      ":nth-child(2)")  # 点击保存组织架构弹窗
		# ele1.click()
		self.wd.find_element_by_css_selector(self.find_Element(2, 1, "数字")).send_keys("456")
		ran_str = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=10))
		self.wd.find_element_by_css_selector(self.find_Element(3, 2, "文本")).send_keys(ran_str)
		self.wd.find_element_by_css_selector(".executor-add i").click()  # 点击添加联系人
		time.sleep(2)
		self.wd.find_element_by_css_selector('[data-id*="admin_pretest"] label').click()  # 选择管理员本身
		time.sleep(1)
		self.wd.find_element_by_css_selector(".ui-helper-clearfix.ui-dialog-buttonpane>div>button"
		                                     ":nth-child(2)").click()  # 点击组织架构弹窗里面的确定
		time.sleep(1)
		self.wd.find_element_by_css_selector("button.button-nextworkflow").click()  # 点击提交流程
		time.sleep(2)
		self.wd.get(environment + wf_to_df_02)  # 输入网址，进入接收器的应用
		res_text = self.wd.find_element_by_css_selector("div.el-table__body-wrapper.is-scrolling-none tbody>"
		                                                "tr:nth-child(1)>td:nth-child(3) span").text
		self.wd.get(environment + rulu_page)
		rulu_time_get = self.wd.find_element_by_css_selector('[role*="alert"]>tr:nth-child(8)>td:nth-child(4)').text
		now_time = str(datetime.now())
		now_time_year = now_time[0:4]  # 当前时间的年份
		rulu_time = '{}-{}'.format(now_time_year, rulu_time_get)  # 拼接成完整的时间如：2019-01-02 20:30:07
		timeArray = time.strptime(rulu_time, "%Y-%m-%d %H:%M:%S")
		timeStamp = int(time.mktime(timeArray))  # 在规则列表页获取到的时间转为时间戳
		a = int(time.time())  # 获取当前时间的时间戳,取整数部分
		if ran_str == res_text:
			if timeStamp in range((a - 60), (a + 60)):  # 时间戳在系统时间的前后70秒
				print("接收器的数据和触发时间都正确")
			else:
				raise Exception("接收器的数据正确但是触发时间异常：规则的时间是：%s，系统的时间是：%s" %
				                (rulu_time_get, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a))))
		else:
			if timeStamp in range((a - 60), (a + 60)):  # 时间戳在系统时间的前后70秒
				raise Exception("接收器的数据异常，触发时间正确：触发器的数据是：%s，接收器的数据是：%s"
				                % (ran_str, res_text))
			else:
				raise Exception("触发时间和接收器的数据都不正确：规则的时间是：%s，系统的时间是：%s,"
				                "触发器的数据是：%s，接收器的数据是：%s" %
				                (rulu_time_get, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a)), ran_str,
				                 res_text))

	def wf_to_wf(self, environment):
		self.wd.get(environment + wf_to_wf_01)  # 输入网址
		time.sleep(3)
		self.wd.find_element_by_css_selector("[class*=el-button][class*=view-btn-add]").click()  # 点击添加流程
		time.sleep(2.5)
		self.wd.find_element_by_css_selector(self.find_Element(1, 1, "字符串")).send_keys("123")  # 字符串字段里面输入123
		# self.wd.find_element_by_css_selector(self.find_Element(1,2,"用户信息")).click()  # 点击用户信息字段，选择管理员，点击保存
		# ele = self.wd.find_element_by_css_selector('[data-id*="admin_pretest"]')  # 选择管理员，点击保存
		# ele.click()
		# time.sleep(2)
		# ele1 = self.wd.find_element_by_css_selector(".ui-helper-clearfix.ui-dialog-buttonpane>div>button"
		#                                      ":nth-child(2)")  # 点击保存组织架构弹窗
		# ele1.click()
		self.wd.find_element_by_css_selector(self.find_Element(2, 1, "数字")).send_keys("456")
		ran_str = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=10))
		self.wd.find_element_by_css_selector(self.find_Element(3, 2, "文本")).send_keys(ran_str)
		self.wd.find_element_by_css_selector(".executor-add i").click()  # 点击添加联系人
		time.sleep(2)
		self.wd.find_element_by_css_selector('[data-id*="admin_pretest"] label').click()  # 选择管理员本身
		time.sleep(1)
		self.wd.find_element_by_css_selector(".ui-helper-clearfix.ui-dialog-buttonpane>div>button"
		                                     ":nth-child(2)").click()  # 点击组织架构弹窗里面的确定
		time.sleep(1)
		self.wd.find_element_by_css_selector("button.button-nextworkflow").click()  # 点击提交流程
		time.sleep(2)
		self.wd.get(environment + wf_to_wf_02)  # 输入网址，进入接收器的应用
		self.wd.refresh()
		time.sleep(1)
		self.wd.refresh()
		res_text = self.wd.find_element_by_css_selector("div.el-table__body-wrapper.is-scrolling-none tbody>"
		                                                "tr:nth-child(1)>td:nth-child(3) span").text  # 查看列表页的数据是不是之前触发器的数据
		self.wd.get(environment + rulu_page)  # 回到规则引擎界面
		rulu_time_get = self.wd.find_element_by_css_selector(
			'[role*="alert"]>tr:nth-child(7)>td:nth-child(4)').text  # 获取触发时间
		now_time = str(datetime.now())
		now_time_year = now_time[0:4]  # 当前时间的年份
		rulu_time = '{}-{}'.format(now_time_year, rulu_time_get)  # 拼接成完整的时间如：2019-01-02 20:30:07
		timeArray = time.strptime(rulu_time, "%Y-%m-%d %H:%M:%S")
		timeStamp = int(time.mktime(timeArray))  # 在规则列表页获取到的时间转为时间戳
		a = int(time.time())  # 获取当前时间的时间戳,取整数部分
		if ran_str == res_text:
			if timeStamp in range((a - 60), (a + 60)):  # 时间戳在系统时间的前后70秒
				print("接收器的数据和触发时间都正确")
			else:
				raise Exception("接收器的数据正确但是触发时间异常：规则的时间是：%s，系统的时间是：%s" %
				                (rulu_time_get, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a))))
		else:
			if timeStamp in range((a - 60), (a + 60)):  # 时间戳在系统时间的前后70秒
				raise Exception("接收器的数据异常，触发时间正确：触发器的数据是：%s，接收器的数据是：%s"
				                % (ran_str, res_text))
			else:
				raise Exception("触发时间和接收器的数据都不正确：规则的时间是：%s，系统的时间是：%s,"
				                "触发器的数据是：%s，接收器的数据是：%s" %
				                (rulu_time_get, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a)), ran_str,
				                 res_text))

	def df_to_df(self, environment):
		self.wd.get(environment + df_to_df_01)  # 输入网址
		time.sleep(3)
		self.wd.find_element_by_css_selector("[class*=el-button][class*=view-btn-add]").click()  # 点击添加数据
		time.sleep(2.5)
		self.wd.find_element_by_css_selector(self.find_Element(1, 1, "字符串")).send_keys("123")  # 字符串字段里面输入123
		# self.wd.find_element_by_css_selector(self.find_Element(1,2,"用户信息")).click()  # 点击用户信息字段，选择管理员，点击保存
		# ele = self.wd.find_element_by_css_selector('[data-id*="admin_pretest"]')  # 选择管理员，点击保存
		# ele.click()
		# time.sleep(2)
		# ele1 = self.wd.find_element_by_css_selector(".ui-helper-clearfix.ui-dialog-buttonpane>div>button"
		#                                      ":nth-child(2)")  # 点击保存组织架构弹窗
		# ele1.click()
		self.wd.find_element_by_css_selector(self.find_Element(2, 1, "数字")).send_keys("456")
		ran_str = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=10))
		self.wd.find_element_by_css_selector(self.find_Element(3, 2, "文本")).send_keys(ran_str)
		self.wd.find_element_by_css_selector(".button-savedataflow").click()
		time.sleep(2)
		self.wd.get(environment + df_to_df_02)  # 输入网址，进入接收器的应用
		self.wd.refresh()
		time.sleep(1)
		res_text = self.wd.find_element_by_css_selector("div.el-table__body-wrapper.is-scrolling-none tbody>"
		                                                "tr:nth-child(1)>td:nth-child(3) span").text  # 查看列表页的数据是不是之前触发器的数据
		self.wd.get(environment + rulu_page)  # 回到规则引擎界面
		rulu_time_get = self.wd.find_element_by_css_selector(
			'[role*="alert"]>tr:nth-child(6)>td:nth-child(4)').text  # 获取触发时间
		now_time = str(datetime.now())
		now_time_year = now_time[0:4]  # 当前时间的年份
		rulu_time = '{}-{}'.format(now_time_year, rulu_time_get)  # 拼接成完整的时间如：2019-01-02 20:30:07
		timeArray = time.strptime(rulu_time, "%Y-%m-%d %H:%M:%S")
		timeStamp = int(time.mktime(timeArray))  # 在规则列表页获取到的时间转为时间戳
		a = int(time.time())  # 获取当前时间的时间戳,取整数部分
		if ran_str == res_text:
			if timeStamp in range((a - 60), (a + 60)):  # 时间戳在系统时间的前后70秒
				print("接收器的数据和触发时间都正确")
			else:
				raise Exception("接收器的数据正确但是触发时间异常：规则的时间是：%s，系统的时间是：%s" %
				                (rulu_time_get, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a))))
		else:
			if timeStamp in range((a - 60), (a + 60)):  # 时间戳在系统时间的前后70秒
				raise Exception("接收器的数据异常，触发时间正确：触发器的数据是：%s，接收器的数据是：%s"
				                % (ran_str, res_text))
			else:
				raise Exception("触发时间和接收器的数据都不正确：规则的时间是：%s，系统的时间是：%s,"
				                "触发器的数据是：%s，接收器的数据是：%s" %
				                (rulu_time_get, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a)), ran_str,
				                 res_text))

	def df_to_wf(self, environment):
		self.wd.get(environment + df_to_wf_01)  # 输入网址
		time.sleep(3)
		self.wd.find_element_by_css_selector("[class*=el-button][class*=view-btn-add]").click()  # 点击添加数据
		time.sleep(2.5)
		self.wd.find_element_by_css_selector(self.find_Element(1, 1, "字符串")).send_keys("123")  # 字符串字段里面输入123
		# self.wd.find_element_by_css_selector(self.find_Element(1,2,"用户信息")).click()  # 点击用户信息字段，选择管理员，点击保存
		# ele = self.wd.find_element_by_css_selector('[data-id*="admin_pretest"]')  # 选择管理员，点击保存
		# ele.click()
		# time.sleep(2)
		# ele1 = self.wd.find_element_by_css_selector(".ui-helper-clearfix.ui-dialog-buttonpane>div>button"
		#                                      ":nth-child(2)")  # 点击保存组织架构弹窗
		# ele1.click()
		self.wd.find_element_by_css_selector(self.find_Element(2, 1, "数字")).send_keys("456")
		ran_str = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=10))
		self.wd.find_element_by_css_selector(self.find_Element(3, 2, "文本")).send_keys(ran_str)
		self.wd.find_element_by_css_selector(".button-savedataflow").click()
		time.sleep(2)
		self.wd.get(environment + df_to_wf_02)  # 输入网址，进入接收器的应用
		self.wd.refresh()
		time.sleep(1)
		self.wd.refresh()
		res_text = self.wd.find_element_by_css_selector("div.el-table__body-wrapper.is-scrolling-none tbody>"
		                                                "tr:nth-child(1)>td:nth-child(3) span").text  # 查看列表页的数据是不是之前触发器的数据
		self.wd.get(environment + rulu_page)  # 回到规则引擎界面
		rulu_time_get = self.wd.find_element_by_css_selector(
			'[role*="alert"]>tr:nth-child(5)>td:nth-child(4)').text  # 获取触发时间
		# rulu_time = rulu_time.split(" ")[1][0:5]
		# now_time = str(datetime.now())
		# now_time = now_time.split(" ")[1][0:5]
		now_time = str(datetime.now())
		now_time_year = now_time[0:4]  # 当前时间的年份
		rulu_time = '{}-{}'.format(now_time_year, rulu_time_get)  # 拼接成完整的时间如：2019-01-02 20:30:07
		timeArray = time.strptime(rulu_time, "%Y-%m-%d %H:%M:%S")
		timeStamp = int(time.mktime(timeArray))  # 在规则列表页获取到的时间转为时间戳
		a = int(time.time())  # 获取当前时间的时间戳,取整数部分
		if ran_str == res_text:
			if timeStamp in range((a - 60), (a + 60)):  # 时间戳在系统时间的前后70秒
				print("接收器的数据和触发时间都正确")
			else:
				raise Exception("接收器的数据正确但是触发时间异常：规则的时间是：%s，系统的时间是：%s" %
				                (rulu_time_get, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a))))
		else:
			if timeStamp in range((a - 60), (a + 60)):  # 时间戳在系统时间的前后70秒
				raise Exception("接收器的数据异常，触发时间正确：触发器的数据是：%s，接收器的数据是：%s"
				                % (ran_str, res_text))
			else:
				raise Exception("触发时间和接收器的数据都不正确：规则的时间是：%s，系统的时间是：%s,"
				                "触发器的数据是：%s，接收器的数据是：%s" %
				                (rulu_time_get, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a)), ran_str,
				                 res_text))

	def df_to_remind(self, environment):
		self.wd.get(environment + df_to_remind)  # 输入网址
		time.sleep(3)
		self.wd.find_element_by_css_selector("[class*=el-button][class*=view-btn-add]").click()  # 点击添加数据
		time.sleep(2.5)
		self.wd.find_element_by_css_selector(self.find_Element(1, 1, "字符串")).send_keys("123")  # 字符串字段里面输入123
		# self.wd.find_element_by_css_selector(self.find_Element(1, 2, "用户信息")).click()  # 点击用户信息字段，选择管理员，点击保存
		# ele = self.wd.find_element_by_css_selector('[data-id*="admin_pretest"]')  # 选择管理员，点击保存
		# ele.click()
		# time.sleep(2)
		# ele1 = self.wd.find_element_by_css_selector(".ui-helper-clearfix.ui-dialog-buttonpane>div>button"
		#                                             ":nth-child(2)")  # 点击保存组织架构弹窗
		# ele1.click()
		self.wd.find_element_by_css_selector(self.find_Element(2, 1, "数字")).send_keys("456")
		ran_str = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=10))
		self.wd.find_element_by_css_selector(self.find_Element(3, 2, "文本")).send_keys(ran_str)
		self.wd.find_element_by_css_selector(".button-savedataflow").click()
		time.sleep(2)
		self.wd.get(environment + rulu_page)  # 回到规则引擎界面
		self.wd.find_element_by_css_selector('tbody[role*="alert"]>tr:nth-child(4)'
		                                     '>td:nth-child(6)>button:nth-child(1)').click()  # 点击设置时间的小闹钟
		time.sleep(1)
		time_input = self.wd.find_element_by_css_selector("#otime")  # 填时间的input框
		time.sleep(1.5)
		time_input.clear()

		# 触发的时间加1分钟
		a = time.time()  # 获取当前时间的时间戳
		time_in = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a + 60)))  # 将这样的时间取到分钟2019-01-02 22:43:30
		time_in_hm = time_in[11:16]  # 在小闹钟里面填上小时:分钟；hh:mm

		time_input.send_keys(time_in_hm)
		self.wd.find_element_by_css_selector(".ui-helper-clearfix.ui-dialog-buttonpane"
		                                     ">div>button:nth-child(2)").click()
		time.sleep(2)
		self.wd.find_element_by_css_selector("#ui-id-2~div>div>button").click()  # 保存成功点击关闭
		# self.wd.get(environment + df_to_remind_01)
		print("等待数据触发中...")
		time.sleep(90)
		print("等待时间结束...")
		self.wd.refresh()
		rulu_time = self.wd.find_element_by_css_selector(
			'[role*="alert"]>tr:nth-child(4)>td:nth-child(4)').text  # 获取触发时间
		rulu_time = rulu_time[6:11]

		self.wd.get(environment + df_to_remind)

		yellow = self.wd.find_element_by_css_selector("div.el-table__body-wrapper.is-scrolling-none tbody"
		                                              ">tr:nth-child(1)>td:nth-child(2)>div>"
		                                              "div[class*=column-remind]")  # 是否有标黄的元素
		if rulu_time == time_in_hm:
			if yellow:
				print("触发时间正确,数据正常标黄")
			else:
				raise Exception("触发时间正确，但是数据没有标黄")
		else:
			if yellow:
				raise Exception("数据正常标黄，但触发时间错误:规则的触发时间是：%s，设置的触发时间是：%s" % (rulu_time, time_in_hm))
			else:
				raise Exception("触发时间异常，数据也没有标黄:规则的时间是：%s，设置的触发时间是：%s" % (rulu_time, time_in_hm))

	def zy_to_wf(self, environment):
		self.wd.get(environment + zy_to_wf_01)  # 输入网址
		time.sleep(3)
		self.wd.find_element_by_css_selector("[class*=el-button][class*=view-btn-add]").click()  # 点击添加数据
		time.sleep(2.5)
		self.wd.find_element_by_css_selector(self.find_Element(1, 1, "字符串")).send_keys("123")  # 字符串字段里面输入123
		# self.wd.find_element_by_css_selector(self.find_Element(1,2,"用户信息")).click()  # 点击用户信息字段，选择管理员，点击保存
		# ele = self.wd.find_element_by_css_selector('[data-id*="admin_pretest"]')  # 选择管理员，点击保存
		# ele.click()
		# time.sleep(2)
		# ele1 = self.wd.find_element_by_css_selector(".ui-helper-clearfix.ui-dialog-buttonpane>div>button"
		#                                      ":nth-child(2)")  # 点击保存组织架构弹窗
		# ele1.click()
		self.wd.find_element_by_css_selector(self.find_Element(2, 1, "数字")).send_keys("456")
		ran_str = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=10))
		self.wd.find_element_by_css_selector(self.find_Element(3, 2, "文本")).send_keys(ran_str)
		self.wd.find_element_by_css_selector(".button-savedataflow").click()
		time.sleep(2)
		self.wd.get(environment + zy_to_wf_02)  # 输入网址，进入接收器的应用
		self.wd.refresh()
		time.sleep(2)
		self.wd.refresh()
		res_text = self.wd.find_element_by_css_selector("div.el-table__body-wrapper.is-scrolling-none tbody>"
		                                                "tr:nth-child(1)>td:nth-child(3) span").text  # 查看列表页的数据是不是之前触发器的数据
		self.wd.get(environment + rulu_page)  # 回到规则引擎界面
		rulu_time_get = self.wd.find_element_by_css_selector(
			'[role*="alert"]>tr:nth-child(3)>td:nth-child(4)').text  # 获取触发时间
		now_time = str(datetime.now())
		now_time_year = now_time[0:4]  # 当前时间的年份
		rulu_time = '{}-{}'.format(now_time_year, rulu_time_get)  # 拼接成完整的时间如：2019-01-02 20:30:07
		timeArray = time.strptime(rulu_time, "%Y-%m-%d %H:%M:%S")
		timeStamp = int(time.mktime(timeArray))  # 在规则列表页获取到的时间转为时间戳
		a = int(time.time())  # 获取当前时间的时间戳,取整数部分
		if ran_str == res_text:
			if timeStamp in range((a - 60), (a + 60)):  # 时间戳在系统时间的前后70秒
				print("接收器的数据和触发时间都正确")
			else:
				raise Exception("接收器的数据正确但是触发时间异常：规则的时间是：%s，系统的时间是：%s" %
				                (rulu_time_get, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a))))
		else:
			if timeStamp in range((a - 60), (a + 60)):  # 时间戳在系统时间的前后70秒
				raise Exception("接收器的数据异常，触发时间正确：触发器的数据是：%s，接收器的数据是：%s"
				                % (ran_str, res_text))
			else:
				raise Exception("触发时间和接收器的数据都不正确：规则的时间是：%s，系统的时间是：%s,"
				                "触发器的数据是：%s，接收器的数据是：%s" %
				                (rulu_time_get, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a)), ran_str,
				                 res_text))

	def cycle_to_df(self, environment):
		self.wd.get(environment + rulu_page_cycle_to_df1)
		time_input = self.wd.find_element_by_css_selector(".startTime")
		time.sleep(1.5)
		time_input.clear()  # 清除掉开始时间里面的时间

		# 触发的时间加1分钟
		# now_time = str(datetime.now())
		# now_time_h = now_time.split(" ")[1][0:2]
		# now_time_m = str(int(now_time.split(" ")[1][3:5]) + 1)
		# now_time_y = now_time.split(" ")[0]
		# time_in = '{} {}:{}'.format(now_time_y, now_time_h, now_time_m)
		a = time.time()  # 获取当前时间的时间戳
		time_in = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a + 60)))  # 将这样的时间取到分钟2019-01-02 22:43:30
		time_in_hmrhm = time_in[:-3]  # 周期规则首次触发时间设置如2019-01-02 23:28
		print(time_in_hmrhm)
		time_input.send_keys(time_in_hmrhm)  # 填上系统时间加一分钟的时间

		self.wd.find_element_by_css_selector("#step_next").click()  # 相当于保存
		self.wd.get(environment + rulu_page_cycle_to_df2)  # 跳到规则配置的第五步保存

		self.wd.find_element_by_css_selector("#step_next").click()  # 保存规则,以上创建好规则

		time.sleep(90)
		self.wd.get(environment + rulu_page)  # 回到规则引擎界面
		rulu_time = self.wd.find_element_by_css_selector(
			'[role*="alert"]>tr:nth-child(2)>td:nth-child(4)').text  # 获取触发时间
		rulu_time = rulu_time.split(" ")[1][0:5]
		self.wd.get(environment + cycle_to_df)  # 进入到from，验证数据
		time.sleep(5)
		self.wd.find_element_by_css_selector(".el-table__fixed>.el-table__fixed-body-wrapper>table tbody"
		                                     ">tr:nth-child(1)>td:nth-child(2)>div>div").click()  # 点击第一行的关键字，进入详情页
		time.sleep(1)
		self.wd.find_element_by_css_selector("div.form-toolbar>div:nth-child(1)"
		                                     ">button:nth-child(2)").click()  # 点击历史记录
		history_time = self.wd.find_element_by_css_selector("div.history-time")
		history_time = history_time.text[0:5]
		if str(history_time) == str(time_in_hmrhm[-5:]) == str(rulu_time):
			print("周期触发正常")
		else:
			raise Exception(
				"周期触发的时间不正常，规则设置的触发时间是%s，数据填入的时间是%s,规则实际的触发时间是%s" % (time_in_hmrhm[-5:], history_time, rulu_time))

	def cycle_to_wf(self, environment):
		self.wd.get(environment + rulu_page_cycle_to_wf1)
		time_input = self.wd.find_element_by_css_selector(".startTime")
		time.sleep(1.5)
		time_input.clear()  # 清除掉开始时间里面的时间

		# # 触发的时间加1分钟
		# now_time = str(datetime.now())
		# now_time_h = now_time.split(" ")[1][0:2]
		# now_time_m = str(int(now_time.split(" ")[1][3:5]) + 1)
		# now_time_y = now_time.split(" ")[0]
		# time_in = '{} {}:{}'.format(now_time_y, now_time_h, now_time_m)
		a = time.time()  # 获取当前时间的时间戳
		time_in = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a + 60)))  # 将这样的时间取到分钟2019-01-02 22:43:30
		time_in_hmrhm = time_in[:-3]  # 周期规则首次触发时间设置如2019-01-02 23:28
		time_input.send_keys(time_in_hmrhm)  # 填上系统时间加一分钟的时间

		self.wd.find_element_by_css_selector("#step_next").click()  # 相当于保存
		self.wd.get(environment + rulu_page_cycle_to_wf2)  # 跳到规则配置的第五步保存

		self.wd.find_element_by_css_selector("#step_next").click()  # 保存规则,以上创建好规则

		time.sleep(90)
		self.wd.get(environment + rulu_page)  # 回到规则引擎界面
		rulu_time = self.wd.find_element_by_css_selector(
			'[role*="alert"]>tr:nth-child(1)>td:nth-child(4)').text  # 获取触发时间
		rulu_time = rulu_time.split(" ")[1][0:5]
		self.wd.get(environment + cycle_to_wf)  # 进入到from，验证数据
		time.sleep(3)
		accpet_time = self.wd.find_element_by_css_selector("div.el-table__body-wrapper.is-scrolling-none tbody>"
		                                                   "tr:nth-child(1)>td:nth-child(4) span").text

		accpet_time = accpet_time.split(" ")[1][0:5]
		if str(accpet_time) == str(time_in_hmrhm[-5:]) == str(rulu_time):
			print("周期触发正常")
		else:
			raise Exception("周期触发的时间不正常，规则设置的触发时间是%s，数据填入的时间是%s,规则实际的触发时间是%s"
			                % (time_in_hmrhm[-5:], accpet_time, rulu_time))

	# 下面是企业主页的用例
	def get_newuser(self, environment, number):
		"""添加用户，检查【新增用户】数量是否增加"""
		self.wd.get(environment + companyinfo)
		user = self.wd.find_element_by_css_selector("tbody>[class*=el-table__row]:nth-child(1)>td:nth-child(2)>div")
		time.sleep(2)
		user_nunber = int(user.text)
		print("没新增用户之前，运营概况里面【新增人数】是:{} ".format(user_nunber))
		# 下面调用函数添加用户
		Web_interface().add_users(environment, number)
		time.sleep(2)
		self.wd.refresh()
		new_user = self.wd.find_element_by_css_selector("tbody>[class*=el-table__row]:nth-child(1)>td:nth-child(2)>div")
		time.sleep(1)
		new_user_number = int(new_user.text)
		print("新增{}个用户之后，运营概况里面【新增人数】是:{} ".format(number, new_user_number))
		if len(Web_interface().create_users) == int(new_user_number - user_nunber):
			print("添加的用户数是：{}，多出的用户数是：{}。相等，正确".format(number, new_user_number - user_nunber))
		else:
			raise Exception("新添加的用户是 %s 人，页面上多出来的用户数是 %s " % (number, (new_user_number - user_nunber)))

	def get_webactivepeople(self, environment, number):
		"""添加用户，查看【新增用户】【web活跃用户】【总活跃用户】增加的人数知否正常"""
		self.wd.get(environment + companyinfo)  # 登录到相应的页面
		self.wd.refresh()
		time.sleep(3)
		user_xinzen = self.wd.find_element_by_css_selector(
			"tbody>[class*=el-table__row]:nth-child(1)>td:nth-child(2)>div").text  # 获取3个数据
		uesr_webactive = self.wd.find_element_by_css_selector(
			"tbody>[class*=el-table__row]:nth-child(1)>td:nth-child(3)>div").text
		uesr_active_all = self.wd.find_element_by_css_selector(
			"tbody>[class*=el-table__row]:nth-child(1)>td:nth-child(6)>div").text
		print(
			"新增用户前:【新增用户】的人数是：{};【Web活跃用户】的人数是：{};【总活跃用户】的人数是：{}".format(user_xinzen, uesr_webactive, uesr_active_all))
		print(">>>>>>>>>>>>>>>>>>>下面开始创建用户>>>>>>>>>>>>>>>>>>>")
		Web_interface().active_people(environment, number)  # 调用函数添加数据
		print(">>>>>>>>>>>>>>>用户创建完成，并成功登录>>>>>>>>>>>>>>>>")
		self.wd.refresh()
		time.sleep(3)
		user_xinzen_new = self.wd.find_element_by_css_selector(
			"tbody>[class*=el-table__row]:nth-child(1)>td:nth-child(2)>div").text  # 重新获取数据
		uesr_webactive_new = self.wd.find_element_by_css_selector(
			"tbody>[class*=el-table__row]:nth-child(1)>td:nth-child(3)>div").text
		uesr_active_all_new = self.wd.find_element_by_css_selector(
			"tbody>[class*=el-table__row]:nth-child(1)>td:nth-child(6)>div").text
		print("新增用户后:【新增用户】的人数是：{};【Web活跃用户】的人数是：{};【总活跃用户】的人数是：{}".format(user_xinzen_new, uesr_webactive_new,
		                                                                   uesr_active_all_new))
		if int(user_xinzen_new) - int(user_xinzen) == int(number):
			if int(uesr_webactive_new) - int(uesr_webactive) == int(number):
				if int(uesr_active_all_new) - int(uesr_active_all) == int(number):
					print(
						"【新增用户】的增加数量是:{}，正确；【web活跃用户】的增加数量是:{}，正确；【总活跃用户】的增加数量是:{},正确".format(int(number), int(number),
						                                                                      int(number)))
				else:
					raise Exception("【新增用户】的增加数量是:{}；正确。【web活跃用户】的增加数量是:{}，正确。但是【总活跃用户】的增加数量是:{},异常".format(int(number),
					                                                                                        int(number),
					                                                                                        (int(
						                                                                                        uesr_active_all_new) - int(
						                                                                                        uesr_active_all))))
			else:
				raise Exception("【新增用户】的增加数量是:{}；正确。但是【web活跃用户】的增加数量是:{}，异常".format(int(number), (
							int(user_xinzen_new) - int(user_xinzen))))

		else:
			raise Exception("【新增用户】的增加数量是:{}；异常".format(int(user_xinzen_new) - int(user_xinzen)))

	def Theme_Colors(self, environment):
		self.wd.get(environment + themeColor)  # 登录到相应的页面
		self.wd.refresh()
		time.sleep(1)
		skin_list = self.wd.find_element_by_css_selector("ul.skin-list")
		item = skin_list.find_elements_by_css_selector("li")  # 找每一个主题颜色，返回值是一个列表
		i = random.randint(0, 8)
		get_renyi = item[i]  # 任何获取一个主题颜色
		time.sleep(1)
		i_name = get_renyi.find_element_by_css_selector("li p").text  # 获取刚刚选中的主题名
		time.sleep(1)
		get_renyi.find_element_by_css_selector("li div").click()  # 并点击
		self.wd.find_element_by_css_selector("button.el-button.el-button--primary.el-button--medium").click()
		self.wd.find_element_by_css_selector("div.el-message-box__btns>button:nth-child(1)").click()
		check = get_renyi.find_element_by_css_selector('li div i[class*="icon-check"]')  # 选中之后胡UI有一个icon-check的属性
		if check:
			print("成功选中主题为【{}】".format(i_name))
		else:
			raise Exception("主题没有被选中或没有保存成功")
		session = Web_interface().login_api(environment)
		c = Web_interface().add_user(session, environment)
		print("成功创建用户{}".format(c[-1]))
		entele = self.wd.find_element_by_css_selector("i.icon-xiala- ")  # 选中头像右侧的下拉按钮
		time.sleep(2)
		entele.click()  # 点击头像右侧的下拉按钮
		self.wd.find_element_by_css_selector("i.icon-guanji").click()  # 选中退出按钮并点击
		self.wd.find_element_by_css_selector(
			"#x-header-app>div:nth-child(4)>div:nth-child(2) footer span:nth-child(2)").click()  # 退出账号
		self.user_login(environment, nsername=c[-1], password="11111111", enterprise="pre测试企业")  # 新创建的用户登录

		entele = self.wd.find_element_by_css_selector("i.icon-xiala- ")  # 选中头像右侧的下拉按钮
		time.sleep(2)
		entele.click()  # 点击头像右侧的下拉按钮
		zhutis = self.wd.find_element_by_css_selector("li.theme-swither")  # 获取主题
		ActionChains(self.wd).move_to_element(zhutis).perform()  # 悬停至换肤
		time.sleep(1)
		# zhuti = zhutis.find_elements_by_css_selector("li")
		# for k in zhuti:
		# 	color_name = k.text
		# 	print(color_name)
		# 	print(k.text)
		# 	check_in = k.find_element_by_css_selector("i.fa-check-square")
		# 	if color_name == i_name and check_in:
		# 		print("新建用户的主题是系统管理员设置的主题：{}".format(color_name))
		# 		break
		check_in_name = self.wd.find_element_by_xpath('//*[@class="square-icon fa fa-check-square"]/..').text
		# 上面只能通过下节节点找上节节点，被选中之后的，会有一个属性fa-check-square，看这个节点的上节节点是的主题名称是不是之前管理员选的主题，这里不需要用for，因为每次选中都会有一个独特的属性
		if check_in_name == i_name:
			print("新用户的主题是管理员设置的主题：{}。正确".format(check_in_name))
		else:
			raise Exception("新用户的主题不是管理员设置的主题，管理员设置的主题是{}，自己实际的主题是{}".format(i_name, check_in_name))
		self.wd.get(environment + "/user/signout")
		# 再次回到管理员页面，方便下一个用例执行
		self.user_login(environment, nsername="admin_pretest", password="11111111", enterprise="pre测试企业")  # 新创建的用户登录

	def style_sheet(self, environment):
		self.wd.get(environment + stylesheet)  # 登录到相应的页面
		self.wd.refresh()
		time.sleep(1)
		self.wd.find_element_by_css_selector(".el-button--medium.el-button--default").click()
		self.wd.find_element_by_css_selector("div.el-message-box__btns>button:nth-child(2)").click()  # 点击保存
		time.sleep(1)
		self.wd.find_element_by_css_selector("div.el-message-box__btns>button:nth-child(1)").click()  # 点击关闭
		list_code = Web_interface().list_style(environment)
		if list_code == "":
			print("重置样式功能正常")
		else:
			raise Exception("重置样式功能正常或获取样式的接口异常")
		ran_str = "测试样式表_" + (
			''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=6)))
		self.wd.find_element_by_css_selector(".edit-panel.el-textarea textarea").send_keys(ran_str)
		self.wd.find_element_by_css_selector("button.el-button--primary.el-button--medium").click()
		# 点击保存按钮
		self.wd.find_element_by_css_selector("div.el-message-box__btns>button:nth-child(2)").click()
		# 点击确定弹窗
		time.sleep(1)
		self.wd.find_element_by_css_selector("div.el-message-box__btns>button:nth-child(1)").click()
		# 点击关闭弹窗
		list_code = Web_interface().list_style(environment)
		if list_code == ran_str:
			print("保存样式功能正常")
		else:
			raise Exception("保存样式功能异常：填入的样式内容是：{}；获取到的样式内容是：{}".format(ran_str, list_code))

	# def logo_upload(self,environment):
	# 	self.wd.get(environment + logo)  # 登录到相应的页面
	# 	try:
	# 		exist_img = self.wd.find_element_by_css_selector("ul.img-list")
	# 		self.wd.find_element_by_css_selector("div.upload-container>button:nth-child(4)").click()
	# 		self.wd.find_element_by_css_selector("div.el-message-box__btns>button:nth-child(2)").click()
	# 		time.sleep(2)
	# 		#页面元素在还没有被立刻删掉
	# 		upload_container = self.wd.find_element_by_css_selector("div.upload-container")
	# 		img_list = upload_container.find_elements_by_css_selector("ul.img-list")
	# 		print(img_list)
	# 		# try:
	# 		# 	#检查图片是否确实被删除
	# 		# 	exist_img = self.wd.find_element_by_css_selector("ul.img-list")
	# 		# 	print("之前的图片没有被删除")
	# 		# except:
	# 		# 	print("之前的图片被成功删除")
	# 	except:
	# 		self.wd.find_element_by_css_selector("div.upload-btn").click()
	# 		shell = win32com.client.Dispatch("WScript.shell")
	# 		time.sleep(2)
	# 		shell.sendkeys(r"d:\1.jpg" + "\r\n")
	# 		try:
	# 			exist_img = self.wd.find_element_by_css_selector("ul.img-list")
	# 			print("上传成功")
	# 			#确认有图片了之后在进行下面的操作
	# 			print(111111)
	# 		except:
	# 			print("上传失败")

	def logo_upload(self, environment):
		self.wd.get(environment + logo)  # 登录到相应的页面
		time.sleep(2)
		upload_container_before = self.wd.find_element_by_css_selector("div.upload-container")
		img_lists_before = upload_container_before.find_elements_by_css_selector("ul.img-list")
		# 如果之前里面有logo，就会有一个上面这个节点，加s找比较方便，通过判断列表是不是为空,确定原来是不是有logo，要么是1，要么是0
		if img_lists_before != []:
			img_list = self.wd.find_element_by_css_selector("ul.img-list")
			# 下面就是要知道到底有几个logo
			img_item = img_list.find_elements_by_css_selector("li.img-item")
			times = len(img_item)
			print("里面一共存在{}张logo图片".format(times))
			# i就是一共有几个logo
			for i in range(0, times):
				# 把所有的logo删除掉d:\1.jpg

				time.sleep(0.5)
				self.wd.find_element_by_css_selector("div.upload-container>button:nth-child(4)").click()
				time.sleep(0.5)
				self.wd.find_element_by_css_selector("div.el-message-box__btns>button:nth-child(2)").click()
			self.wd.refresh()
			time.sleep(1)
			upload_container_after = self.wd.find_element_by_css_selector("div.upload-container")
			img_lists_after = upload_container_after.find_elements_by_css_selector("ul.img-list")
			if img_lists_after == []:
				# 检查下是不是删除干净了
				print("logo删除功能正常。之前的logo都删掉了")
			else:
				raise Exception("logo没有完全清空")
		# 下面开始上传图片
		self.wd.find_element_by_css_selector("div.upload-btn").click()
		shell = win32com.client.Dispatch("WScript.shell")

		time.sleep(3)
		shell.sendkeys(r"d:\1.jpg" + "\r\n")
		time.sleep(1)
		upload_container_end = self.wd.find_element_by_css_selector("div.upload-container")
		img_lists_end = upload_container_end.find_elements_by_css_selector("ul.img-list")
		if img_lists_end != []:
			print("上传成功")
		# 确认有图片了之后在进行下面的操作
		else:
			raise Exception("logo上传失败")

		# 下面要选择节点，保存图片
		self.wd.find_element_by_css_selector("span.el-input__suffix").click()  # 点击组织架构下拉按钮
		time.sleep(1)
		self.wd.find_element_by_css_selector(".unit-panel>ul.x-tree>li>i").click()  # 选中根节点
		time.sleep(1)
		self.wd.find_element_by_css_selector("div.upload-container>button:nth-child(5)").click()  # 点击保存
		time.sleep(0.5)
		self.wd.find_element_by_css_selector("div.el-message-box>div:nth-child(3)>button:nth-child(1)").click()  # 差掉弹窗
		# 下面就是验证图片是不是上传成功
		self.wd.refresh()
		time.sleep(1)
		upload_end = self.wd.find_element_by_css_selector("div.upload-container")
		img_end = upload_end.find_elements_by_css_selector("ul.img-list")
		if img_end != []:
			print("logo上传并保存成功")
		# 确认有图片了之后在进行下面的操作
		else:
			raise Exception("logo保存失败")

		# 下面是验证用户是不是使用的是管理员设置的图片，这里就是验证一下管理员的logo
		self.wd.get(environment + appcenter)
		time.sleep(2)
		img_name = ((datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "_logo.png").replace(":", "-")
		print(img_name)
		self.wd.get_screenshot_as_file(r"D:\auto_test\{}".format(img_name))
		# ele_logo = self.wd.find_element_by_css_selector('[href*="/appcenter"][class*="logo"]>img')
		# time.sleep(1)
		# ele_logo.screenshot("button.png")
		filenames = os.listdir(r"D:\auto_test")
		isExist = False
		print(filenames)
		# in 方法最简单
		# if img_name in filenames:
		#     print("截图成功")
		# else:
		#     raise Exception("截图失败")
		for filename in filenames:
			if filename == img_name:
				print('截图保存成功')
				break
		else:
			raise Exception("截图保存失败")

	# for...else方法也是可以的，之前没有这么用过

	def role_authorization(self, environment):
		self.wd.get(environment + role)  # 登录到相应的页面
		time.sleep(2)
		# 下面是判断之前里面有没有设置
		tbody = self.wd.find_element_by_css_selector("#editTablePanelList")
		tr_list = tbody.find_elements_by_css_selector("tr")
		if len(tr_list) > 1:
			for i in range(0, len(tr_list)):
				time.sleep(1)
				self.wd.find_element_by_css_selector('a.del[title*= "删除"]').click()
				time.sleep(1)
				self.wd.find_element_by_css_selector("div.ui-dialog-buttonset>button").click()
			text_none = self.wd.find_element_by_css_selector("#editTablePanelList>tr>td").text
			if text_none == "暂无数据显示":
				print("之前的数据被清空")
			else:
				raise Exception("之前的数据没有被成功删除")
		else:
			tr_odd = self.wd.find_element_by_css_selector("#editTablePanelList>tr")
			td = tr_odd.find_elements_by_css_selector("td")
			if len(td) > 1:
				# 里面存在一个配置
				self.wd.find_element_by_css_selector('a.del[title*= "删除"]').click()
				time.sleep(1)
				self.wd.find_element_by_css_selector("div.ui-dialog-buttonset>button").click()
				text_none_new = self.wd.find_element_by_css_selector("#editTablePanelList>tr>td").text
				if text_none_new == "暂无数据显示":
					print("之前的数据被清空")
				else:
					raise Exception("之前的数据没有被成功删除")
		# 上面的操作是清空之前的数据，下面的数据是填入数据
		session = Web_interface().login_api(environment)
		c = Web_interface().add_user(session, environment)
		print("成功创建用户{}".format(c[-1]))
		self.wd.find_element_by_css_selector(
			"#authorizationList>div:nth-child(1)>div:nth-child(2)>table>tbody>tr:nth-child(1)>td:nth-child(2)>a").click()
		time.sleep(2)
		self.wd.find_element_by_css_selector("#department_Ztree>li>button:nth-child(2)").click()  # 选中根节点
		root_name = self.wd.find_element_by_css_selector("#department_Ztree>li>a>span").text  # 获取根节点的名字
		time.sleep(1)
		self.wd.find_element_by_css_selector("div.ui-dialog-buttonset>button:nth-child(2)").click()  # 点击确定
		time.sleep(1)
		# 下面判断pre测试企业的节点是不是被选中
		check_choice = self.wd.find_element_by_css_selector("#editTablePanelList>tr:nth-child(1)>td:nth-child(1)").text
		if check_choice == root_name:
			print("节点被成功选中")
		else:
			raise Exception("根节点没有被成功选中")
		self.wd.find_element_by_css_selector("#editTablePanelList>tr:nth-child(1)>td:nth-child(2)>a").click()
		time.sleep(1)
		self.wd.find_element_by_css_selector("#orgfield>div:nth-child(1)>div:nth-child(1)>input").send_keys(c[-1])
		time.sleep(2)
		self.wd.find_element_by_css_selector(".o-search-display>ul i").click()  # 勾选组织架构筛选到的人
		time.sleep(1)
		self.wd.find_element_by_css_selector("#orgfield+div>div>button:nth-child(2)").click()  # 点击保存
		time.sleep(1)
		self.wd.find_element_by_xpath(
			'//*[@id="department_dialog"]/../following-sibling::div//div[3]//div//button').click()
		time.sleep(1)
		# 上面是创建一个规则，下面要检查这个规则是不是创建成功
		check_user = self.wd.find_element_by_css_selector(
			"#editTablePanelList>tr:nth-child(1)>td:nth-child(2)>span").text
		check_user = check_user.split("-")[-1]
		if check_user == c[-1]:
			print("授权用户被成功选中")
		else:
			raise Exception("授权用户没有被选中")
		self.wd.get(environment + "/user/signout")
		self.user_login(environment, nsername=c[-1], password="11111111", enterprise="pre测试企业")  # 新创建的用户登录
		self.wd.get(environment + "/enterprise/orgManage")  # 进入到组织架构页面
		time.sleep(2)
		base_uesr = self.wd.find_element_by_css_selector("li.user-tab.active").text
		if base_uesr == "基本用户":
			print("{}用户能正常进入组织架构页面".format(c[-1]))
		else:
			raise Exception("{}用户不能正常进入组织架构页面".format(c[-1]))
		# 上面的功能实现被配置的用户能正常查看组织架构页面
		# 下面要验证没有配置的用户不能正常进入组织架构页面
		self.wd.get(environment + "/user/signout")
		c = Web_interface().add_user(session, environment)
		print("成功创建用户{}".format(c[-1]))
		self.user_login(environment, nsername=c[-1], password="11111111", enterprise="pre测试企业")  # 新创建的用户登录
		self.wd.get(environment + "/enterprise/orgManage")  # 进入到组织架构页面
		time.sleep(2)
		error_404 = self.wd.find_element_by_css_selector("#error_404")
		if error_404:
			print("没有被授权的用户{},不能进入组织架构页面".format(c[-1]))
		else:
			raise Exception("没有被授权的用户{},也能进入组织架构页面".format(c[-1]))
		self.wd.get(environment + "/user/signout")
		# 再次回到管理员页面，方便下一个用例执行
		self.user_login(environment, nsername="admin_pretest", password="11111111", enterprise="pre测试企业")  # 新创建的用户登录


if __name__ == '__main__':
	wo = Web_Lib()
	wo.open_browser()
	wo.user_login("https://www.qycloud.com.cn")
	wo.role_authorization("https://www.qycloud.com.cn")
