*** Settings ***
Variables   cfg.py
Library    pylib.Web_Lib
Library    pylib.Web_interface

Suite Setup         open_browser
Suite Teardown      close_browser


*** Test Cases ***
用户登录 - tc000001
    user login          https://www.qycloud.com.cn     admin_pretest         11111111



流程触发数据 - tc000002
    wf to df            https://www.qycloud.com.cn



流程触发流程 - tc000003
    wf to wf             https://www.qycloud.com.cn



数据触发数据 - tc000004
    df to df            https://www.qycloud.com.cn



数据触发流程 - tc000005
    df to wf            https://www.qycloud.com.cn





资源触发流程 - tc000006
    zy to wf            https://www.qycloud.com.cn





数据触发数据通知 - tc000007
    del all         https://www.qycloud.com.cn          admin_pretest           11111111

    df to remind            https://www.qycloud.com.cn

    del all         https://www.qycloud.com.cn         admin_pretest           11111111



周期触发数据 - tc000008
    cycle_to_df         https://www.qycloud.com.cn


周期触发流程 - tc000009
    cycle_to_wf         https://www.qycloud.com.cn



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