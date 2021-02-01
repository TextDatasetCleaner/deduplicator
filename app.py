from flask import Flask, request, render_template
from deduplicator import Deduplicator

app = Flask(__name__)

duplicator = Deduplicator()

def showDedupl(string):
        global duplicator
        result = duplicator.isDuplicate(string)
        return result

@app.route('/')
def my_form():
        return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form__post():
        text = request.form['u']
        return render_template('index2.html', res=str(showDedupl(text)))

if __name__ == '__main__':
        app.run()
