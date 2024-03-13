from flask import Flask, request, render_template
from main import take_in_log
from db import init_db, get_problems
from leetcode_journal.model import problem

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('static/index.html')

@app.route('/log', methods=['POST'])
def new_problem():
    url = request.form['problem_url']
    data = take_in_log(url)
    new_problem(data)
    return {"message": "Success"}

@app.route('/problems', methods=['GET'])
def get_problems():
    problems = get_problems()
    return {"problems": problems}

if __name__ == '__main__':
    init_db()
    app.run(debug=True)