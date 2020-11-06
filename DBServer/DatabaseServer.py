from flask import Flask, jsonify, request
import json
import sqlite3

from Database import Database

app = Flask(__name__)
app.config.from_pyfile("config.py")
db = Database()


@app.route('/get_list', methods=['POST'])
def get_list():
    if request.method == 'POST':
        number = int(request.form['number'])
        res = db.get_list(number)
        return jsonify({'problem_list': res})


@app.route("/save_list", methods=['POST'])
def save_list():
    if request.method == 'POST':
        lst = json.loads(request.form['lst'])
        db.save_list(lst)
        return jsonify({'flag': 1})


@app.route("/get_problem", methods=['POST'])
def get_problem():
    if request.method == 'POST':
        oj = request.form['oj']
        problemid = request.form['problemid']
        problem = db.get_problem(oj, problemid)
        return jsonify({'problem': problem})


@app.route("/save_problem", methods=['POST'])
def save_problem():
    if request.method == 'POST':
        problem = json.loads(request.form['problem'])
        db.save_problem(problem)
        return jsonify({'flag': 1})


@app.route('/get_title', methods=['POST'])
def get_title():
    if request.method == 'POST':
        oj = request.form['oj']
        problemid = request.form['problemid']
        res = db.get_title(oj, problemid)
        return jsonify({'title': res})


@app.route('/reset', methods=['POST'])
def reset():
    con = sqlite3.connect('Data.db')
    cur = con.cursor()
    try:
        cur.execute('DROP * FROM TABLE XOJ')
    except:
        print("reset eroor")
    con.commit()
    con.close()
    return jsonify({'flag': 1})

app.run(host='0.0.0.0', port=5000)
