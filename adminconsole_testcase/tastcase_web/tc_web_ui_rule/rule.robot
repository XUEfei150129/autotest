*** Settings ***
Variables   cfg.py
Library    pylib.Web_rul
Library    pylib.Web_interface


Suite Setup            user_login_init_rul              https://www.qycloud.com.cn


Suite Teardown         Close_browser

*** Test Cases ***
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


