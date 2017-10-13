*** Settings ***
Library  Selenium2Library
Library  Collections
Resource  rflib/rc.robot
*** Test Cases ***
用例1：添加课程1
    [Setup]     deleteAllLesson
    logintest
    Addcourse   初中数学    初中数学描述      1
    ${lession}=     Get course list
    run keyword if     $lession==[u'初中数学']
    ...  log to console  1
    [Teardown]   deleteAllLesson
用例1：添加课程2
    [Setup]     deleteAllLesson
    logintest
    Addcourse   初中化学    初中化学描述      2
    ${lession}=     Get course list
    SHOULD BE TRUE   $lession==[u'初中化学']
    [Teardown]   deleteAllLesson