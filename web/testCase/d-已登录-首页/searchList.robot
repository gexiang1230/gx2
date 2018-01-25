*** Settings ***
Library      pylib.SearchInfo
Library      pylib.dataBase.dataPerform
Suite Setup    login   ly   ly123!@#
Suite Teardown  TearBrower

*** Test Cases ***
#用例1：姓名
#       ${info}=   create dictionary    inputs=李艳
#       checkSelectBox      姓名      &{info}
#       ${comfirm}=          search
#       should contain     ${comfirm}      李艳
#
#
#用例2：设备号
#       ${info}=   create dictionary    inputs=626010110266890
#       checkSelectBox      姓名      &{info}
#       ${comfirm}=          search
#       should contain     ${comfirm}     626010110266890
#
#
#
#用例3：客户编号
#        ${info}=   create dictionary    inputs=K16112500091
#       checkSelectBox      姓名      &{info}
#       ${comfirm}=          search
#       should contain     ${comfirm}      K16112500091

用例4：验证姓名的查询个数
       ${info}=   create dictionary    inputs=李艳
       checkSelectBox      姓名      &{info}
       ${comfirm}=         loading

       ${countResult} =     querys
            ...   SELECT${space}COUNT(DISTINCT cust_name)${space}FROM${space}db_main_list${space}WHERE${space}cust_name${space}LIKE${space}'李艳%'
       should contain    ${comfirm}     ${countResult}



