pre = "https://pre.qycloud.com.cn"
www = "https://www.qycloud.com.cn"
home_login = "/home/login"

appcenter = "/appcenter"
rulu_page = "/rulesengine#!/category/12"


# wf_to_df
wf_to_df_01 = "/app/!/workflow/LiuChengChuFaShuJu"
wf_to_df_02 = "/app/!/information/LiuChengChuFaShuJu02"


# wf_to_wf
wf_to_wf_01 = "/app/!/workflow/LiuChengChuFaLiuChen"
wf_to_wf_02 = "/app/!/workflow/uChengChuFaLiuChen80"


# df_to_df
df_to_df_01 = "/app/!/information/ShuJuChuFaShuJu01"
df_to_df_02 = "/app/!/information/ShuJuChuFaShuJu02"

# df_to_wf
df_to_wf_01 = "/app/!/information/ShuJuChuFaLiuCheng01"
df_to_wf_02 = "/app/!/workflow/ShuJuChuFaLiuCheng02"


#df_to_remind
df_to_remind = "/app/!/information/ShuJuChuFaShuJuTongZ"

#zy_to_wf
zy_to_wf_01 = "/app/!/information/ZiYuanChuFaLiuCheng0qy"
zy_to_wf_02 = "/app/!/workflow/ZiYuanChuFaLiuCheng0"

#cycle_to_df
cycle_to_df = "/app/!/information/ZhouQiChuFaShuJu"
rulu_page_cycle_to_df1 = "/rulesengine/create/startrules/?edit=112"
rulu_page_cycle_to_df2 = "/rulesengine/create/end/?edit=112"



#cycle_to_wf
cycle_to_wf = "/app/!/workflow/ZhouQiChuFaLiuCheng"
rulu_page_cycle_to_wf1 = "/rulesengine/create/startrules/?edit=176"
rulu_page_cycle_to_wf2 = "/rulesengine/create/end/?edit=176"


#下面是企业主页的
companyinfo = "/companyinfo"
themeColor = "/enterprise/themeColor"

stylesheet = "/enterprise/stylesheet"


logo = "/enterprise/logo"

#下面是角色权限的
role = "/role/authorization"



'''
div:nth-child(2)>div:nth-child(1)>div:nth-child(2)>div>div>div>input				#第一排第一个		字符串
div:nth-child(2)>div:nth-child(1)>div:nth-child(4)>div>div>div>textarea				#第一排第二个		用户信息
div:nth-child(2)>div:nth-child(2)>div:nth-child(2)>div>div>div>input				#第二排第一个		数字
div:nth-child(2)>div:nth-child(2)>div:nth-child(4)>div>div							#第二排第二个		经纬度
div:nth-child(2)>div:nth-child(3)>div:nth-child(2)>div>div>div>input				#第三排第一个		编号
div:nth-child(2)>div:nth-child(3)>div:nth-child(4)>div>div>div>textarea				#第三排第二个		文本
div:nth-child(2)>div:nth-child(4)>div:nth-child(2)>div>div>span>div>input			#第四排第一个		多选
div:nth-child(2)>div:nth-child(4)>div:nth-child(4)>div>div>div>div>input			#第四排第二个		单选
div:nth-child(2)>div:nth-child(5)>div:nth-child(2)>div>div>div>div>input			#第五排第一个		多选
div:nth-child(2)>div:nth-child(5)>div:nth-child(4)>div>div>div>div>button			#第五排第二个		附件
div:nth-child(2)>div:nth-child(6)>div:nth-child(2)>div>div>div>input				#第六排第一个		日期时间
div:nth-child(2)>div:nth-child(6)>div:nth-child(4)>div>div>div>textarea				#第六排第二个		组织架构
div:nth-child(2)>div:nth-child(7)>div:nth-child(2)>div>div>div>div>input			#第7排第一个		数据源
'''


# def find_Element(row, number, type):
# 	if type == "字符串" or type =="数字" or type =="日期时间" or type =="编号":
# 		ele_front = "div:nth-child(2)>div:nth-child(%s)>div:nth-child(%s)>div>"%(row,number*2)
# 		ele_back = "div>div>input"
# 		ele = ele_front + ele_back
#
# 	elif type == "用户信息" or type =="文本":
# 		ele_front = "div:nth-child(2)>div:nth-child(%s)>div:nth-child(%s)>div>"%(row,number*2)
# 		ele_back = "div>div>textarea"
# 		ele = ele_front + ele_back
#
# 	elif type == "经纬度":
# 		ele_front = "div:nth-child(2)>div:nth-child(%s)>div:nth-child(%s)>div>"%(row,number*2)
# 		ele_back = "div"
# 		ele = ele_front + ele_back
#
# 	elif type == "地区":
# 		ele_front = "div:nth-child(2)>div:nth-child(%s)>div:nth-child(%s)>div>" %(row,number*2)
# 		ele_back = "div>span>div>input"
# 		ele = ele_front + ele_back
#
# 	elif type == "单选" or type =="多选" or type =="数据源":
# 		ele_front = "div:nth-child(2)>div:nth-child(%s)>div:nth-child(%s)>div>"%(row,number*2)
# 		ele_back = "div>div>div>input"
# 		ele = ele_front + ele_back
#
# 	elif type == "附件":
# 		ele_front = "div:nth-child(2)>div:nth-child(%s)>div:nth-child(%s)>div>"%(row,number*2)
# 		ele_back = "div>div>div>button"
# 		ele = ele_front + ele_back
#
# 	else:
# 		raise Exception("cannot find any Element!!")
#
# 	return print(str(ele))
#
#
# find_Element(1,1,"单选")











"""
全局的变量
"""
