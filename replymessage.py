from double_balls import *
from letou_balls import *
import jieba


def format_ball_information(content):
    format_content = ''
    for m in content:
        format_content = format_content + '期号: ' + m[0] + '\n红球: ' + m[1] + \
                         '\n蓝球: ' + m[2] + '\n日期: ' + m[3] + '\n\n'
    return format_content


def format_rewards_information(content, flag):
    # if len(content[1]) > 0:
    #     format_content_red = "红球中奖" + str(len(content[1])) + "个,号码为" + list_to_str(content[1]) + "\n"
    # else:
    #     format_content_red = "红球都被狗吃了\n"
    # if len(content[2]) > 0:
    #     format_content_blue = "蓝球中奖" + str(len(content[2])) + "个,号码为" + list_to_str(content[2]) + "\n"
    # else:
    #     format_content_blue = "蓝球都被狗吃了\n"
    # format_content = flag + "\n第 " + content[0] + " 期\n" + format_content_red + format_content_blue
    if len(content[2]) > 0 or len(content[1]) > 3:
        format_content_red = "红球中奖" + str(len(content[1])) + "个,号码为" + list_to_str(content[1]) + "\n"
        format_content_blue = "蓝球中奖" + str(len(content[2])) + "个,号码为" + list_to_str(content[2]) + "\n"
        format_content = flag + "\n第 " + content[0] + " 期\n" + format_content_red + format_content_blue
    else:
        format_content = "没有中奖"
    return format_content


def history(flag, no):
    """公众号获取双色球历史回复"""
    if flag == "双色球":
        content = get_nearest_double_history(no)
        return flag + "近5期开奖情况：\n" + format_ball_information(content)
    if flag == "大乐透":
        content = get_nearest_letou_history(no)
        return flag + "近5期开奖情况：\n" + format_ball_information(content)


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
        reply = format_rewards_information(compare_rewards(flag), flag)
    else:
        reply = "Sorry,上次木有买彩票哦"
    return reply


def reply_content(content):
    reply = "欢迎使用本公众号\n" \
            "请输入帮助获取使用指南\n"
    content_resolved = content_resolve(content)
    if "帮助" in content_resolved:
        reply = reply_help()
    if "双色球" in content_resolved:
        reply = reply_balls("双色球")
    if "大乐透" in content_resolved:
        reply = reply_balls("大乐透")
    if "双色球" in content_resolved and "历史" in content_resolved:
        reply = history("双色球", 5)
    if "双色球" in content_resolved and "中奖" in content_resolved:
        reply = reply_reward("双色球")
    if "大乐透" in content_resolved and "中奖" in content_resolved:
        reply = reply_reward("大乐透")
    if "大乐透" in content_resolved and "历史" in content_resolved:
        reply = history("大乐透", 5)
    return reply


def content_resolve(content_to_reply):
    """结巴分词分析提取微信获得的内容"""
    content = jieba.cut(content_to_reply)
    content_resolved = ','.join(content).split(',')
    return content_resolved
