from flask import Flask, request, render_template, Response
from main import take_in_log
from db import init_db, get_problems, add_new

app = Flask(__name__, template_folder="static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log', methods=['POST'])
def new_problem():
    url = request.form['problem_url']
    data = take_in_log(url)
    add_new(data)
    
    response = Response(status=204)
    response.headers['HX-Refresh'] = 'true'
    return response
    
@app.route('/problems/', methods=['GET'])
def problems():
    page = int(request.args.get('page', 1))
    per_page = 10

    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    problems = get_problems()
    paginated_problems = problems[start_index:end_index]
    
    return render_template('table.html', data=paginated_problems, page=page)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)