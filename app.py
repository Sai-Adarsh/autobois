#!/usr/bin/env python2
import flask
import pyautogui

# Creating application
APP = flask.Flask(__name__)


@APP.route('/')
def index():
    return flask.render_template('index.html')


@APP.route('/running', methods=['POST', 'GET'])
def run():
    print("I am running")
    pyautogui.moveTo(645, 0)
    result = "running"
    return flask.render_template("index.html", result = result)

if __name__ == "__main__":
    APP.debug = True
    APP.run()