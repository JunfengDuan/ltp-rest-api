# coding:utf-8
import re


def phone_number_recognition(text):
    """
    找到文中的所有数字串， 过滤出长度为11位的
    :param text:
    :return:
    """
    numbers = number_rule(text)
    nums = []
    for n in numbers:
        if len(n) == 11 and int(n[0]) == 1:
            nums.append(n)

    return str(dict(result=nums))


def id_recognition(text):
    """
    正则表示：
    第一位1-9  [1-9]
    后面5位数字0-9 \d{5}
    年份:1或2开头，后面三位数字0-9 [12]\d{3}
    月份:0开头接1-9或1开头接012  [0][1-9]|1[012]
    日期:0开头接1-9或1、2开头接0-9或3开头接0,1  0[1-9]|[12][0-9]|3[01]
    3位数字0-9 \d{3}
    最后一位为数字或X或x   \d|X|x
    :param text:
    :return:
    """

    id_pattern = '[1-9]\d{5}(?:19|20)\d\d(?:0[1-9]|1[012])(?:0[1-9]|[12]\d|3[01])\d{3}[0-9xX]'

    ids = re.findall(id_pattern, text)

    return str(dict(result=ids))


def number_rule(text):
    num_pattern = '[0-9]+'
    m = re.findall(num_pattern, text)
    return m

