from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astro_form():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Отбор астронавтов</title>
                              </head>
                              <body>
                                <div class="form-container">
                                    <h1>Анкета претендента</h1>
                                    <h3>на участие в миссии</h3>
                                    <form class="login_form" method="post" id="astro-form">
                                        <input type="text" class="form-control" placeholder="Введите имя" name="name">
                                        <input type="text" class="form-control" placeholder="Введите фамилию" name="second_name">
                                        <div class="form-group">
                                            <br>
                                            <input type="email" class="form-control" placeholder="Введите адрес электронной почты" name="email">
                                        </div>
                                         <div class="form-group">
                                                <label for="educationSelect">Какое у вас образование?</label>
                                                <select class="form-control" id="educationSelect" name="education">
                                                    <option>Общее</option>
                                                    <option>Высшее</option>
                                                </select>
                                        </div>
                                        <div class="form-group">
                                            <label for="form-check">Какие у Вас есть профессии?</label>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="labor" id="engineer_research" value="engineer_researcher" checked>
                                                <label class="form-check-label" for="engineer_research">
                                                    Инженер-исследователь
                                                </label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="labor" id="engineer_builder" value="engineer_builder">
                                                <label class="form-check-label" for="engineer_builder">
                                                    Инженер-строитель
                                                </label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="labor" id="pilot" value="pilot">
                                                <label class="form-check-label" for="pilot">
                                                    Пилот
                                                </label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="labor" id="exobiologist" value="exobiologist">
                                                <label class="form-check-label" for="exobiologist">
                                                    Экзобиолог
                                                </label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="labor" id="doctor" value="doctor">
                                                <label class="form-check-label" for="doctor">
                                                    Доктор
                                                </label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="labor" id="radiation_engineer" value="radiation_engineer">
                                                <label class="form-check-label" for="radiation_engineer">
                                                    Инженер по радиацонной защите
                                                </label>
                                            </div>                                                                                        
                                        </div>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                                <label class="form-check-label" for="male">
                                                    Мужской
                                                </label>
                                        </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                                <label class="form-check-label" for="female">
                                                    Женский
                                                </label>
                                            </div>
                                        </div>
                                        <div class="form-group">
                                            <label for="motivation">Почему Вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="motivation" name="motivation"></textarea>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                        </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        return f"Анкета отправлена!"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
