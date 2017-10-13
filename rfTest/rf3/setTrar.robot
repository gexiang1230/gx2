*** Settings ***
Library   Selenium2Library

Suite Setup             log to console  \n'套件初始化'     #整体前后执行
Suite Teardown    log to console    \n '套件清除'
Test Setup       log to console     \n'测试用例初始化'      #没有初始化和清除的测试用例会执行
Test Teardown     log to console    \n '测试用例清除'


*** Test Cases ***
用例1
     [Documentation]   \n测试初始化和清除
     [Setup]          log to console    \n'第一行'
     log to console   \n第二行：测试用例1主体部分
     [Teardown]   log to console     \n'第三行'
用例2
     log to console   \n 测试用例2主体部分
用例3
     log to console    \n测试用例3主体部分