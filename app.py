import os
from collections import Counter
from flask import Flask, render_template, request, redirect
from flask.ext.wtf import Form
from flask_wtf.html5 import NumberInput
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.bootstrap import Bootstrap

from which_plates.main import which_plates


app = Flask(__name__)
Bootstrap(app)
app.secret_key = os.environ.get("SECRET_KEY")

class PlatesForm(Form):
    plates = StringField("plates", default="55,45,44,35,33,25,22,10,5,2.5", validators=[Required()])
    goal = StringField("goal", default="225", validators=[Required()])
    bar = StringField("bar", default="45", validators=[Required()])
    submit = SubmitField('Submit')


@app.route("/", methods=["GET", "POST"])
def index():
    warm_up = None
    if request.method == "POST":

        warm_up = which_plates(
            (float(request.form['goal'])- float(request.form['bar']))/2 ,
            Counter([float(p) for p in request.form['plates'].split(',')]),
            [.20, .40, .60, .80, 1]
        )
        warm_up = [(plates, sum(plates)) for action, plates in warm_up if action=="l"]
    return render_template("index.html", form=PlatesForm(), warm_up=warm_up) 

if __name__ == '__main__':
    PORT = int(os.environ.get("PORT", 5000))
    DEBUG = bool(os.environ.get("DEBUG", False))
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
