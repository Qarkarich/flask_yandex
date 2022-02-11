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


@app.route('/promotion_image')
def promote_page():
    return f'''<!DOCTYPE html>
                <html>
                <head>
                    <title>Колонизация</title>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                </head>
                <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='images/mars.png')}" alt="Красная 
                    планета!" width="500"><br>
                    <span>Вот она какая, красная планета</span>
                    <ul style="list-style: none">
                                <li class="alert alert-primary" role="alert">Человечество 
                                вырастает из детства.</li>
                                <li class="alert alert-secondary" role="alert">Человечеству мала 
                                одна планета.</li>
                                <li class="alert alert-success" role="alert">Мы сделаем обитаемыми 
                                безжизненные пока планеты.</li>
                                <li class="alert alert-warning" role="alert">И начнем с Марса!</li>
                                <li class="alert alert-primary" role="alert">Присоединяйся!</li>
                    </ul>
                </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
