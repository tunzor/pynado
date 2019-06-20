from flask import Flask
import logging
import pynado

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
version = '3.0'

header = '<head><style>h4, p {background-color: seashell;}</style>' + \
         '<h2 style="background-color: mistyrose;">Welcome to <span style="color: seagreen;">Pynado</span>' \
         '<span style="color: olive;"> v' + version + '</span>!</h2>'


@app.route('/')
def index():
    app.logger.info('v' + version + ': welcome page')
    return header + \
           '<p>Input a word after the / in the address bar. <br/>For example, <a href="/hello">/hello</a></p>'


@app.route('/<word>')
def nadoize(word):
    app.logger.info('v' + version + ': nadoize word')
    return header + \
           '<p>The NATO alphabetized equivalent is:<br/><br/>' \
           '<span style="color: steelblue; font-size: 16pt; font-weight: bold;">' + \
           pynado.nadoize(word) + '</span></p>'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
