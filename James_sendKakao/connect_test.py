from flask import Flask, request, render_template, redirect, json
import requests


app = Flask("__name__", static_url_path='/static')


@app.route('/')
def indexk():           
    return render_template('NEW_Alimtalk_sendForm.html')



if __name__ == '__main__':
    app.run(port="5090", debug=True)

