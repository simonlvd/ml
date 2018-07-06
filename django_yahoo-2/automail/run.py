# !/Users/simon/anaconda3/bin/python
# coding = utf-8
import imaplib
import re
import email
import requests
from bs4 import BeautifulSoup


def urlGet(url):
    try:
        response = requests.get(url)
        print('请求成功:',response)
    except:
        print('请求失败!')


def parseEmail(msg):
    # sub = msg.get('subject')
    body = []
    for part in msg.walk():
        # 如果ture的话内容是没用的
        if not part.is_multipart():
            body.append(part.get_payload(decode=True).decode('utf-8'))
            # 解码出文本内容，直接输出来就可以了。
    # return {"sub": sub, "body": " ".join(body)}
    return {"body": " ".join(body)}


def getUrl(content):
    text = BeautifulSoup(content, 'lxml')
    urls = text.findAll('a')
    pattern = re.compile(r"https://www\.coinex\.com/my/wallet.*")
    for u in urls:
        # print(u['href'])
        match = pattern.match(u['href'])
        if match:
            print(match.group())
            urlGet(match.group())
        # else:
        #     print('暂无需求')
        # print(u)

def MailVerify(Email, Password):
    ret = ''
    try:
        M = imaplib.IMAP4_SSL('imap.mail.yahoo.com')
        ret = M.login(Email, Password)

    except BaseException:
        print('login fail')
        # writ_add_to_excel(Email, Password)
    retR = re.compile('^\(\'OK')
    if(retR.match(str(ret))):
        print("login succeed!")
        M.select()
        # type, data = M.search(None, 'ALL')
        type, data = M.search(None, 'UnSeen')
        newlist = data[0].split()
        # print(newlist)
        if newlist is not None:
            for i in range(0,len(newlist)):
            # for i in range(0, 10):
                type, data1 = M.fetch(newlist[i], '(RFC822)')
                # print(data1[0][1].decode('utf-8'))
                msg = email.message_from_string(data1[0][1].decode('utf-8'))
                # print(msg)
                res = parseEmail(msg)
                # print(res['body'])
                getUrl(content=res['body'])


