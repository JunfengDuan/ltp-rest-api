from ner.cn_ner import *


def org_ner(text):

    sent_str = text.replace('\n', '')

    entity = text_ner(sent_str)
    organizations = org_extract(entity)

    return str(dict(result=organizations))
