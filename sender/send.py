from __future__ import print_function

from flask import Flask, send_from_directory, request

app = Flask(__name__, static_url_path='')

f_name = ''


@app.route('/')
def get_file():
    return send_from_directory("../", f_name)


@app.route('/end')
def end_transmission():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return "Server shutting down..."


@app.route('/name')
def get_file_name():
    return f_name


def start_server(file_name):
    global f_name
    f_name = file_name
    app.run("0.0.0.0", "1921")
