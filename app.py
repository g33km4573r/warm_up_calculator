import os
from collections import Counter
from flask import Flask, render_template, request
from flask.ext.wtf import Form
from flask_wtf.html5 import NumberInput
from wtforms import StringField
from wtforms.validators import Required
from flask.ext.bootstrap import Bootstrap

from which_plates.main import which_plates


app = Flask(__name__)
Bootstrap(app)
app.secret_key = os.environ.get("SECRET_KEY")

class PlatesForm(Form):
    plates = StringField("plates", validators=[Required()])
    goal = StringField("goal", validators=[Required()])


@app.route("/", methods=["GET", "POST"])
def index():
    warm_up = None
    if request.method == "POST":
        warm_up = which_plates(
            float(request.form['goal']),
            Counter([float(p) for p in request.form['plates'].split(',')]),
            [.20, .40, .60, .80, 1]
        )
        warm_up = [plates for action, plates in warm_up if action=="l"]

    return render_template("index.html", form=PlatesForm(), warm_up=warm_up) 

if __name__ == '__main__':
    app.run(debug=True)
