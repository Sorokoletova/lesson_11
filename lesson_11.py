from flask import Flask, render_template
from function_11 import get_candidates_list, get_candidates_by_id, get_candidates_skill, get_candidates_by_name
app = Flask(__name__)


@app.route('/',)
def page_all():
     candidates = get_candidates_list()
     return render_template("list.html", candidates=candidates)


@app.route('/candidate/<int:number_id>')
def page_number_id(number_id):
    candidates = get_candidates_by_id(number_id)

    return render_template("single.html", candidates=candidates)


@app.route('/skill/<skill>')
def page_skill(skill):
    candidates = get_candidates_skill(skill)

    return render_template("skill.html", candidates=candidates)


@app.route('/search/<candidate_name>')
def page_search(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates)


app.run()
