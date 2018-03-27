# coding:utf-8
from flask import Flask, request

from ner.sxr_ner import sxr_ner
from ner.lxr_ner import lxr_ner


app = Flask(__name__)


@app.route('/sxr', methods=['GET', 'POST'])
def sxr():
    text = request.get_json().get('text')
    print('text:', text)

    if text is None or len(text) == 0:
        return ""

    return sxr_ner(text)


@app.route('/lxr', methods=['GET', 'POST'])
def lxr():
    text = request.get_json().get('text')
    print('text:', text)

    if text is None or len(text) == 0:
        return ""

    return lxr_ner(text)


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8083, debug=True)

