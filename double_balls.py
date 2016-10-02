# coding=utf-8
import re
import datetime
from base_function import *

base_double_red_balls = ['01', '02', '03', '04', '05', '06', '07', '08', '09',
                         '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                         '20', '21', '22', '23', '24', '25', '26', '27', '28',
                         '29', '30', '31', '32', '33']
base_double_blue_balls = ['01', '02', '03', '04', '05', '06', '07', '08', '09',
                          '10', '11', '12', '13', '14', '15', '16']


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
    """预测双色球号码并存储"""
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


def check_no_double(id):
    """检查双色球号码是否存入数据库，为存入返回True"""
    if find_double_balls_data_by_id(id) == []:
        return True


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
            print("双色球" + date + '的数据已存入')
            continue


def get_nearest_double_history(no):
    """获取最近 NO 期双色球数据"""
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT  * FROM number_dou_balls ORDER BY id_no DESC LIMIT 0,?", (no,))
    values = cursor.fetchall()
    return values


def find_calculate_dou_data_by_id(id_no):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    id_no
    cursor.execute("SELECT * FROM calculate_dou_balls WHERE id_no = ?", (id_no,))
    values = cursor.fetchall()
    return values


def find_double_balls_data(red_balls, name="data.db"):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute("SELECT blue_balls FROM number_dou_balls WHERE red_balls = ?", (red_balls,))
    values = cursor.fetchall()
    return values


def find_double_balls_data_by_id(id_no, name="data.db"):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute("SELECT red_balls FROM number_dou_balls WHERE id_no = ?", (id_no,))
    values = cursor.fetchall()
    return values


def insert_double_balls_data(id_no, red_balls, blue_balls, date, name="data.db"):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO number_dou_balls VALUES (?,?,?,?)",
                   (id_no, red_balls, blue_balls, date))
    cursor.close()
    conn.commit()
    conn.close()


def insert_calculate_dou_data(id_no, red_balls, blue_balls, date, name="data.db"):
    """往计算双色球的表中插入数值"""
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO calculate_dou_balls VALUES (?,?,?,?)",
                   (id_no, red_balls, blue_balls, date))
    cursor.close()
    conn.commit()
    conn.close()


def find_calculate_dou_data(id_no, name="data.db"):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM calculate_dou_balls WHERE id_no = ?", (id_no,))
    values = cursor.fetchall()
    return values


def get_double_color_ball(address):
    """抓取双色球历史信息"""
    result = []
    id_no_list = []
    ball_red_list = []
    soup = get_code(address)
    date = re.findall('\d{4}-\d{2}-\d{2}', str(soup.text))
    id_no_base_list = re.findall('2016\d\d\d', str(soup))
    for x in id_no_base_list:
        if x not in id_no_list:
            id_no_list.append(x)
    ball_red = re.findall('<em>\d\d</em><em>\d\d</em><em>\d\d</em><em>\d\d</em><em>\d\d</em><em>\d\d</em>',
                          str(soup.select('.redBalls')))
    ball_blue_list = re.findall('\d\d', str(soup.select('.blueBalls')))
    for m in ball_red:
        ball_red_list.append(re.findall('\d\d', m))
    for x in range(0, len(date)):
        result.append({'date': date[x], 'ball_red': ball_red_list[x],
                       'ball_blue': ball_blue_list[x], 'title': id_no_list[x]}, )
    return result
