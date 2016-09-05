import requests
from bs4 import BeautifulSoup
import re

address_base = 'http://www.lottery.gov.cn/lottery/dlt/History.aspx?p='


def get_code(address):
    """获取页面源代码"""
    r = requests.get(address)
    return BeautifulSoup(r.text, 'html.parser')


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


def get_double_color_ball(address):
    """抓取双色球历史信息"""
    result = []
    ball_blue_list = []
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
                       'ball_blue': ball_blue_list[x], 'title': id_no_list[x]},)
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

