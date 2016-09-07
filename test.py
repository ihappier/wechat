from replymessage import reply_content


content = ['帮助', '双色球历史', '双色球', '双色球中奖', "大乐透", "大乐透历史", "大乐透中奖"]
for m in content:
    print(reply_content(m))
# import jieba
#
#
# content = "告诉我双色球历史"
# c = jieba.cut(content)
#
# s = ','.join(c)
# print(s)
# m = s.split(',')
# print(m)
# if "双色球" in m and "历史" in m:
#     print(2)
