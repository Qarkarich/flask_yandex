import datetime

import flask_login
from flask import Flask, render_template, redirect
from data import db_sessions
from data.users import User
from data.jobs import Jobs
from forms.user import RegisterForm, LoginForm
from forms.job import AddJobForm
from flask_login import login_user, LoginManager, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_sessions.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/register', methods=['GET', 'POST'])
def register_form():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_sessions.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            email=form.email.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_sessions.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@flask_login.login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/addjob', methods=['GET', 'POST'])
def add_job():
    form = AddJobForm()
    if form.validate_on_submit():
        db_sess = db_sessions.create_session()
        if db_sess.query(Jobs).filter(Jobs.job == form.job.data).first():
            return render_template("addjob.html", message="Job already exists", form=form,
                                   title="Adding a job")

        job_endtime = datetime.datetime.now()
        if not form.is_finished.data:
            job_endtime += datetime.timedelta(hours=form.work_size.data)
        job_id = 1
        if db_sess.query(Jobs).order_by(Jobs.id.desc()).first():
            job_id = db_sess.query(Jobs).order_by(Jobs.id.desc()).first().id + 1

        job = Jobs(
            id=job_id,
            team_leader=form.team_leader_id.data,
            job=form.job.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            is_finished=form.is_finished.data,
            end_date=job_endtime
        )

        db_sess.add(job)
        db_sess.commit()
        return redirect('/')

    return render_template('addjob.html', form=form, title="Adding a job")


@app.route('/')
def show_jobs_table():
    db_sess = db_sessions.create_session()
    data = db_sess.query(Jobs).all()

    for job in data:
        user = db_sess.query(User).filter(User.id == job.team_leader).first()
        if user:
            job.team_leader = f"{user.surname} {user.name}"
        else:
            job.team_leader = "Unknown"

    return render_template('job_table.html',
                           jobs=data)


def main():
    db_sessions.global_init("db/mars_explorer.db")
    login_manager.init_app(app)
    app.run(host='127.0.0.1', port='8080')


if __name__ == '__main__':
    main()
