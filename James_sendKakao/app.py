from flask import Flask, request, render_template, redirect, json
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
from tkinter import messagebox
import requests
import Alimtalk
import Chingutalk

from get_token import genToken


app = Flask("__name__", static_url_path='/static')

app.register_blueprint(Alimtalk.bp)
app.register_blueprint(Chingutalk.bp)


@app.route("/")
def starter():
    return "Hello"


if __name__ == '__main__':
    app.run(port="5070", debug=True)