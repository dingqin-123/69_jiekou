# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 0001 下午 4:10
# @Author  : dingqin


from practice01.R_W_excel import read_data
from practice01.http_request import http_request
from practice01.R_W_excel import write_data
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


Token=None  #全局变量，初始值设置为None

def run(file_name,sheet_name,col_actual,col_result):       #行是跟着id走的，不用变，需要变化的就是列
    global Token   #在这里声明  函数外的Token 和函数内的Token是同一个值
    all_data=read_data(file_name, sheet_name)
    print('获取到的所有测试数据是：',all_data)
    for test_data in all_data:
        # if test_data[0]==1:     #1、
        # if test_data[1]=='登陆':   #2、
        ip = 'http://120.78.128.25:8766'
        response = http_request(ip + test_data[4], eval(test_data[5]), token=Token, method=test_data[3])
        if 'login' in test_data[4]:
            # 它就是一个登陆的用例
            Token='Bearer '+response['data']['token_info']['token']
        print('最后的结果',response)

        #写入结果
        write_data(file_name,sheet_name,test_data[0]+1,col_actual,str(response))
        actual={'code': response['code'],'msg': response['msg']}
        if eval(test_data[6])==actual:
            print('用例执行通过！')
            write_data(file_name,sheet_name,test_data[0]+1,col_result,'PASS')
        else:
            print('用例执行通过！')
            write_data(file_name,sheet_name, test_data[0]+1,col_result,'FAIL')

run('test_case.xlsx','recharge',8,9)


