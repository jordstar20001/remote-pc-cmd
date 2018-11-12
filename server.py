# Jordan Zdimirovic (C)

from flask import Flask, request, make_response

import os

server = Flask(__name__)

@server.route("/taskkill", methods=["POST"])
def taskkill():
    data = request.get_json()
    forceMode = data['forceMode']
    repeats = data['repeats']
    delay = data['delay']
    task = data['task']

    for i in range(repeats):
        if forceMode:
            os.system("taskkill /im " + task + ".exe /f")

        else:
            os.system("taskkill /im " + task + ".exe")

    return make_response(), 200

server.run("0.0.0.0", 31415, debug=True)
