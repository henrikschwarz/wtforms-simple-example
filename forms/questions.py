from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired

class QuestionsForm(FlaskForm):
    class Meta:
        csrf = False
    # Example of defining a field. A in depth description can be found.
    # field_name = FieldType(label, description="some description", validators=[])
    question1 = StringField("Question 1", description="This is the form description for question number 1", validators=[DataRequired()])
    question2 = StringField("q2", validators=[DataRequired()])
    question3 = StringField("q3", validators=[DataRequired()])
    question4 = StringField("q4", validators=[DataRequired()])
    question5 = StringField("q5", validators=[DataRequired()])
    question6 = StringField("q6", validators=[DataRequired()])
    question7 = StringField("q7", validators=[DataRequired()])