*** Settings ***
Library  Selenium2Library
Library  Collections

*** Keywords ***
get login
     open browser      http://localhost/mgr/login/login.html    Chrome
     SET SELENIUM IMPLICIT WAIT    10

deleteAllLesson
    logintest
    SET SELENIUM IMPLICIT WAIT    2   #登陆之后的操作立马获取元素，使用html获取，可能会报错，因为页面会跳转刷新
    :For   ${one}  IN RANGE  99
       \   sleep  1
       \   ${html}=  Get Webelement  tag=html
       \   ${eles}=  Evaluate   $html.find_elements_by_css_selector("*[ng-click^='delOne']")
       \   Exit For Loop If   $eles==[]
       \   Click Element   @{eles}[0]
       \   Click Element   css=button.btn-primary
    Set Selenium Implicit Wait   10

logintest
    get login
    Input Text          id=username    auto
    Input Text          id=password    qwe123
    click element       tag=button
Addcourse
    [Arguments]      ${courseName}     ${courseDisc}       ${courseId}     #定义变量，Arguments
    click element       css=button[ng-click^="showAddOne"]
    input text          css=input[ng-model="addData.name"]         ${courseName}
    input text          css=textarea[ng-model="addData.desc"]       ${courseDisc}
    input text          css=input[ng-model="addData.display_idx"]    ${courseId}
    click element       css=button[ng-click="addOne()"]

Get course list
    ${eles}=    get webelements   xpath=//div[@class='row col-lg-12 col-md-12 col-sm-12 ng-scope']//td[2]
    ${lession}=   create list

    :for   ${ele}   in   @{eles}
    \    log to console    ${ele.text}
    \    Append To List     ${lession}     ${ele.text}
    [Return]    ${lession}

