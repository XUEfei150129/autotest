# from appium import webdriver   #webdriver是基于selenium扩展的一个对象
# import time,traceback
#
# class Android_Lib():
#
# 	def __init__(self):
# 		pass
#
# 	# 方便导入库的时候，传入参数
#
# 	def device_attachment(self,platformVersion,appPackage,appActivity):
# 		desired_caps = {}   #存储一些配置信息，通过字典键值对来存。吧配置信息传递给appium server
# 		desired_caps['platformName'] = 'Android'      #指定自动化的设备
# 		desired_caps['platformVersion'] = platformVersion    #   7.0
# 		desired_caps['deviceName'] = 'test'    #对安卓没啥用，但是不能不写
# 		# desired_caps['app'] = r'd:\app-release.apk'       #app安装包的路径，如果手机没装的话，会帮你装上。如果装好，可以注释
# 		desired_caps['appPackage'] =appPackage     #com.jungan.www.hqs
# 		desired_caps['appActivity'] = appActivity   #com.jungan.www.module_main.ui.SplanActivity
# 		desired_caps['unicodeKeyboard']  = True    #输入中文的话，这个就要打开。给appium自动化用的。输入非ask码用的
# 		desired_caps['resetKeyboard']  = True   #配合上面一起用的，据说可以还原之前的输入法
# 		desired_caps['noReset'] = True          #非常重要。如果不设置的话。每次运行都会清空里面的数据。
# 		desired_caps['newCommandTimeout'] = 6000     #主要是与服务端appiumserver连接的时间，防止断开。6000s
# 		#启动Remote RPC
# 		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)       #
# 		self.driver.implicitly_wait(10)
#
#
#
#
# 	def Andirod_login(self,username,password):
# 		time.sleep(2)
# 		self.driver.find_element_by_xpath(
# 			'//*[@resource-id="com.jungan.www.hqs:id/class_gv"]//android.widget.RelativeLayout[1]/	android.widget.TextView').click()  # 选择初三
# 		self.driver.find_element_by_xpath('//*[@resource-id="com.jungan.www.hqs:id/tabbar"]//android.widget.RelativeLayout[4]').click()
#
# 		self.driver.find_element_by_id("com.jungan.www.hqs:id/btn_login").click()            #点击登录
#
# 		self.driver.find_element_by_id("com.jungan.www.hqs:id/et_phonenum").send_keys(username)
#
# 		self.driver.find_element_by_id("com.jungan.www.hqs:id/et_password").send_keys(password)
#
# 		self.driver.find_element_by_id("com.jungan.www.hqs:id/btn_commit").click()
# 		ele = self.driver.find_element_by_id("com.jungan.www.hqs:id/userName_tv")
# 		ele_name = ele.text
# 		if ele_name == username:
# 			print("登录成功")
# 		else:
# 			print("登录失败")
#
# 	def search_course_UI(self,coursename):
# 		self.driver.find_element_by_xpath('//*[@resource-id="com.jungan.www.hqs:id/tabbar"]//android.widget.RelativeLayout[1]').click()          #f返回到首页
# 		# self.driver.find_element_by_xpath('//*[@resource-id="com.jungan.www.hqs:id/class_gv"]//android.widget.RelativeLayout[1]/	android.widget.TextView').click()               #选择初三
# 		self.driver.find_element_by_id("com.jungan.www.hqs:id/home_seacher_img").click()     #点击搜索
#
# 		self.driver.find_element_by_id("com.jungan.www.hqs:id/ss_et").send_keys(coursename)
#
# 		self.driver.find_element_by_id("com.jungan.www.hqs:id/seacher_tv").click()
#
#
# 		ele = self.driver.find_element_by_id("com.jungan.www.hqs:id/title_tv")
# 		ele = ele.text
# 		# print(ele)
#
#
# 		if coursename in ele :
# 			print("搜索功能正常")
# 		else:
# 			print("搜索功能异常")
#
#
#
# # if  __name__ == '__main__':
# # 	wo = Android_Lib()
# # 	wo.device_attachment(7.0,"com.jungan.www.hqs","com.jungan.www.module_main.ui.SplanActivity")
# # 	wo.Andirod_login("15050563690","11111111")
# # 	wo.search_course_UI("语文")