#! /usr/bin/env/python3
# coding=utf-8
# @Time    : 2019/2/22  9:31
# @Author  : XueFei
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

class Web_Operation_backstage():
	ROBOT_LIBRARY_SCOPE = 'GLOBAL'

	def __init__(self):
		pass

	def open_browser(self):
		self.wd = webdriver.Chrome()
		self.wd.maximize_window()  # 最大化窗口
		self.wd.implicitly_wait(15)

	def close_browser(self):
		self.wd.quit()

	def user_login_init_backstage(self, environment, nsername="admin_pretest", password="11111111", enterprise="pre测试企业"):  # 用户登录
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
		# 系统管理-组织架构编辑
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
			'//*[@id="department_dialog"]/../following-sibling::div//div[3]//div//button').click()  # 点击关闭
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

	def User_activity_analysis(self, environment):
		# 系统管理-运营概况分析
		self.wd.get(environment + role)  # 登录到相应的页面
		time.sleep(2)
		relatedUser = self.wd.find_element_by_css_selector(".operationOverviewRelatedUser.relatedUser")
		li_list = relatedUser.find_elements_by_css_selector("li")
		if li_list != []:  # 说明里面有之前配过的数据
			print("里面有数据，下面开始删除数据")
			self.wd.find_element_by_css_selector(
				'[data-category*="operationOverview"]+div>table>tbody>tr>td:nth-child(2)>a').click()  # 点击添加
			time.sleep(2)
			self.wd.find_element_by_css_selector("#o-ztree-orgfield>li>button:nth-child(2)").click()  # 全部选中
			time.sleep(2)
			self.wd.find_element_by_css_selector("#o-ztree-orgfield>li>button:nth-child(2)").click()  # 全部取消
			time.sleep(2)
			self.wd.find_element_by_xpath(
				'//*[@id="department_dialog"]/../following-sibling::div//div[3]//div//button[2]').click()
			time.sleep(1)
			self.wd.find_element_by_xpath(
				'//*[@id="department_dialog"]/../following-sibling::div//div[3]//div//button').click()  # 点击关闭
			time.sleep(1)
			# 下面检查数据是不是被删除完
			relatedUser = self.wd.find_element_by_css_selector(".operationOverviewRelatedUser.relatedUser")
			li_list = relatedUser.find_elements_by_css_selector("li")
			if li_list == []:
				print("之前的数据被删除完")
			else:
				raise Exception("之前的数据没有被成功删除")
		print("里面没有数据，下面开始创建数据")
		session = Web_interface().login_api(environment)
		c = Web_interface().add_user(session, environment)
		print("成功创建用户{}".format(c[-1]))
		self.wd.find_element_by_css_selector(
			'[data-category*="operationOverview"]+div>table>tbody>tr>td:nth-child(2)>a').click()  # 点击添加
		time.sleep(2)
		self.wd.find_element_by_css_selector("#orgfield>div:nth-child(1)>div:nth-child(1)>input").send_keys(c[-1])
		time.sleep(2)
		self.wd.find_element_by_css_selector(".o-search-display>ul i").click()  # 勾选组织架构筛选到的人
		time.sleep(1)
		self.wd.find_element_by_css_selector("#orgfield+div>div>button:nth-child(2)").click()  # 点击保存
		time.sleep(1)
		self.wd.find_element_by_xpath(
			'//*[@id="department_dialog"]/../following-sibling::div//div[3]//div//button').click()  # 点击关闭
		# 上面实现创建一个用户，并将这个用户添加到配置里面，下面要检查一下这个用户是不是被成功选中
		self.wd.refresh()
		time.sleep(2)
		span_text = self.wd.find_element_by_css_selector(
			".operationOverviewRelatedUser.relatedUser>li>span:nth-child(2)").text
		span_text = span_text.split("-")[-1].strip()  # 因为字符串后面会有一个空格
		if span_text == c[-1]:
			print("配置保存成功")
		else:
			raise Exception("配置保存失败")
		# 上面是完成配置，下面登录到配置用户的界面去检查
		self.wd.get(environment + "/user/signout")
		self.user_login(environment, nsername=c[-1], password="11111111", enterprise="pre测试企业")  # 新创建的用户登录
		self.wd.get(environment + companyinfo)
		time.sleep(2)
		span_title = self.wd.find_element_by_css_selector("div.company-container>div>p>span:nth-child(2)").text
		if span_title == "人员概况":
			print("配置的用户{}能正常访问容器的运营概况".format(c[-1]))
		else:
			raise Exception("配置的用户{}不能正常访问容器的运营概况".format(c[-1]))
		# 下面在用一个没有配置的用户，看看是否可以访问运营概况
		session = Web_interface().login_api(environment)
		c = Web_interface().add_user(session, environment)
		print("成功创建用户{}".format(c[-1]))
		self.wd.get(environment + "/user/signout")
		self.user_login(environment, nsername=c[-1], password="11111111", enterprise="pre测试企业")  # 新创建的用户登录
		self.wd.get(environment + companyinfo)
		time.sleep(2)
		error_404 = self.wd.find_element_by_css_selector("#error_404")
		if error_404:
			print("没有被授权的用户{},不能正常访问容器的运营概况".format(c[-1]))
		else:
			raise Exception("没有被授权的用户{},也能正常访问容器的运营概况".format(c[-1]))
		self.wd.get(environment + "/user/signout")
		# 再次回到管理员页面，方便下一个用例执行
		self.user_login(environment, nsername="admin_pretest", password="11111111", enterprise="pre测试企业")  # 新创建的用户登录



if __name__ == '__main__':
	wo = Web_Operation_backstage()
	wo.open_browser()
	wo.user_login("https://www.qycloud.com.cn")
	wo.User_activity_analysis("https://www.qycloud.com.cn")
