from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    team_leader_id = IntegerField('Job leader', validators=[DataRequired()])
    job = StringField('Job title', validators=[DataRequired()])
    work_size = IntegerField('Work size', validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    is_finished = BooleanField('Is work finished?')
    submit = SubmitField('Submit')
