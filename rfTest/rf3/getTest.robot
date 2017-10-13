*** Settings ***
Library  Selenium2Library    #库的名字一定要对
Library  Dialogs

*** Test Cases ***
用例1
    ${var1}  convert to integer   100
    ${var2}  set variable    5
    should be true  $var1*int($var2)==500

用例2    # 循环

    :for  ${one}            in range     9999
     \   ${weight}=        get value from user   请输入你的体重    60
     \    run keyword if    int($weight)>60   log to console  太重了
     \    run keyword if    $weight=='quit'   exit

用例3   #初始化清除





