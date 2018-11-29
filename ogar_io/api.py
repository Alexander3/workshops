from multiprocessing import Queue
from random import randint

import flask
from flask import Flask, request

app = Flask(__name__)
queue = Queue()


@app.route('/down')
@app.route('/up')
@app.route('/left')
@app.route('/right')
def move():
    command = request.path.strip('/')
    user = request.cookies.get('user')
    if not user:
        user = str(randint(0, 10 * 5))
    queue.put((command, user))

    res = flask.make_response()
    res.set_cookie('user', user)
    return res
