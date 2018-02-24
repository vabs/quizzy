from flask import Blueprint, render_template

base = Blueprint('base', __name__, template_folder='../../templates/base')

@base.route('/', methods=['GET'])
def index():
	return render_template('index.html')