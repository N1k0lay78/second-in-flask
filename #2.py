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


@app.route('/answer/')
@app.route('/auto_answer/')
def anketa_answer():
    user = {}
    user['surname'] = input('Фамилия')
    user['name'] = input('Имя')
    user['education'] = input("Образование")
    user['profession'] = input("Професия")
    user['sex'] = input("Пол")
    user['motivation'] = input("Мотивация")
    user['ready'] = input("Готовы ли вы остаться на марсе?")
    title = 'Анкета'
    return render_template('auto_answer.html', user=user, style=url_for('static', filename='css/style.css'), title=title)


if __name__ == '__main__':
    print('http://127.0.0.1:8080/auto_answer/')
    app.run(port=8080, host='127.0.0.1')
