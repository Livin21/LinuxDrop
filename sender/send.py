from __future__ import print_function

from os import getcwd
import logging

from flask import Flask, send_from_directory, request

app = Flask(__name__, static_url_path='')

f_name = ''


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route('/')
def get_file():
    return send_from_directory(getcwd(), f_name)


@app.route('/end')
def end_transmission():
    print ("File is being transmitted through space...")
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    print ("Confirmation from alien planet: File Received...")
    print ("Falling back to earth...")
    print ("Shutting down thrusters...")
    print ("Bye!")
    return "Shutting down scanner. Bye!"


@app.route('/name')
def get_file_name():
    print ("Beaming file details to alien planet")
    return f_name


def start_server(file_name):
    print ("Starting thrusters...")
    print ("Launching " + file_name + " to outer space...")
    global f_name
    f_name = file_name
    app.run("0.0.0.0", "1921")
