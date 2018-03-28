from ner.cn_ner import *


def address_ner(text):

    sent_str = text.replace('\n', '').replace(' ', '')

    entity = text_ner(sent_str)
    address = address_extract(entity)

    return str(dict(result=address))
