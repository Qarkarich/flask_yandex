from flask import Flask, url_for

app = Flask(__name__)

planets = {
    'Марс': {
        'description': ['Эта планета близка к Земле;', 'На ней много необходимых ресурсов;',
                        'На ней есть вода и атмосфера;', 'На ней есть небольшое магнитное поле;',
                        'Наконец, она просто красива!']
    },
    'Меркурий': {
        'description': ['Это хорошее место чтобы любоваться солнцем;',
                        'Там можно организовать хороший курорт;',
                        'Можно добывать много энергии термогенераторами;',
                        'Просто хороший солярий;', 'Так себе идея...']
    },
    'Юпитер': {
        'description': ['Там просторно;', 'Можно поставить ветрогенераторы;',
                        'Можно летать в газе;', 'Красивые штормы;', 'В целом, не очень идея...']
    },
    'Сатурн': {
        'description': ['Красивые кольца;', 'Много гелия, разговариваешь смешным голосом;',
                        'Можно сделать летающий город;', 'Красиво;', 'Милое место;']
    }
}


@app.route('/choice/<planet_name>')
def describe_planet(planet_name):
    if planet_name in planets:
        description = planets[planet_name]['description']
        return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}</h1>
                    <h2>{description[0]}</h2>
                    <div class="alert alert-primary" role="alert">
                        {description[1]}
                    </div>
                    <div class="alert alert-secondary" role="alert">
                        {description[2]}
                    </div>
                    <div class="alert alert-success" role="alert">
                        {description[3]}
                    </div>
                    <div class="alert alert-danger" role="alert">
                        {description[4]}
                    </div>
                  </body>
                </html>'''
    else:
        return f'''<h1>Такой вариант не предусмотрен.</h1>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')