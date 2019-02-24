*** Settings ***
Variables   cfg.py
Library    pylib.Web_Operation_backstage
Library    pylib.Web_interface


Suite Setup            user_login_init_backstage              https://www.qycloud.com.cn


Suite Teardown         close_browser


*** Test Cases ***

运营概况新增活跃用户 - tc000010
    get_webactivepeople     https://www.qycloud.com.cn          4



系统主题配色（新用户） - tc000011
    Theme_Colors          https://www.qycloud.com.cn


测试样式表 - tc000012
    style_sheet          https://www.qycloud.com.cn


测试logo上传 - tc000013
    logo_upload          https://www.qycloud.com.cn



角色权限组织架构 - tc000014
    role authorization         https://www.qycloud.com.cn


角色权限运营概况 - tc000015
    User_activity_analysis         https://www.qycloud.com.cn

