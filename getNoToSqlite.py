from spiders import *
from calculate import *


def store_letou():
    """大乐透结果存入sqlite"""
    address_base = 'http://www.lottery.gov.cn/lottery/dlt/History.aspx?p='
    result = get_all_no(address_base)
    len(result)
    for x in range(0, len(result)):
        id_no = result[x]['title']
        red_balls = list_to_str(result[x]['ball_five'])
        blue_balls = list_to_str(result[x]['ball_double'])
        date = result[x]['date']
        if find_data_by_id(id_no) == []:
            insert_data(id_no, red_balls, blue_balls, date)
        else:
            continue


def store_double():
    """双色球结果存之"""
    address = 'http://baidu.lecai.com/lottery/draw/list/50'
    result = get_double_color_ball(address)
    for x in range(0, len(result)):
        id_no = result[x]['title']
        red_balls = list_to_str(result[x]['ball_red'])
        blue_balls = result[x]['ball_blue']
        date = result[x]['date']
        if check_no_double(id_no):
            insert_double_balls_data(id_no, red_balls, blue_balls, date)
        else:
            print(date + '的数据已存入')
            continue


def store_lelou_everyday():
    """存入大乐透数据"""
    address = 'http://www.lottery.gov.cn/lottery/dlt/History.aspx?p=1'
    result = get_new_result(address)
    for x in range(0, len(result)):
        id_no = result[x]['title']
        red_balls = list_to_str(result[x]['ball_five'])
        blue_balls = list_to_str(result[x]['ball_double'])
        date = result[x]['date']
        if check_no_letou(id_no):
            insert_data(id_no, red_balls, blue_balls, date)
        else:
            print(date + '的数据已存')
            continue


def check_no_letou(id):
    """检查大乐透号码是否已存入数据库，未存入返回True"""
    if find_data_by_id(id) == []:
        return True


def check_no_double(id):
    """检查双色球号码是否存入数据库，为存入返回True"""
    if find_double_balls_data_by_id(id) == []:
        return True


def store_dou_calculte():
    date = datetime.date.today().strftime('%Y-%m-%d')
    if find_calculate_dou_data(date) == []:
        insert_calculate_dou_data(get_double_no()[0], get_double_no()[1], date)


store_double()