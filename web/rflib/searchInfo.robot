

*** Keywords ***
searchText
     [Arguments]    ${element}
     sleep  3
     ${ele}=   checkTextBox    ${element}
     ${real}=  create list      姓名   电话  设备  型号  测量类型  等级  慢病阶段
     ...                        设备号  未测天数 联系方式  所属客服  订单号
     ...                       客户编号  未回访  到期时间  否有微信  未达PPC
     ...                       用户组别  签收时间  是否检查  设备厂商
     should contain    ${real}    ${ele}
