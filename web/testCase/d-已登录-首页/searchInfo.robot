*** Settings ***
Library  pylib.SearchInfo.SearchInfo

*** Test Cases ***
用例1：测试获取页面文本
       suite setup action
       ${ele}=    checkInfo
       log to console  $ele