import os
from flask import Flask, render_template
from flask.ext.wtf import Form
from flask_wtf.html5 import NumberInput
from wtforms import StringField
from wtforms.validators import Required
from flask.ext.bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
app.secret_key = os.environ.get("SECRET_KEY")

class PlatesForm(Form):
    plates = StringField("plates", validators=[Required()])
    goal = StringField("goal", validators=[Required()])


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", form=PlatesForm()) 


if __name__ == '__main__':
    app.run(debug=True)
