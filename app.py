from flask import Flask, request, render_template
from main import take_in_log
from db import init_db, get_problems, add_new
from model import problem

app = Flask(__name__, template_folder="static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log', methods=['POST'])
def new_problem():
    url = request.form['problem_url']
    data = take_in_log(url)
    add_new(data)
    problems = get_problems()
    return render_template('table.html', data=problems)
    
@app.route('/problems', methods=['GET'])
def get_problems():
    problems = get_problems()
    table_html = render_template('table.html', data=problems)
    return table_html

if __name__ == '__main__':
    init_db()
    app.run(debug=True)