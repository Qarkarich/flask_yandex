from flask import Flask
from data import db_sessions


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_sessions.global_init("db/mars_explorer.db")
    app.run()


if __name__ == '__main__':
    main()