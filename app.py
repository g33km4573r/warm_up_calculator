import os
from collections import Counter
from flask import Flask, render_template, request, redirect
from flask.ext.wtf import Form
from flask_wtf.html5 import NumberInput
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.bootstrap import Bootstrap

from which_plates.which_plates.main import which_plates


app = Flask(__name__)
Bootstrap(app)
app.secret_key = os.environ.get("SECRET_KEY")

class PlatesForm(Form):
    plates = StringField("plates", default="45,35,25,15,10,5", validators=[Required()])
    goal = StringField("goal", default="125", validators=[Required()])
    submit = SubmitField('Submit')


@app.route("/", methods=["GET", "POST"])
def index():
    warm_up = None
    if request.method == "POST":
        warm_up = which_plates(
            float(request.form['goal']),
            Counter([float(p) for p in request.form['plates'].split(',')]),
            [.20, .40, .60, .80, 1]
        )
        warm_up = [(plates, sum(plates)) for action, plates in warm_up if action=="l"]


    return render_template("index.html", form=PlatesForm(), warm_up=warm_up) 


if __name__ == '__main__':
    app.run(debug=True)
