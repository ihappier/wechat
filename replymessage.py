from calculate import *


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
        format_content_blue = "蓝球都被狗吃了"
    format_content = format_content_red + format_content_blue
    return format_content


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
    reply = "输入双色球获得双色球预测\n输入历史获得最近5期双色球开奖结果\n"
    return reply


def reply_reward():
    if compare_rewards():
        reply = format_rewards_information(compare_rewards())
    else:
        reply = "Sorry,上次木有买彩票哦"
    return reply


def reply_content(content):
    reply = "欢迎使用本公众号\n" \
            "请输入帮助或help获取使用指南"
    if "帮助" in content:
        reply = reply_help()
    if "双色球" in content:
        reply = reply_dou_balls()
    if "历史" in content:
        reply = double_ball_history(5)
    if "中奖" in content:
        reply = reply_reward()
    return reply
