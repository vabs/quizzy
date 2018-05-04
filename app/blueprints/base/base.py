from flask import Blueprint, render_template, session, request, redirect, url_for
from ..forms.login import LoginForm
from app import connected_players
from ..score import calculate_score

base = Blueprint('base', __name__, template_folder='../../templates/base')


@base.route('/', methods=['GET', 'POST'])
def index():
	form = LoginForm()
	if form.validate_on_submit():
		session['name'] = form.name.data
		session['room'] = 'birthday'
		if session['name'] not in connected_players.keys():
			connected_players[session['name']] = 0
		return redirect(url_for('.play'))
	elif request.method == 'GET':
		form.name.data = session.get('name', '')
	return render_template('index.html', form=form)


@base.route('/play', methods=['GET'])
def play():
	return 'Ready to play!'


@base.route('/answer', methods=['POST'])
def answer():
    """To capture responses from users and calculate score.
    """
    print(request.form)
    ans = json.loads(request.form.keys()[0])
    old_score = 0
    if session['name'] in connected_players.keys():
            old_score = connected_players[session['name']]

    if 'test' in ans["ans"][0]:
        return 'test answer'
    else:
        timed = int(float(ans["ans"][2]))
        score = calculate_score(ans["ans"][0], ans["ans"][1], old_score, timed)
        connected_players[session['name']] = score
        socketio.emit('scores', 
                    {
                        'msg': 'score are updated',
                        'connected_players': connected_players
                    }, 
                    namespace='/score')
    return "success"
