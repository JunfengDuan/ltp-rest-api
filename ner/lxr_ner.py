# coding:utf-8
from ner.cn_ner import *

sxr = read_sxr('sxr.txt')


def lxr_ner(text):

    sentences = get_effect_sent(text)
    sent_str = " ".join(sentences)

    entity = text_ner(sent_str, 'dict/lxr_lexicon.txt')
    lxr_set = lxr_extract(entity)

    data = []
    for name in lxr_set:
        if name not in sxr:
            data.append(name)
    return str(data)
