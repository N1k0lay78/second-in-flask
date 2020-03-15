from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/<title>')
def index(title):
    return render_template('base.html', style=url_for('static', filename='css/style.css'), title=title)


if __name__ == '__main__':
    print('http://127.0.0.1:8080/index')
    app.run(port=8080, host='127.0.0.1')