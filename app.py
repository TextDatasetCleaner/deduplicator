from flask import Flask, jsonify, render_template, request

from deduplicator import Deduplicator  # noqa: I001


app = Flask(__name__)

duplicator = Deduplicator()


def showdedupl(string):
    return duplicator.isduplicate(string)


@app.route('/')
def my_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['input']
    return jsonify({'data': showdedupl(text)})


if __name__ == '__main__':
    app.run()
