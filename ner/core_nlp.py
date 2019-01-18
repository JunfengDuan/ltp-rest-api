# coding:utf-8

from ner import model_load as extract


# 分词
def text_seg(sentence):
    word = list(extract.segment(sentence))
    result = []
    for i, item in enumerate(word):
        result.append({'id': i, 'word': item})
    return result


# 词性标注
def text_pos(sentence):
    word = extract.segment(sentence)
    pos = extract.pos(word)
    result = []
    for i, item in enumerate(zip(word, pos)):
        result.append({'id': i, 'word': item[0], 'pos': item[1]})
    return result


# 命名实体识别
def text_ner(sentence):
    word = extract.segment(sentence)
    pos = extract.pos(word)
    ner = extract.ner(word, pos)
    result = []
    for i, item in enumerate(zip(word, pos, ner)):
        result.append({'id': i, 'word': item[0], 'pos': item[1], 'ne': item[2]})
    return result


# 依存句法分析
def text_parse(sentence):
    word = extract.segment(sentence)
    pos = extract.pos(word)
    parsers, _ = extract.parse(word, pos)

    result = []
    for i, item in enumerate(zip(word, pos, parsers)):
        result.append({'id': i, 'word': item[0], 'pos': item[1], 'parent': int(item[2][0])-1, 'relate': item[2][1]})

    return result


# 语义角色标注
def text_srl(sentence):
    word = extract.segment(sentence)
    pos = extract.pos(word)
    _, arcs = extract.parse(word, pos)
    roles = extract.srl(word, pos, arcs)
    seg = text_seg(sentence)
    result = []
    for item in roles:
        result.append({'id': item[0], 'type': item[1], 'beg': item[2], 'end': item[3]})
    return {'seg': seg, 'role': result}


# 读文件
def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()
    return data



