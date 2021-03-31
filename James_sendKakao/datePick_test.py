from flask import Flask, request, render_template, redirect, json
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
from datetime import timedelta
from datetime import datetime
from tkinter import messagebox
import requests

from get_token import genToken


app = Flask("__name__", static_url_path='/static')

@app.route("/")
def starter():
    return "Hello"


#================================================= Alim talk =============================================================
from Alimtalk_checkList import getTemplateMessage


@app.route('/alimtalk')
def index_alimtalk():
        
    return render_template('calendaer_test.html')



@app.route('/sendAlimtalk', methods = ['POST'])
def sendMessage1():
        
    date = request.form["date"]
    time = request.form["time"]

    send_year = str(request.form["date"][:4])
    send_mon = str(request.form["date"][5:7])
    send_date = str(request.form["date"][8:10])

    send_hour = str(request.form['time'][:2])
    send_min = str(request.form['time'][3:6])
    send_sec = "00"
    

    return  send_hour+send_min+send_sec


if __name__ == '__main__':
    app.run(port="5000", debug=True)

   

