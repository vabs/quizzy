from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio, connected_players


@socketio.on('joined', namespace='/play')
def joined():
    join_room('quizzy')
    emit('status', {'msg': session.get('name') + ' has joined the game.'}, room='quizzy')


@socketio.on('/status', namespace='/play')
def players():
	emit('players', { 'players': connected_players })