from double_balls import *
from letou_balls import *
import jieba


def format_ball_information(content):
    format_content = ''
    for m in content:
        format_content = format_content + '期号: ' + m[0] + '\n红球: ' + m[1] + \
                         '\n蓝球: ' + m[2] + '\n日期: ' + m[3] + '\n\n'
    return format_content


def format_rewards_information(content):
    if len(content[0]) > 0:
        format_content_red = "红球中奖" + str(len(content[0])) + "个,号码为" + list_to_str(content[0]) + "\n"
    else:
        format_content_red = "红球都被狗吃了"
    if len(content[1]) > 0:
        format_content_blue = "蓝球中奖" + str(len(content[1])) + "个,号码为" + list_to_str(content[1]) + "\n"
    else:
        format_content_blue = "蓝球都被狗吃了\n"
    format_content = format_content_red + format_content_blue
    return format_content


def history(flag, no):
    """公众号获取双色球历史回复"""
    if flag == "双色球":
        content = get_nearest_double_history(no)
        return format_ball_information(content)
    if flag == "大乐透":
        content = get_nearest_letou_history(no)
        return format_ball_information(content)


def reply_balls(flag):
    """公众号获取计算彩票回复"""
    if flag == "双色球":
        content = get_double_no()
        return "双色球预测：" + "\n" + format_ball_information(content)
    if flag == "大乐透":
        content = get_no()
        return "大乐透预测：" + "\n" + format_ball_information(content)


def reply_help():
    """帮助信息格式"""
    reply = "输入双色球获得双色球预测\n输入历史获得最近5期双色球开奖结果\n"
    return reply


def reply_reward(flag):
    if compare_rewards(flag):
        reply = format_rewards_information(compare_rewards(flag))
    else:
        reply = "Sorry,上次木有买彩票哦"
    return reply


def reply_content(content):
    reply = "欢迎使用本公众号\n" \
            "请输入帮助或help获取使用指南\n"
    print(content)
    if "帮助" in content:
        reply = reply_help()
    if "双色球" in content:
        reply = reply_balls("双色球")
    if "大乐透" in content:
        reply = reply_balls("大乐透")
    if "双色球历史" in content:
        reply = history("双色球", 5)
    if "双色球中奖" in content:
        reply = reply_reward("双色球")
    if "大乐透中奖" in content:
        reply = reply_reward("大乐透")
    if "大乐透历史" in content:
        reply = history("大乐透", 5)
    return reply
