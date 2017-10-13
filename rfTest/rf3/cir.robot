*** Settings ***
Library     Selenium2Library
Library     course_mgr
Library     Collections


*** Test Cases ***
用例1：返回所有课程列表
    ${courselist}=     listCourse
    :for  ${courses}  in   @{courselist}
    \   log to console    ${courses}
    ${comparCourses}=  create list    java     selenium   初中化学
   lists should be equal  ${courselist}     ${comparCourses}
用例2：获得华为官网的热销单品的名字
   open browser    https://www.vmall.com/    chrome
   set selenium implicit wait   4
   ${eles}=  GET WEBELEMENTS    xpath=//div[@class="home-recommend-goods home-hot-goods"]//h3
   :for   ${ele}  in   @{eles}
   \   log to console  ${ele.text}
   close browser