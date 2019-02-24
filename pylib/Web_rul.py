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


class Web_rul():
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

	def user_login_init_rul(self, environment, nsername="admin_pretest", password="11111111",
	                        enterprise="pre测试企业"):  # 用户登录
		self.open_browser()
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

		a = time.time()  # 获取当前时间的时间戳
		time_in = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a + 61)))  # 将这样的时间取到分钟2019-01-02 22:43:30
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

		a = time.time()  # 获取当前时间的时间戳
		time_in = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a + 61)))  # 将这样的时间取到分钟2019-01-02 22:43:30
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


if __name__ == '__main__':
	wo = Web_rul()
	wo.open_browser()
	wo.user_login("https://www.qycloud.com.cn")
	wo.cycle_to_df("https://www.qycloud.com.cn")
