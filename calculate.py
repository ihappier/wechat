from create_sqlite import *
import random

base_red_balls = ['01', '02', '03', '04', '05', '06', '07', '08', '09',
                  '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                  '20', '21', '22', '23', '24', '25', '26', '27', '28',
                  '29', '30', '31', '32', '33', '34', '35']
base_blue_balls = ['01', '02', '03', '04', '05', '06', '07', '08', '09',
                   '10', '11', '12']
base_double_red_balls = ['01', '02', '03', '04', '05', '06', '07', '08', '09',
                         '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                         '20', '21', '22', '23', '24', '25', '26', '27', '28',
                         '29', '30', '31', '32', '33']
base_double_blue_balls = ['01', '02', '03', '04', '05', '06', '07', '08', '09',
                          '10', '11', '12', '13', '14', '15', '16']


def create_balls(base_ball, number):
    red_balls = sorted(random.sample(base_ball, number))
    return red_balls


def compare_balls(red_balls, blue_balls):
    """判断这个号码有没有抽出过，如果抽出过返回False，反之返回True"""
    red_balls_final = list_to_str(red_balls)
    if find_data(red_balls_final) == []:
        return True
    else:
        blue_balls_compare = find_data(red_balls_final)[0][0].split()
        if blue_balls != blue_balls_compare:
            return True


def get_no():
    """获取大乐透号码"""
    red_balls = create_balls(base_red_balls, 5)
    blue_balls = create_balls(base_blue_balls, 2)
    compare_balls(red_balls, blue_balls)
    if compare_balls(red_balls, blue_balls):
        return '红球' + list_to_str(red_balls) + ',蓝球' + list_to_str(blue_balls)
    else:
        get_no()


def compare_double_balls(red_balls, blue_balls):
    """判断双色球这个号码有没有抽出过，如果抽出过返回False，反之返回True"""
    red_balls_final = list_to_str(red_balls)
    if find_double_balls_data(red_balls_final) == []:
        return True
    else:
        blue_balls_compare = find_double_balls_data(red_balls_final)[0][0]
        if blue_balls[0] != blue_balls_compare:
            return True


def get_double_no():
    """获取双色球号码并存储"""
    id_no = str(int(get_nearest_double_history(1)[0][0]) + 1)
    date = datetime.date.today().strftime('%Y-%m-%d')
    value_base = find_calculate_dou_data(id_no)
    if value_base == []:
        red_balls = create_balls(base_double_red_balls, 6)
        blue_balls = create_balls(base_double_blue_balls, 1)
        if compare_double_balls(red_balls, blue_balls):
            insert_calculate_dou_data(id_no, list_to_str(red_balls), blue_balls[0], date)
            values = find_calculate_dou_data(id_no)
            return values
        else:
            get_double_no()
    else:
        values = value_base
        return values


def compare_rewards():
    id_no = get_nearest_double_history(1)[0][0]
    values_calculate = find_calculate_dou_data(id_no)
    values_rewards = get_nearest_double_history(1)
    if values_calculate ==[]:
        return False
    else:
        return[compare_balls(str_to_list(values_calculate[0][1]),
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