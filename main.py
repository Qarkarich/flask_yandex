from flask import Flask
from data import db_sessions
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

users = [
    {'surname': 'Scott',
     'name': 'Ridley',
     'age': 21,
     'position': 'captain',
     'speciality': 'research engineer',
     'address': 'module_1',
     'email': 'scott_chief@mars.org'},
    {'surname': 'Mark',
     'name': 'Watney',
     'age': 141,
     'position': 'crew member',
     'speciality': 'biologist',
     'address': 'module_1',
     'email': 'mars_survivor@mars.org'},
    {'surname': 'Dominic',
     'name': 'Torreto',
     'age': 15,
     'position': 'family member',
     'speciality': 'racer',
     'address': 'module_718',
     'email': 'taxi_driver123@mars.org'},
    {'surname': 'Sid',
     'name': 'Ryley',
     'age': 32,
     'position': 'crew member',
     'speciality': 'unknown',
     'address': 'module_3',
     'email': 'boring_person15@mars.org'}
]

jobs = [
    {'team_leader': 1,
     'job': 'deployment of residential modules 1 and 2',
     'work_size': 15,
     'collaborators': '2, 3',
     'is_finished': False
     }
]


def main():
    db_sessions.global_init("db/mars_explorer.db")
    db_sess = db_sessions.create_session()

    for member in users:
        user = User()
        user.surname = member['surname']
        user.name = member['name']
        user.age = member['age']
        user.position = member['position']
        user.speciality = member['speciality']
        user.address = member['address']
        user.email = member['email']

        db_sess.add(user)
        db_sess.commit()

    for obj in jobs:
        job = Jobs()
        job.team_leader = obj['team_leader']
        job.job = obj['job']
        job.work_size = obj['work_size']
        job.collaborators = obj['collaborators']
        job.is_finished = obj['is_finished']

        db_sess.add(job)
        db_sess.commit()

    app.run()


if __name__ == '__main__':
    main()
