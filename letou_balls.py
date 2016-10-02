# coding=utf-8
from base_function import *
import re
import datetime


base_red_balls = ['01', '02', '03', '04', '05', '06', '07', '08', '09',
                  '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                  '20', '21', '22', '23', '24', '25', '26', '27', '28',
                  '29', '30', '31', '32', '33', '34', '35']
base_blue_balls = ['01', '02', '03', '04', '05', '06', '07', '08', '09',
                   '10', '11', '12']


def get_no(address):
    """取得大乐透结果所有页面数，并返回个数"""
    soup = get_code(address)
    data = soup.find_all(id='ContentPlaceHolderDefault_LabelTotalPages')[0]
    no = int(re.findall('\d\d', str(data))[0])
    return no


def get_new_result(address):
    """抓取大乐透每页的开奖数字，日期，期数，并以字典的形式返回"""
    result = []
    ball_blue_list = []
    ball_red_list = []
    soup = get_code(address)
    date = re.findall('\d{4}-\d{2}-\d{2}', str(soup.find_all(bgcolor=("#ffffff", "#f4f4f4"))))
    title = re.findall('\d{5}', str(soup.find_all(height='24')))
    ball_red = re.findall('\d{2} \d{2} \d{2} \d{2} \d{2}', str(soup.select('.FontRed')))
    ball_blue = re.findall('\d{2} \d{2}', str(soup.select('.FontBlue')))
    for m in ball_blue:
        ball_blue_list.append(re.findall('\d\d', m))
    for m in ball_red:
        ball_red_list.append(re.findall('\d{2}', m))
    for x in range(0, len(date)):
        result.append({'title': title[x], 'date': date[x], 'ball_five': ball_red_list[x],
                       'ball_double': ball_blue_list[x]})
    return result


def get_all_no(address):
    """遍历所有网页抓取所有大乐透结果"""
    result = []
    address_first = address + "1"
    range_no = get_no(address_first)
    for x in range(1, range_no):
        address_final = address + str(x)
        result.extend(get_new_result(address_final))
    len(result)
    return result


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
            print("大乐透" + date + '的数据已存')
            continue


def check_no_letou(id):
    """检查大乐透号码是否已存入数据库，未存入返回True"""
    if find_data_by_id(id) == []:
        return True


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


def insert_data(id_no, red_balls, blue_balls, date, name="data.db"):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO number VALUES (?,?,?,?)",
                   (id_no, red_balls, blue_balls, date))
    cursor.close()
    conn.commit()
    conn.close()


def find_data(red_balls, name="data.db"):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute("SELECT blue_balls FROM number WHERE red_balls = ?", (red_balls,))
    values = cursor.fetchall()
    return values


def find_data_by_id(id_no, name="data.db"):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute("SELECT red_balls FROM number WHERE id_no = ?", (id_no,))
    values = cursor.fetchall()
    return values


def get_nearest_letou_history(no):
    """获取大乐透历史数据，输入需要前几期"""
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT  * FROM NUMBER ORDER BY id_no DESC LIMIT 0,?", (no,))
    values = cursor.fetchall()
    return values


def compare_balls(red_balls, blue_balls):
    """判断这个号码有没有抽出过，如果抽出过返回False，反之返回True"""
    red_balls_final = list_to_str(red_balls)
    if find_data(red_balls_final) == []:
        return True
    else:
        blue_balls_compare = str_to_list(find_data(red_balls_final)[0][0])
        if blue_balls != blue_balls_compare:
            return True


def get_no():
    """获取大乐透号码"""
    # red_balls = create_balls(base_red_balls, 5)
    # blue_balls = create_balls(base_blue_balls, 2)
    # compare_balls(red_balls, blue_balls)
    # if compare_balls(red_balls, blue_balls):
    #     return '红球' + list_to_str(red_balls) + ',蓝球' + list_to_str(blue_balls)
    # else:
    #     get_no()
    id_no = str(int(get_nearest_letou_history(1)[0][0]) + 1)
    date = datetime.date.today().strftime('%Y-%m-%d')
    value_base = find_calculate_letou_data_by_id(id_no)
    if value_base == []:
        red_balls = create_balls(base_red_balls, 5)
        blue_balls = create_balls(base_blue_balls, 2)
        if compare_balls(red_balls, blue_balls):
            insert_number_cal_data(id_no, list_to_str(red_balls), blue_balls[0], date)
            values = find_calculate_dou_data(id_no)
            return values
        else:
            get_no()
    else:
        values = value_base
        return values
