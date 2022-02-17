from flask import Flask, render_template, url_for

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
