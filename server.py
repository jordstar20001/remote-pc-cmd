# Jordan Zdimirovic (C)

from flask import Flask, request, make_response, jsonify

import os

import time

server = Flask(__name__)

@server.route("/taskkill", methods=["POST"])
def taskkill():
    data = request.get_json()
    forceMode = data['forceMode']
    repeats = data['repeats']
    delay = data['delay']
    task = data['task']

    termination_code = None

    for i in range(repeats):
        if forceMode:
            termination_code = os.system("taskkill /im " + task + " /f")

        else:
            termination_code = os.system("taskkill /im " + task)

        if termination_code != 0:
            return make_response(), 500
        time.sleep(delay / 1000)


    return make_response(), 200

@server.route("/tasklist", methods=["GET"])
def tasklist():
    process = os.popen("tasklist")
    output = process.read()
    process.close()
    out_split = output.split("\n")
    resp_data = {"tasks":[]}
    for line in out_split:
        curr_task = line.split(" ")[0]
        if curr_task not in resp_data['tasks']:
            if "exe" in curr_task or "msi" in curr_task:
                resp_data['tasks'].append(curr_task)



    return make_response(jsonify(resp_data)), 200




server.run("0.0.0.0", 31415, debug=True)
