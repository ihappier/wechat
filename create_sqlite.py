import sqlite3
import datetime


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


def get_ball_double_table(name='data.db'):
    """创建计算大乐透的表"""
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute("create table calculate_dou_balls (id_no varchar(20) PRIMARY KEY , red_balls VARCHAR (20),"
                   " blue_balls VARCHAR (20), "
                   "date VARCHAR (20))")
    cursor.close()
    conn.commit()
    conn.close()


def insert_calculate_dou_data(id_no, red_balls, blue_balls, date, name="data.db"):
    """往计算大乐透的表中插入数值"""
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
    cursor.execute("select red_balls from number WHERE id_no = ?", (id_no,))
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


def find_double_balls_data(red_balls, name="data.db"):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute("SELECT blue_balls FROM number_dou_balls WHERE red_balls = ?", (red_balls,))
    values = cursor.fetchall()
    return values


def find_double_balls_data_by_id(id_no, name="data.db"):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute("select red_balls from number_dou_balls WHERE id_no = ?", (id_no,))
    values = cursor.fetchall()
    return values


def get_nearest_letou_history(no):
    """获取大乐透历史数据，输入需要前几期"""
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("select  * from NUMBER ORDER BY id_no DESC LIMIT 0,?", (no,))
    values = cursor.fetchall()
    return values


def get_nearest_double_history(no):
    """获取最近 NO 期双色球数据"""
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("select  * from number_dou_balls ORDER BY id_no DESC LIMIT 0,?", (no,))
    values = cursor.fetchall()
    return values


def find_calculate_dou_data_by_id(id_no):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    id_no
    cursor.execute("select * from calculate_dou_balls WHERE id_no = ?", (id_no,))
    values = cursor.fetchall()
    return values

