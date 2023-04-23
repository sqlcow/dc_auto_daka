# -*- coding: utf-8 -*-

import requests
import json
import sys
import codecs
import datetime


# 获取当前时间
now = datetime.datetime.now()
#更改编码：适用于python2.7版本
reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.open('/www/wwwroot/daka.sqlcow.com/log.txt', 'w', encoding='utf-8')
# 读取用户信息文件，格式为每行一个用户，用逗号隔开学号和密码
with codecs.open('/www/wwwroot/daka.sqlcow.com/user_info.txt', 'r',encoding='utf-8') as f:
    user_list = [line.strip().split(',') for line in f.readlines()]
        # 循环打卡
    for user in user_list:
            # 登录
            login_url = 'http://smse.fun-master.cn/report/login/dologin'
            login_data = {
                'stu_no': user[0],
                'password': user[1],
                'rememberme': '0',
            }
            login_headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': 'http://smse.fun-master.cn/report/login',
            }
            session = requests.Session()
            response = session.post(login_url, data=login_data, headers=login_headers)
            if response.json()['msg'] == '登录成功！':
                print('学号为{}的用户登录成功'.format(user[0]))
            else:
                print('学号为{}的用户登录失败'.format(user[0]))
                continue  # 登录失败则跳过该用户，进行下一个用户的打卡

            # 自动打卡
            report_url = 'http://smse.fun-master.cn/report/index/doreporthd'
            report_data = {
                'at_school': '1',
                'practise': '2',
                'current_province': '',
                'current_city': '',
                'current_area': '',
                'current_address': '',
                'mor_check': '',
                'non_check': '',
                'night_check': '',
                'under_check': '2',
                'new_contact': '2',
                'new_contact_desc': '',
                'new_contact1': '2',
                'new_contact1_desc': '',
                'mor_c': '2',
                'code': '1',
                'non_c': '2',
                'night_c': '2',
                'mor_desc': '',
                'non_desc': '',
                'night_desc': '',
                'less_check': '2',
                'less_check_desc': '',
                'seem_ill': '2',
            }
            report_headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': 'http://smse.fun-master.cn/report/index/index',
            }
            report_response = session.post(report_url, data=report_data, headers=report_headers)
            if report_response.json()['msg'] == '今日信息已经提交，感谢配合':
                print(now.strftime("当前时间为：%Y-%m-%d %H:%M:%S"))
                print('学号为{}的用户打卡成功'.format(user[0]))
            elif report_response.json()['msg'] == '今天已经提交过信息了':
                print(now.strftime("当前时间为：%Y-%m-%d %H:%M:%S"))
                print('学号为{}的用户今天已经打过卡了喔'.format(user[0]))
            else:
                print(now.strftime("当前时间为：%Y-%m-%d %H:%M:%S"))
                print('学号为{}的用户打卡失败了，哼哼哼'.format(user[0]))

            # 打印返回值
            # print(report_response.json())
# 关闭文件
sys.stdout.close()

# 将标准输出流重定向回控制台
sys.stdout = sys.__stdout__