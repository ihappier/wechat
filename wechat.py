from flask import Flask, request, make_response
import hashlib
import xml.etree.ElementTree as ET
from replymessage import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def wechat_auth():
    if request.method == 'GET':
        data = request.args
        token = 'zhutoufang'
        signature = data.get('signature', '')
        timestamp = data.get('timestamp', '')
        nonce = data.get('nonce', '')
        echostr = data.get('echostr', '')
        s = [timestamp, nonce, token]
        s.sort()
        s = ''.join(s).encode('utf-8')
        if (hashlib.sha1(s).hexdigest() == signature):
            return make_response(echostr)

    if request.method == 'POST':
        xml_str = request.stream.read()
        xml = ET.fromstring(xml_str)
        toUserName = xml.find('ToUserName').text
        fromUserName = xml.find('FromUserName').text
        createTime = xml.find('CreateTime').text
        msgType = xml.find('MsgType').text
        if msgType != 'text':
            reply = '''<xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[%s]]></MsgType>
            <Content><![CDATA[%s]]></Content>
            </xml>
            ''' % (fromUserName,
                   toUserName,
                   createTime,
                   'text',
                   '未知格式')
            return reply
        content = xml.find('Content').text
        print(content)
        msgId = xml.find('MsgId').text
        content_reply = reply_content(content)
        reply = '''
                        <xml>
                        <ToUserName><![CDATA[%s]]></ToUserName>
                        <FromUserName><![CDATA[%s]]></FromUserName>
                        <CreateTime>%s</CreateTime>
                        <MsgType><![CDATA[%s]]></MsgType>
                        <Content><![CDATA[%s]]></Content>
                        </xml>
                        ''' % (fromUserName, toUserName, createTime, msgType, content_reply)
        return reply


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
