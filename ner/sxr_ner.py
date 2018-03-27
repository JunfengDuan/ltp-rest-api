# coding:utf-8

from ner.cn_ner import *

sxr = read_sxr('sxr.txt')
sxr_rel_dict, sxr_rel_list = read_sxr_rel('rel.txt')


def sxr_ner(text):

    print('sxr:', sxr)
    print('sxr_rel_list:', sxr_rel_list)

    sents = get_effect_sent(text)
    sent_str = " ".join(sents)

    objects = []
    entity = text_ner(sent_str, 'dict/sxr_lexicon.txt')
    sxr_objects = sx_object_extract(entity)
    if sxr_objects:
        objects.extend(sxr_objects)

    print('objects:', objects)
    obj = []
    for o in objects:
        bt = ''
        for s in sxr:
            if o in s and s in sent_str:
                if bt in s:
                    bt = s
        if len(bt) > 0 and bt not in obj:
            obj.append(bt)

    full_name = name_link(obj)
    data = str(full_name)
    return data


def name_link(ner_name):
    for i, name in enumerate(ner_name):
        for rel in sxr_rel_list:
            if name in rel:
                ner_name[i] = rel[0]
    return ner_name

