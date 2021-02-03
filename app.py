from flask import Flask, render_template, request

from deduplicator import Deduplicator


app = Flask(__name__)

duplicator = Deduplicator()


def showdedupl(string):
    return duplicator.isduplicate(string)


@app.route('/')
def my_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['u']
    return render_template('index2.html', res=str(showdedupl(text)))


if __name__ == '__main__':
    app.run()
