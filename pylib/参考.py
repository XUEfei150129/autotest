#
# from selenium import webdriver
# import time
# from selenium.webdriver.common.action_chains import ActionChains    #悬停的操作
# def create_rulu():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     driver.get("https://www.qycloud.com.cn/home/login")
#     driver.find_element_by_id("userid").send_keys("admin_pretest")
#     driver.find_element_by_id("password").send_keys("11111111")
#     driver.maximize_window()
#     loginele = driver.find_element_by_class_name("loginButton")
#     time.sleep(3)
#     loginele.click()               #登录企业
#     time.sleep(3)
#     # 判断进入的企业是不是DB测试企业
#     driver.get("https://www.qycloud.com.cn/appcenter")
#     # print(driver.title)
#     b = driver.title
#     if "pre测试企业" in b:
#         print("1.成功登录到pre测试企业")
#     else:
#         entele = driver.find_element_by_css_selector("i.icon-xiala- ")      #选中头像右侧的下拉按钮
#         time.sleep(2)
#         entele.click()      #点击头像右侧的下拉按钮
#         enttitle = driver.find_element_by_css_selector("li .ent-switcher")     #选中企业切换按钮
#         ActionChains(driver).move_to_element(enttitle).perform()             # 悬停至企业切换按钮
#         time.sleep(1)
#         driver.find_element_by_css_selector('li .ent-switcher ul li[title="pre测试企业"]').click()    #选中要切换的企业，并进入
#         time.sleep(4)
#         b = driver.title
#         if "pre测试企业" in b:
#             print("1.成功切换到Pre测试企业")
#         else:
#             print("1.切换企业失败")
#
#     driver.get("https://www.qycloud.com.cn/rulesengine")       #进入规则引擎页面
#     rulele = driver.find_element_by_id("BtnAddRules")
#     typeele = rulele.get_attribute("type")
#     if typeele =="button":
#         print("2.正确跳转至规则引擎界面")
#     else:
#         print("2.规则引擎界面跳转失败")
#     #创建规则
#     driver.find_element_by_id("BtnAddRules").click()   #创建规则
#     driver.find_element_by_css_selector("input.input_n").send_keys("这是selenium创建的规则----数据触发数据")
#     driver.find_element_by_css_selector(".text_n").send_keys("数据触发数据")
#     ele1 = driver.find_element_by_css_selector("#step_next")         #下一页
#     print("  第一步：规则名及说明创建完成")
#     time.sleep(2)
#     ele1.click()
#     ele2 = driver.find_element_by_css_selector('img[src$="/app/info/ico.png"]')       #选择数据
#     time.sleep(2)
#     ele2.click()
#     driver.find_element_by_id("step_next").click()   #下一页
#     print("  第二步：成功选择触发器类型")
#     driver.find_element_by_css_selector("#select2-chosen-4").click()     #点击具体的应用的输入框
#     driver.find_element_by_css_selector("#s2id_autogen4_search").send_keys("df111111")
#     driver.find_element_by_css_selector("ul#select2-results-4").click()           #选中具体的应用
#     time.sleep(2)
#     driver.find_element_by_css_selector("#rule_form table.settingTable>tbody>tr:nth-child(2)>td:nth-child(2) span").click()    #点击表单的输入框
#     # driver.find_element_by_css_selector("#select2-drop>div>input").send_keys("df11111111")
#     driver.find_element_by_css_selector("#select2-drop>div+ul>li:nth-child(2)>div").click()     #点击具体的表单
#     driver.find_element_by_css_selector("#step_next").click()   #点击下一步
#     print("  第三步：成功选择触发器 df111111")
#     driver.find_element_by_css_selector('img[src$="/rulesengine/app/info/ico.png"]').click()    #选中数据
#     time.sleep(1)
#     driver.find_element_by_css_selector("#step_next").click()         #点击下一步
#     print("  第四步：成功选择接收器类型")
#     driver.find_element_by_css_selector("#select2-chosen-1").click()      #点击选择接收器的应用
#     driver.find_element_by_css_selector("#s2id_autogen1_search").send_keys("df222222")     #选择接收器的应用
#     driver.find_element_by_css_selector("#select2-results-1").click()      #选中接收器的应用
#     driver.find_element_by_css_selector("#select2-chosen-2").click()
#     driver.find_element_by_css_selector("#s2id_autogen2_search").send_keys("df22222222")
#     driver.find_element_by_css_selector("#select2-results-2").click()    #选中接收器的表单
#     driver.find_element_by_css_selector("a.edit").click()      #点击编辑按钮，进行赋值匹配
#     driver.find_element_by_css_selector("input.addCondition").click()      #点击添加字段
#
#     driver.find_element_by_css_selector("td.prevFieldSpace>div>a b").click()      #id是随机变化的，无法点位。用子节点兄弟节点定位元素
#     driver.find_element_by_css_selector("#select2-drop>div>input").send_keys("字符串")    #赋值匹配
#     driver.find_element_by_css_selector("#select2-drop>ul>li>ul>li>div").click()
#
#     driver.find_element_by_css_selector('.valueSpace>div>a>span[class*="select2-chosen"]').click()
#     driver.find_element_by_css_selector("#select2-drop>div>input").send_keys("字符串")
#     driver.find_element_by_css_selector("#select2-drop ul>li ~li>ul>li>div>span").click()
#
#     driver.find_element_by_css_selector("div.ui-dialog-buttonpane>div>button~button").click()    #点击确定
#     driver.find_element_by_id("step_next").click()     #点击确定
#     ele3 = driver.find_elements_by_css_selector("#rule_form>table>tbody>tr")
#     # for one in ele3:
#     if ele3[0].text == "规则名称: 这是selenium创建的规则----数据触发数据" and \
#         ele3[1].text =="描述: 数据触发数据" and \
#         ele3[2].text == "触发条件: df11111111：":
#         print("  第五步：规则确认正确")
#     else:
#         print("  第五步：规则确认异常")
#
#     driver.find_element_by_id("step_next").click()     #点击创建
#     print("  第六步：规则创建成功")
#
#     driver.find_element_by_css_selector("#tblEnginerules_wrapper>table>tbody>tr:nth-child(1)>td:nth-child(6)>button:nth-last-child(3)").click()
#     driver.switch_to.alert.accept() #删除规则
#
#
# # create_rulu()
#
# # str1 = "12-26 16:58:43"
# #
# # print(str1)
# # str1 = str1.split(" ")[1][0:5]
# # print(str1)
# #
# #
# # from datetime import datetime
# # now_time = str(datetime.now())
# # now_time = now_time.split(" ")[1][0:5]
# # print(now_time)


# from datetime import datetime

# now_time = str(datetime.now())
# now_time_h = now_time.split(" ")[1][0:2]
# now_time_m = str(int (now_time.split(" ")[1][3:5])+2)
# time = now_time_h + ":"  + now_time_m
# import time
# before = time.time()
# print(before)
# time.sleep(1)
# after = time.time()
# print(after)
# print(f"调用func1，花费时间{after-before}s")


# 1.成功登录到pre测试企业
# 12-28 22:53:51
# 2.触发时间和接收器的数据正确

# import time, datetime
# 字符类型的时间
# tss1 = '2013-10-10 23:40:00'


# 转为时间数组
# timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
# print (timeArray)


# timeArray可以调用tm_year等
# print (timeArray.tm_year)   # 2013


# 转为时间戳
# timeArray = time.strptime("2018-12-28 22:53:52", "%Y-%m-%d %H:%M:%S")
# timeStamp = int(time.mktime(timeArray))
# print (timeStamp)  # 1381419600


# if rulu_time == time_in:
# 	print("触发时间正确")
# 	if yellow:
# 		print("数据正常标黄")
# 	else:
# 		raise Exception("触发时间正确，但是数据没有标黄")
# else:
# 	if yellow:
# 		print("数据正常标黄，但触发时间错误")
# 	else:
# 		raise Exception("触发时间异常，数据也没有标黄")
# ran_str = "111"
# res_text = "111"
# rulu_time = "333"
# now_time = "333"
# if ran_str == res_text:
# 	if rulu_time == now_time:
# 		print("接收器的数据和触发时间都正确")
# 	else:
# 		raise Exception("接收器的数据正确但是触发时间异常：规则的时间是：%s，系统的时间是：%s"%(rulu_time,now_time))
# else:
# 	if rulu_time == now_time:
# 		raise Exception("接收器的数据异常，触发时间正确：触发器的数据是：%s，接收器的数据是：%s"%(ran_str,res_text))
# 	else:
# 		raise Exception("触发时间和接收器的数据都不正确：规则的时间是：%s，系统的时间是：%s,"
# 		                "触发器的数据是：%s，接收器的数据是：%s"%(rulu_time,now_time,ran_str,res_text))


# from datetime import datetime
# now_time = str(datetime.now())
# now_time_h = now_time.split(" ")[1][0:2]
# now_time_m = str(int(now_time.split(" ")[1][3:5]) + 1)
# time_in = '{}:{}'.format(now_time_h, now_time_m)
# now_time_y = now_time.split(" ")[0]
# now_time = str(datetime.now())
# time_in = '{} {}:{}'.format(now_time_y,now_time_h, now_time_m)
# print(time_in[-5:])


# time_in = "2018-12-31 16:34"
# b = "16:34"
# print(a[-5:])

#
# a = "21:21:06"
# print(a[0:5])


# now_time = str(datetime.now())
# now_time_h = now_time.split(" ")[1][0:2]
# now_time_m = str(int(now_time.split(" ")[1][3:5]) + 1)
# now_time_y = now_time.split(" ")[0]
# time_in = '{} {}:{}'.format(now_time_y,now_time_h, now_time_m)
# print(time_in)

#
# a = "2018-12-31 22:15:52"
# print(a.split(" ")[1][0:5])

from datetime import datetime
import time

# now_time = str(datetime.now())
# now_time_year = now_time[0:4]           #当前时间的年份
# rulu_time_get = "01-02 20:30:07"        #获取到的规则的时间
# rulu_time = '{}-{}'.format(now_time_year,rulu_time_get)         #拼接成完整的时间如：2019-01-02 20:30:07
# # print(rulu_time)
# timeArray = time.strptime(rulu_time, "%Y-%m-%d %H:%M:%S")
# timeStamp = int(time.mktime(timeArray))    # 在规则列表页获取到的时间转为时间戳
# if timeStamp in range (int (time.time()-60),int (time.time()+60)):
# 	print(1)
# a = time.time()
# print(a)
# print(222**222)
# print(a)

# if 105 in range (100,300):
# 	print(1)
# print(timeStamp<time.time())


# # 字符类型的时间
# tss1 = '2013-10-10 23:40:00'
# # 转为时间数组
# timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
# print (timeArray )
# # timeArray可以调用tm_year等
# # print timeArray.tm_year   # 2013
# # 转为时间戳
# timeStamp = int(time.mktime(timeArray))
# print (timeStamp)  # 1381419


# tss1 = '2019-01-02 20:30:07'
# timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
# timeStamp = int(time.mktime(timeArray))
# print(timeStamp)


# timeStamp = 1381419600
# timeArray = time.localtime(timeStamp)
# otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
# print otherStyleTime   # 2013--10--10 23:40:00

# a = time.time()     #获取当前时间的时间戳
# b = int(a)
# # print(type(int (a)))
# # print(int (a))
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a)))


# rulu_time = rulu_time.split(" ")[1][0:5]
# now_time = str(datetime.now())
# now_time = now_time.split(" ")[1][0:5]
# now_time = str(datetime.now())
# now_time_year = now_time[0:4]  # 当前时间的年份
# # rulu_time = '{}-{}'.format(now_time_year, rulu_time_get)  # 拼接成完整的时间如：2019-01-02 20:30:07
# timeArray = time.strptime(rulu_time, "%Y-%m-%d %H:%M:%S")
# timeStamp = int(time.mktime(timeArray))  # 在规则列表页获取到的时间转为时间戳
# a =int (time.time())    #获取当前时间的时间戳,取整数部分


# now_time = str(datetime.now())
# a = int (time.time())
# now_time_in = now_time[0:16]
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a))
# # print(now_time)
# print(now_time_in)


# a = time.time()    #获取当前时间的时间戳,取整数部分
# time_in = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a+60)))     #将这样的时间取到分钟2019-01-02 22:43:30
# time_in_hm = time_in[11:16]
# print(time_in_hm)
#
# a = "01-02 22:52:07"
# print(a[6:11])

# now_time = str(datetime.now())
# now_time_h = now_time.split(" ")[1][0:2]
# now_time_m = str(int(now_time.split(" ")[1][3:5]) + 1)
# time_in = '{}:{}'.format(now_time_h, now_time_m)
# print(time_in)

# a = time.time()  # 获取当前时间的时间戳
# time_in = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a + 60)))  # 将这样的时间取到分钟2019-01-02 22:43:30
# time_in_hmrhm = time_in[:-3]
# print(time_in_hmrhm)
# time_in_hmrhm = time_in_hmrhm[-5:]
# print(time_in_hmrhm)
#
#
# rulu_time = "01-02 22:54:08"
# rulu_time = rulu_time.split(" ")[1][0:5]
# print(rulu_time)


#
# import random
# from selenium import webdriver
# import time
# from selenium.webdriver.common.action_chains import ActionChains    #悬停的操作
#
#
#
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get("https://pre.qycloud.com.cn/home/login")
# driver.find_element_by_id("userid").send_keys("admin_pretest")
# driver.find_element_by_id("password").send_keys("11111111")
# driver.maximize_window()
# loginele = driver.find_element_by_class_name("loginButton")
# time.sleep(3)
# loginele.click()               #登录企业
# time.sleep(3)
#
# driver.get("https://pre.qycloud.com.cn/enterprise/themeColor")       #进入规则引擎页面
#
# skin_list = driver.find_element_by_css_selector("ul.skin-list")
# item = skin_list.find_elements_by_css_selector("li")
#
#
# i = random.randint(0,8)
# c = item[i]
# print(c)
# i_name = c.find_element_by_css_selector("li p").text
# c.find_element_by_css_selector("li div").click()
# print(i_name)
# driver.find_element_by_css_selector("button.el-button.el-button--primary.el-button--medium").click()
# driver.find_element_by_css_selector("div.el-message-box__btns>button:nth-child(1)").click()
# check = c.find_element_by_css_selector('li div i[class*="icon-check"]')
# if check:
# 	print("成功选中主题为【{}】".format(i_name))
#
#
#


#
# import random
# i = random.randint(1,9)
# i = i-1
# print(i)
# a = [0,1,2,3,4,5,6,7,8]
# b = a.index(i)
# print(b)

# from datetime import datetime
# img_name = (datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "_logo.png"
# print(img_name)

#
# img_name = (datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "_logo.png"
# img_name = img_name.replace(":","-")
# print(img_name)
# a = (r"D:\auto_test\{}".format(img_name))
#
# print(a)

# import os
# path = r'D:\auto_test'
# filenames = os.listdir(path)
# print(type(filenames))
# for filename in filenames:
#     print(filename)

# a = "总经理-ddddd-R9dgkTcSru"
# a = a.split("-")
# print(a)

# a = "   sddsd   "
# b= a.strip().split("ddd")[0]
# print(len(b))
# print(b)
# import unittest
# class aaa(unittest.TestCase):
# 	def test_111(self):
# 		a = 1+1
# 		self.assertEqual(21,a,msg="验证1+1是不是等于2")
#
#
# a=aaa()
# a.test_111()


"""
使用Github

目的
    借助github托管项目代码
基本概念
    仓库(Repository)  ：仓库的意思，即是你的项目，你想在GitHub上开元一个项目，那就必须要新建一个Repository，如果你开源的项目多恶劣，你就拥有了多个Repository
                      ：仓库用来存放项目代码的，每个项目对应一个仓库。多个开源项目则有多个仓库

    收藏（star）：仓库主页star按钮，意思是收藏项目的人数，在GitHub上如果你有一个项目获得100个star都是很不容易了！
                ：收藏项目，方便下次查看
                
    复制克隆项目(Fork):该fork的项目是独立存在的
    
    
    
    
注册github账号
    官方网址：Github.com
    (第二步，默认免费；第三步，跳过。新注册的用户必须邮箱验证后才可以创建git仓库)
    第一次创建项目的时候要验证邮箱
    
    
创建仓库
    说明
    一个Git库（仓库）对应一个开源项目。
    通过git管理git库      
    
    
    
    
    
    
    
    
仓库管理
    新建文件
    编辑文件
    删除文件
    
    搜索仓库文件（快捷键t）
        
    下载/检出项目
    

    GitHub Issues
    作用：发现代码bug，但是目前没有成型代码，需要讨论时用；或者使用开源项目出现问题时使用
    
    情景：张三发现李四开源git库，则发提交了一个Issue，李四隔天登录在github主页看到通知冰河张三交流，最后关闭Issue
    
    
    基本概念实战
        Github主页
        仓库主页（不陌生了）
        个人主页
            仓库(Repository)：存放项目代码
            收藏：
                打开对应的项目主页，点击右上角star按钮，即可收藏
                情景：张三无意访问到李四的开源项目感觉不错并进行收藏
                
            关注（Watch）
                情景：张三关注了李四的项目，李四添加项目文件，张三的github主页会有怎样的进展
        
            复制克隆项目（Fork）
                情景：张三fork了李四的项目，相当于张三复制了李四的项目，所以自己也单独有了一个一样名称的仓库（注：该仓库会声明来自于李四，但是独立存在）
    
            
            发起请求（Pull Request）
                情景：张三修改了fork的项目中的文件，希望更新原来的仓库，这时候他要新建一个pull request
    
    开源项目贡献流程
        1.新建Issue
            提交使用问题或者建议，或者想法
        2.Pull Request
            步骤：1.fork项目
                2.修改自己仓库的项目代码
                3.新建pull request
                4.等待作者操作（合并审核）
        
        
        
    
Git 安装和使用
目的
    通过git管理github托管项目代码
下载安装
    1) Git 官网下载
        https://www.git-scm.com/download/win
    2）双击安装
    3）回到桌面右击看是否多出两个git图标


Git工作区域
    工作区（Working Directory）：添加，编辑，修改文件等动作
    暂存区：暂存已经修改的文件最后统一提交到git仓库中
    Git 仓库（Git Repository）：最终确定的文件保存到仓库，成为一个新的版本，并且对他人可见




Git初始化及仓库创建和操作
基本信息设置
    1.设置用户名
    git config --global user.name "XUEfei150129"
    2.设置用户名邮箱
    git config --global user.email "1010029946@qq.com"
    
    该设置在github仓库主页显示谁提交了该文件


初始化一个新的Git仓库
    1.创建文件夹
        mkdir test (手动创建)
    2.在文件内初始化git（创建git仓库）
        cd test (进到test文件夹里面，目的是将test创建成一个仓库)
        git init 
    3.向仓库添加文件
        三步
    4.修改仓库文件
        三步
    5.删除仓库文件
        三步
        
Git管理远程仓库
    作用：备份，实现代码共享集中化管理
    

    Git 克隆操作
    目的
        将远程仓库（github对应的项目）复制到本地
    代码
        git clone 仓库地址
        仓库地址的由来（见图）
    
    






"""
