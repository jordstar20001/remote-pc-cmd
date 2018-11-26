import requests as r

import time

import os

def TaskKill(ip, port):
    task = input("Which task would you like to kill? (eg: winword.exe) : ")
    force = input("Would you like to turn force mode on? (Y)es or (N)o : ").lower()
    while True:
        if force == "y":
            force = True
            break

        elif force == "n":
            force = False
            break

        else:
            print("Invalid choice. Try again.")

    repeats = None

    while True:
        repeats = int(input("How many times would you like to repeat the taskkill? : "))
        if repeats < 1:
            print("Sorry, but you have to kill the task at least once.")

        else:
            break

    delay = 0

    if repeats > 1:
        while True:
            delay = int(input("How many milliseconds between each taskkill? : "))

            if delay < 0:
                print("Sorry, but delay must be a positive value OR 0")

            else:
                break

    data = {
        "task":task,
        "forceMode":force,
        "repeats":repeats,
        "delay":delay

    }

    resp = r.post("http://" + ip + ":" + port + "/taskkill", json=data)
    if resp.status_code == 200:
        print("Successfully killed task!")

    elif resp.status_code == 500:
        print("Error. Either the task was not found on the target machine, or you do not have permission to kill this task.")

def TaskList(ip, port):
    resp = r.get("http://" + ip + ":" + port + "/tasklist")
    if resp.status_code == 200:
        print("The tasks found on the machine are...")
        time.sleep(1)
        for task in resp.json()["tasks"]:
            print(task)
            time.sleep(0.08)

    else:
        print("Unknown error.")





ip = input("Please input IP of host you want to control : ")

port = input("Please input PORT of host you want to control : ")

while True:
    option = input("What would like to do? [TK] for taskkill, [TL] for tasklist, or [Q] to quit.")
    option = option.lower()
    if option == "tk":
        TaskKill(ip, port)

    elif option == "tl":
        TaskList(ip, port)

    elif option == "q":
        break

    else:
        print("Please select a valid input and try again.")
