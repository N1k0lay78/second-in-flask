from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/<title>')
def index(title):
    return render_template('base.html', style=url_for('static', filename='css/style.css'), title=title)


@app.route('/treaning/<specialist>')
def trening(specialist):
    if 'инженер' in specialist or 'строитель' in specialist:
        file = 'inginer'
    else:
        file = 'gumunit'
    return render_template('tren.html', filename=url_for('static', filename=f'image/{file}.png'),
                           style=url_for('static', filename='css/style.css'), title="Тренировка")


@app.route('/list_prof/<type>')
def list_prof(type):
    profs = ['инженер', 'пилот', 'строитель', 'врач', 'климатолог', 'астогеолог', 'гляциолог', 'метеоролог',
             'киберинженер', 'штурман']
    return render_template('list-prof.html', type=type, style=url_for('static', filename='css/style.css'),
                           title="Cписок профессий", profs=profs)


if __name__ == '__main__':
    print('http://127.0.0.1:8080/list_prof/ul')
    app.run(port=8080, host='127.0.0.1')
