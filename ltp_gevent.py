# coding:utf-8
from flask import Flask, request
from flask_cors import CORS
import ner.core_nlp as nlp
from gevent.pywsgi import WSGIServer

app = Flask(__name__)
CORS(app)


@app.route('/ltp/seg', methods=['GET', 'POST'])
def seg():

    text = request.get_json().get('text')

    print('text:', text)
    text = text.replace('\n', '')

    if text is None or len(text) == 0:
        return ""

    segment = nlp.text_seg(text)
    print('segment:', segment)

    return str(segment)


@app.route('/ltp/pos', methods=['GET', 'POST'])
def pos():

    text = request.get_json().get('text')

    print('text:', text)
    text = text.replace('\n', '')

    if text is None or len(text) == 0:
        return ""

    pos = nlp.text_pos(text)
    print('pos:', pos)

    return str(pos)


@app.route('/ltp/ner', methods=['GET', 'POST'])
def ner():

    text = request.get_json().get('text')

    print('text:', text)
    text = text.replace('\n', '')

    if text is None or len(text) == 0:
        return ""

    entities = nlp.text_ner(text)
    print('ner:', entities)

    return str(entities)


@app.route('/ltp/parse', methods=['GET', 'POST'])
def parse():

    text = request.get_json().get('text')

    print('text:', text)
    text = text.replace('\n', '')

    if text is None or len(text) == 0:
        return ""

    parsers = nlp.text_parse(text)
    print('parsers:', parsers)

    return str(parsers)


@app.route('/ltp/srl', methods=['GET', 'POST'])
def srl():

    text = request.get_json().get('text')

    print('text:', text)
    text = text.replace('\n', '')

    if text is None or len(text) == 0:
        return ""

    roles = nlp.text_srl(text)
    print('roles:', roles)

    return str(roles)


gevent_server = WSGIServer(('', 8082), app)
gevent_server.serve_forever()

