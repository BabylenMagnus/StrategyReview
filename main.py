from flask import Flask, render_template
from config import Pages


app = Flask(__name__)


@app.route('/')
def index():
    return render_template(Pages.index)
