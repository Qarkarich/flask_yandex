from flask import Flask, render_template
from data import db_sessions
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def show_jobs_table():
    db_sess = db_sessions.create_session()
    data = db_sess.query(Jobs).all()

    for job in data:
        user = db_sess.query(User).filter(User.id == job.team_leader).first()
        job.team_leader = f"{user.surname} {user.name}"

    return render_template('job_table.html',
                           jobs=data)


def main():
    db_sessions.global_init("db/mars_explorer.db")

    app.run(host='127.0.0.1', port='8080')


if __name__ == '__main__':
    main()
