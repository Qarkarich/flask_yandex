from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
@app.route('/index/<title>')
def index(title='Миссия колонизации Марса!'):
    style_path = url_for('static', filename='css/style.css')
    return render_template('base.html', title=title, style_path=style_path)


@app.route('/training/<prof>')
def prof_map(prof):
    return render_template()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')