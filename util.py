import os
import random
import re

def mkdirs(path):
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except:
            pass

#随机生成不重复文件名
def rand_file_name(path):
    while True:
        file_path = path + '/' + str(random.randint(0, 65535)) + '.txt'
        if not os.path.exists(file_path):
            return file_path

url_re = re.compile(r"[a-zA-z]+://[^\s]*")

def clear_url(line):
    return url_re.sub('', line)


def is_blank_line(line):
    for c in line:
        if c != ' ':
            return 0
    return 1


def clear_emoji(line):
    try:
        # Wide UCS-4 build
        emoji_re = re.compile(u'['
                              u'\U00010000-\U0010ffff'
                              u'\U0001F300-\U0001F64F'
                              u'\U0001F680-\U0001F6FF'
                              u'\u2600-\u2B55]+',
                              re.UNICODE)
    except re.error:
        # Narrow UCS-2 build
        emoji_re = re.compile(u'('
                              u'\ud83c[\udf00-\udfff]|'
                              u'\ud83d[\udc00-\ude4f\ude80-\udeff]|'
                              u'[\u2600-\u2B55])+',
                              re.UNICODE)
    return emoji_re.sub(r"[emoji]", line)