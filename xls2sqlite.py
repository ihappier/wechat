import xlrd
from create_sqlite import *

file_name = ['G:\\Python\\resultSpider\\2013.xls',
             'G:\\Python\\resultSpider\\2014.xls',
             'G:\\Python\\resultSpider\\2015.xls']

file_double_balls = ['G:\\Python\\resultSpider\\2003.xls',
                     'G:\\Python\\resultSpider\\2004.xls',
                     'G:\\Python\\resultSpider\\2005.xls',
                     'G:\\Python\\resultSpider\\2006.xls',
                     'G:\\Python\\resultSpider\\2007.xls',
                     'G:\\Python\\resultSpider\\2008.xls',
                     'G:\\Python\\resultSpider\\2009.xls',
                     'G:\\Python\\resultSpider\\2010.xls',
                     'G:\\Python\\resultSpider\\2011.xls',
                     'G:\\Python\\resultSpider\\2012.xls',
                     'G:\\Python\\resultSpider\\2013_1.xls',
                     'G:\\Python\\resultSpider\\2014_1.xls',
                     'G:\\Python\\resultSpider\\2015_1.xls',
                     ]


def open_xls(file):
    """打开excle文件，并读取数据"""
    try:
        data = xlrd.open_workbook(file)
        sheet = data.sheet_by_index(0)
        return sheet
    except Exception as e:
        print(str(e))


def get_balls(data):
    """提取红球和蓝球数据，前面为红球，后面为蓝球"""
    a = data.split('|')
    return a


def xls_to_sqlites(file):
    """读取excel中数据并添加到sqlite中"""
    i = 0
    sheets = open_xls(file)
    for i in range(sheets.nrows):
        id_no = str(int(sheets.row_values(i)[0]))  # 获取期数
        red_ball = str(get_balls(sheets.row_values(i)[1])[0])  # 获取红球号码
        blue_ball = str(get_balls(sheets.row_values(i)[1])[1])  # 获取蓝球号码
        date = str(sheets.row_values(i)[2])  # 获取日期
        if find_double_balls_data(red_ball) == []:
            insert_double_balls_data(id_no, red_ball, blue_ball, date)  # 添加到sqlite中


# for m in file_double_balls:
#     xls_to_sqlites(m)
