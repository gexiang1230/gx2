*** Settings ***
Library  pylib.WebOpAdmin.Login
Suite Setup       OpenBrower
Suite Teardown    TearBrower

*** Keywords ***
suite setup action
     login  ly   ly123!@#          #初始化条件是必须处于登录成功的状态
