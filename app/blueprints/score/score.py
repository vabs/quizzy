from flask import Blueprint, render_template

score = Blueprint('score', __name__, template_folder='../../templates/score')

@score.route('/score')
def index():
	return render_template('score.html')