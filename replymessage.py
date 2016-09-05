from calculate import *


def format_ball_information(content):
    format_content = ''
    for m in content:
        format_content = format_content + '期号: ' + m[0] + '\n红球: ' + m[1] +\
                         '\n蓝球: ' + m[2] + '\n日期: ' + m[3] + '\n\n'
    return format_content


def format_rewards_information(content):
    format_content = "中奖"


def double_ball_history(no):
    """公众号获取双色球历史回复"""
    content = get_nearest_double_history(no)
    return format_ball_information(content)


def reply_dou_balls():
    """公众号获取计算双色球回复"""
    content = get_double_no()
    return "双色球预测：" + "\n" + format_ball_information(content)


def reply_help():
    """帮助信息格式"""
    reply = "输入双色球或1获得双色球预测\n输入历史或5获得最近5期双色球开奖结果"
    return reply


def reply_reward():
    if compare_rewards():
        reply =

def reply_content(content):
    reply = "欢迎使用本公众号\n" \
            "请输入帮助或help获取使用指南"
    if "帮助" in content:
        reply = reply_help()
    if "双色球" in content:
        reply = reply_dou_balls()
    elif "历史" in content:
        reply = double_ball_history(1)
    return reply

