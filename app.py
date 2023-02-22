from flask import Flask, render_template, redirect, url_for, request, session
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'fbpp'
)

@app.route('/')
def index():
    return 'Hello world!'

if __name__ == '__main__':
    app.run(debug=True)