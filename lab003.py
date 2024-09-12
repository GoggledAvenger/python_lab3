# Lab3 from https://github.com/THartmanOfTheRedwoods/PyLab003/tree/master

def get_username():
    username = input("Enter username.").strip().upper()
    return username

def get_group():
    group = input("Enter Chat Group name.").strip().upper()
    return group

def get_message():
    message = input("Enter message:").strip().upper()
    return message

import lab_chat as lc

def initialize_chat():
    user = get_username()
    group = get_group()
    node = lc.get_peer_node(user)
    return lc.get_channel(node, group)

def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")

start_chat()