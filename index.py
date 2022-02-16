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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
