import random
import requests
from bs4 import BeautifulSoup
from create_sqlite import *


def create_balls(base_ball, number):
    red_balls = sorted(random.sample(base_ball, number))
    return red_balls


def compare_rewards(flag):
    """比较红球的命中数与蓝球的命中数"""
    if flag == "双色球":
        id_no = get_nearest_double_history(1)[0][0]
        values_calculate = find_calculate_dou_data(id_no)
        values_rewards = get_nearest_double_history(1)
    elif flag == "大乐透":
        id_no = get_nearest_letou_history(1)[0][0]
        values_calculate = find_calculate_letou_data_by_id(id_no)
        values_rewards = get_nearest_letou_history(1)
    if values_calculate == []:
        return False
    else:
        return [compare_balls(str_to_list(values_calculate[0][1]),
                              str_to_list(values_rewards[0][1])),
                compare_balls(str_to_list(values_calculate[0][2]),
                              str_to_list(values_rewards[0][2])),
                ]


def compare_balls(balls_calculate, balls_get):
    """比较预测的结果与实际的结果，列出一致的，以列表的形式返回"""
    balls_in = []
    for ball in balls_calculate:
        if ball in balls_get:
            balls_in.append(ball)
    return balls_in


def list_to_str(list_to_turn):
    """将列表转为字符串"""
    result = ','.join(list_to_turn)
    return result


def str_to_list(str_to_turn):
    """将字符串转为列表"""
    result = str_to_turn.split(',')
    return result


def get_code(address):
    """获取页面源代码"""
    r = requests.get(address)
    return BeautifulSoup(r.text, 'html.parser')
