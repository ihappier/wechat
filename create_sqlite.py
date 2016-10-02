# coding=utf-8
import sqlite3


def create_database(name="data.db"):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE number_dou_balls (id_no VARCHAR(20) PRIMARY KEY,"
                   " red_balls VARCHAR(20),"
                   "blue_balls VARCHAR(20),"
                   "date VARCHAR(20))"),
    cursor.close()
    conn.commit()
    conn.close()


def create_cal_letou_data():
    """创建预测大乐透的表"""
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute(
        "create table number_calculate (id_no VARCHAR (20) PRIMARY KEY, "
        "red_ball VARCHAR (20), blue_ball VARCHAR (20), date VARCHAR (20))")
    cursor.close()
    conn.commit()
    conn.close()


def find_calculate_letou_data_by_id(id_no):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * from number_calculate where id_no = ?", (id_no,))
    values = cursor.fetchall()
    return values


def insert_number_cal_data(id_no, red_balls, blue_balls, date, name="data.db"):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO number_calculate VALUES (?,?,?,?)",
                   (id_no, red_balls, blue_balls, date))
    cursor.close()
    conn.commit()
    conn.close()


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


def get_nearest_double_history(no):
    """获取最近 NO 期双色球数据"""
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT  * FROM number_dou_balls ORDER BY id_no DESC LIMIT 0,?", (no,))
    values = cursor.fetchall()
    return values


def find_calculate_dou_data_by_id(id_no):
    """通过ID获取预测的双色球数据"""
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM calculate_dou_balls WHERE id_no = ?", (id_no,))
    values = cursor.fetchall()
    return values


def find_double_balls_data_by_id(id_no, name="data.db"):
    """通过ID获取抓取的到的双色球开奖数据"""
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute("SELECT red_balls FROM number_dou_balls WHERE id_no = ?", (id_no,))
    values = cursor.fetchall()
    return values


def find_double_balls_data(red_balls, name="data.db"):
    """通过红球获取双色球开奖数据"""
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute("SELECT blue_balls FROM number_dou_balls WHERE red_balls = ?", (red_balls,))
    values = cursor.fetchall()
    return values


def insert_double_balls_data(id_no, red_balls, blue_balls, date, name="data.db"):
    """插入双色球开奖数据"""
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO number_dou_balls VALUES (?,?,?,?)",
                   (id_no, red_balls, blue_balls, date))
    cursor.close()
    conn.commit()
    conn.close()


def get_ball_double_table(name='data.db'):
    """创建计算双色球的表"""
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE calculate_dou_balls (id_no VARCHAR(20) PRIMARY KEY , red_balls VARCHAR (20),"
                   " blue_balls VARCHAR (20), "
                   "date VARCHAR (20))")
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



