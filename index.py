from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def default():
    return '''<!DOCTYPE html>
                <html>
                <head>
                    <title>Миссия колонизации марса!</title>
                </head>
                <body>
                </body>
                </html>'''


@app.route('/index')
def index():
    return '''<!DOCTYPE html>
                <html>
                <head>
                    <title>И на Марсе будут яблони цвести!</title>
                </head>
                <body>
                </body>
                </html>'''


@app.route('/promotion')
def promote_page():
    return '''<!DOCTYPE html>
                <html>
                <head>
                    <title>Реклама!</title>
                </head>
                <body>
                    <ul style="list-style: none">
                                <li>Человечество вырастает из детства.</li>
                                <li>Человечеству мала одна планета.</li>
                                <li>Мы сделаем обитаемыми безжизненные пока планеты.</li>
                                <li>И начнем с Марса!</li>
                                <li>Присоединяйся!</li>
                    </ul>
                </body>
                </html>'''


@app.route('/image_mars')
def show_mars():
    return f'''<!DOCTYPE html>
                <html>
                <head>
                    <title>Привет, Марс!</title>
                </head>
                <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='images/mars.png')}" alt="Красная 
                    планета!" width="500"><br>
                    <span>Вот она какая, красная планета</span>
                </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
