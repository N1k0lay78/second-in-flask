import json
import os
from random import randrange

from flask import Flask, url_for, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class RullingForm(FlaskForm):
    id1 = StringField('ID пользователя', validators=[DataRequired()])
    pasw1 = PasswordField('Пароль пользователя', validators=[DataRequired()])
    id2 = StringField('ID пользователя', validators=[DataRequired()])
    pasw2 = PasswordField('Пароль пользователя', validators=[DataRequired()])
    submit = SubmitField('Зарегестрироваться')


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


def get_list_numbers(number):
    numbers = []
    for i in range(1, number + 1):
        numbers.append(i)
    return numbers


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


@app.route('/login/')
def login():
    form = RullingForm()
    return render_template('rulling.html', style=url_for('static', filename='css/style.css'), title='Управление', form=form, file=url_for('static', filename='image/MARS.png'))


@app.route('/distribution/')
def distribution():
    list = ['РИдли Скот', 'Энди Уир', 'Марк Уотни', 'Веката Капут', 'Тедди Сандерс', 'Шон Бин']
    return render_template('list-users.html', style=url_for('static', filename='css/style.css'), title='Участники', users=list)


@app.route('/table/<pol>/<int:age>')
def usre_caute(pol, age):
    image = 1
    if age >= 21:
        image += 1
        file = 'big_mars.png'
    else:
        file = 'big_mars.png'
    if pol == 'female':
        image += 2
    return render_template('caute.html', style=url_for('static', filename='css/style.css'), title='Участники', type=image, file=url_for('static', filename=f'image/{file}'), file2=url_for('static', filename=f'image/{image}.png'))


@app.route('/member/')
def user():
    i = randrange(3)
    with open('templates/users.json', 'r', encoding='utf-8') as fh:
        user = json.load(fh)['Users'][i]
    return render_template('about.html', style=url_for('static', filename='css/style.css'), title='Марсианин', user=user, file=url_for('static', filename=f'image/{user["image"]}'))


@app.route('/gallery', methods=['POST', 'GET'])
def carousel_2():
    if request.method == 'GET':
        number = 0
        while True:
            if not os.path.exists(f'static/image/mars_{number + 1}.jpg'):
                break
            else:
                number += 1
        return render_template('galery.html', numbers=get_list_numbers(number), help=0)
    if request.method == 'POST':
        f = request.files['file']
        number = 1
        while True:
            if not os.path.exists(f'static/image/mars_{number}.jpg'):
                with open(f'static/image/mars_{number}.jpg', 'wb') as file:
                    file.write(f.read())
                break
            else:
                number += 1
        return render_template('galery.html', numbers=get_list_numbers(number),
                               filename=url_for('static', filename=f'image/mars_{number}.jpg'), help=1)


if __name__ == '__main__':
    print('http://127.0.0.1:8080/gallery')
    app.run(port=8080, host='127.0.0.1')
