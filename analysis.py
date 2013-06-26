#---coding:UTF-8--

from sys import argv
from datetime import date
import os
import re
import datetime
import time
from html import *
from send_email import *
from config import *

# get args,if start_date = 0 and date_count = 0 get yestoday
script, start_date, date_count = argv


# one line result


def one_line_result(line):
    if line.find('GrantType') > 0:
        return None
    usefull_str = line.split(' ')[1]
    line_result = usefull_str.split(':')
    if len(line_result) != 3:
        return None
    return line_result

# get dates for you want logs


def get_dates(is_yesterday):
    if is_yesterday:
        today = date.today()
        yestoday = today + datetime.timedelta(days=-1)
        return [yestoday.strftime('%Y-%m-%d')]
    else:
        your_year = start_date.split('-')[0]
        your_month = start_date.split('-')[1]
        your_day = start_date.split('-')[2]
        your_date = date(int(your_year), int(your_month), int(your_day))
        dates = []
        for x in xrange(0, int(date_count)):
            dates.append((your_date + datetime.timedelta(
                days=x)).strftime('%Y-%m-%d'))
        return dates


# analysis log and return a map


def analysis():
    # key = appId_tokentype value = [total_count, user_count]
    result = {}
    # key = app_id value = [user_id]
    app_user_map = {}
    dates = None

    if '0' == start_date and '0' == date_count:
        dates = get_dates(True)
    else:
        dates = get_dates(False)
    # analysis by date
    for date in dates:
        log_path = log_root_path + date
        if not os.path.exists(log_path):
            print "the log path not exists"  # not analysis because the log path not exists
            os._exit(0)
        for log in log_names:
            file_name = log_path + "/" + log
            if not os.path.isfile(file_name):
                print "the log not exists"  # not analysis because the log not exists
                os._exit(0)
            txt = open(file_name, 'r')
            for line in txt:
                line_result = one_line_result(line)
                if line_result == None:
                    continue
                app_id = line_result[0]
                user_id = line_result[1]
                token_type = line_result[2]
                key = str(app_id) + "_" + str(token_type)
                # app has already exists in app_user_map
                if app_user_map.has_key(app_id):
                    app_user_map[app_id].append(user_id)
                else:
                    app_user_map[app_id] = [user_id]
                # app_token_type has already exists in reslut
                if result.has_key(key):
                    result[key] += 1
                else:
                    result[key] = 1
    for app_user in app_user_map.keys():
        app_user_set = set(app_user_map[app_user])
        app_user_map[app_user] = len(app_user_set)

    app_user_list = []
    for app_user in app_user_map.keys():
        app_user_list.append([app_user_map[app_user], app_user])

    app_user_list.sort()
    app_user_list.reverse()
    return [result, app_user_list]


# get keys


def get_keys(app_user):
    keys = []
    keys.append(str(app_user[1]) + "_" + str(0))
    keys.append(str(app_user[1]) + "_" + str(1))
    keys.append(str(app_user[1]) + "_" + str(2))
    keys.append(str(app_user[1]) + "_" + str(3))
    keys.append(str(app_user[1]) + "_" + str(4))
    return keys

# get token type


def get_token_type(key):
    type_int = key.split('_')[1]
    return token_types[int(type_int)]

# send email to relate body


def get_email_content(result):
    message = "邮件中为top100；详细信息见附件。\n若对应的值为-1：表示没有此类型的数据。\n"
    message += get_html_head()
    message += get_talbe_head('1200', '1', [
                              'AppId', '授权用户数', '授权的类型', '授权对应的数量'])
    body_message = ""
    i = 1
    for app_user in result[1]:
	i = i + 1
        keys = get_keys(app_user)
        flag = False
        for key in keys:
            if flag:
                message += get_tr_head()
            else:
                message += get_tr_head()
                message += get_td_whit_rowspan('5', str(app_user[1]))
                message += get_td_whit_rowspan('5', str(app_user[0]))
            message += get_td(str(get_token_type(key)))
            if result[0].has_key(key + "\n"):
                message += get_td(str(result[0][key + "\n"]))
            else:
                message += get_td('-1')
            message += get_tr_end()
            flag = True
        message += get_tr_end()
	if i == 100:
	    body_message = message + get_talbe_end() + get_end_html()
    message += get_talbe_end()
    message += get_end_html()
    return [message, body_message]

# main function


def main():
    send(get_email_content(analysis()), email_receiver, subject)


# call main function
if __name__ == '__main__':
    main()
