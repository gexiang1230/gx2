*** Settings ***
Library  pylib.SearchInfo               #library 导入的是测试库
Resource   rflib/searchInfo.robot       #resource  用于使用导入资源库
Suite Setup    login   ly  ly123!@#
Suite Teardown  TearBrower

*** Test Cases ***
用例1：检查姓名文本
     RUN KEYWORD      searchText      [for=custName]


用例2：检查电话文本

    RUN KEYWORD      searchText      [for=custPhone]

用例3：检查设备文本

    RUN KEYWORD      searchText
    ...             \#formSearch${space}.form-group:nth-of-type(1)${space}label:nth-of-type(3)
用例4:检查型号文本
    RUN KEYWORD      searchText
    ...             \#formSearch${space}.form-group:nth-of-type(1)${space}label:nth-last-of-type(1)
用例5：检查设备厂商文本
    RUN KEYWORD      searchText
    ...              \ #formSearch${space}.form-group:nth-of-type(5)${space}label:nth-of-type(3)
