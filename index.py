from flask import Flask, render_template, url_for, redirect
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'marsirovka'


@app.route('/')
@app.route('/index/<title>')
def index(title='Миссия колонизации Марса!'):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def prof_map(prof):
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        heading = 'Инженерные тренажеры'
        filename = url_for('static', filename='img/2.png')
    else:
        heading = 'Научные симуляторы'
        filename = url_for('static', filename='img/1.png')

    return render_template('prof.html', prof_heading=heading, filename=filename)


@app.route('/list_prof/<list>')
def prof_list(list):
    professions = ['геолог', 'строитель', 'экзобиолог', 'инженер-биолог', 'экзобиолог',
                   'инженер ракетных двигателей', 'астрофизик']
    if list in ['ul', 'ol']:
        return render_template('prof_list.html', list_type=list, prof_list=professions)
    return render_template('error.html')


@app.route('/answer')
@app.route('/auto_answer')
def show_answer():
    values = [
        {'id': 'title',
         'data': {
             'display_data': ' ',
             'value': ''
         }},
        {'id': 'surname',
         'data': {
             'display_data': 'Фамилия',
             'value': 'Watny'
         }},
        {'id': 'name',
         'data': {
             'display_data': 'Имя',
             'value': 'Mark'
         }},
        {'id': 'education',
         'data': {
             'display_data': 'Образование',
             'value': 'Выше среднего'
         }},
        {'id': 'profession',
         'data': {
             'display_data': 'Профессия',
             'value': 'штурман марсохода'
         }},
        {'id': 'sex',
         'data': {
             'display_data': 'Пол',
             'value': 'male'
         }},
        {'id': 'motivation',
         'data': {
             'display_data': 'Мотивация',
             'value': 'Всегда мечтал застрять на Марсе!'
         }},
        {'id': 'ready',
         'data': {
             'display_data': 'Готовы остаться на Марсе?',
             'value': True
         }}]

    return render_template('auto_answer.html', data=values)


@app.route('/login', methods=['GET', 'POST'])
def login_form():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', form=form,
                           logo_path=url_for('static', filename='img/MARS-2-7.png'))


@app.route('/distribution')
def show_cabins():
    members = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    return render_template('cabins.html', names=members)


@app.route('/table/<sex>/<age>')
def show_table(sex, age):
    if int(age) >= 21:
        img = url_for('static', filename='img/adult.jpg')
        if sex == 'male':
            color = '#342d71'
        elif sex == 'female':
            color = '#ff9478'
    elif int(age) < 21:
        img = url_for('static', filename='img/child.png')
        if sex == 'male':
            color = '#2d55ff'
        elif sex == 'female':
            color = '#ff4c30'

    return render_template('table.html', img=img, wall_color=color)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
