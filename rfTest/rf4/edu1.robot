*** Settings ***
Library  Selenium2Library
Library  Collections
Library  eduini
*** Test Cases ***
用例1：验证当系统中没有课程的时候，是否能成功添加一个课程
    [Setup]     deleteAllLesson
    Open Browser        http://localhost/mgr/login/login.html    Chrome
    SET SELENIUM IMPLICIT WAIT    10
    Input Text          id=username    auto
    Input Text          id=password    qwe123
    click element       tag=button
    click element       css=button[ng-click^="showAddOne"]
    input text          css=input[ng-model="addData.name"]         初中数学
    input text          css=textarea[ng-model="addData.desc"]       初中数学基础信息
    input text          css=input[ng-model="addData.display_idx"]     1
    click element       css=button[ng-click="addOne()"]
    ${eles}=    get webelements   xpath=//div[@class='row col-lg-12 col-md-12 col-sm-12 ng-scope']//td[2]
    ${lession}=   create list
    :for   ${ele}   in   @{eles}
    \    log to console    ${ele.text}
    \    Append To List     ${lession}     ${ele.text}
    ${expected}=   create list    初中数学
    Lists Should Be Equal    ${lession}     ${expected}


    Close Browser

    [Teardown]   deleteAllLesson