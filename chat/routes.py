from flask import Blueprint
from flask import render_template, jsonify, request

from db import db
from models import Message
from pusher_preperation import channels_client

main = Blueprint('chat', __name__)


@main.route('/')
def index():
    messages = Message.query.all()
    return render_template('layout.html', messages=messages)


@main.route('/message', methods=['POST'])
def message():
    try:

        username = request.form.get('username')
        message = request.form.get('message')
        new_message = Message(username=username, message=message)
        db.session.add(new_message)
        db.session.commit()

        channels_client.trigger('chat-channel', 'new-message', {'username': username, 'message': message})

        return jsonify({'result': 'success'})

    except:

        return jsonify({'result': 'failure'})
