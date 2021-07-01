import requests
import json
import random
import string

janus_main_http = "http://207.246.118.54:8088/janus"
janus_admin_http = "http://207.246.118.54:7088/admin"

letters = string.ascii_lowercase
def get_rand_transaction():
    return ''.join(random.choice(letters) for i in range(10))

def start_session(janus_token=None):
    payload={
        "janus": "create",
        "transaction": get_rand_transaction()
    }
    if janu_token:
        payload["token"]=janu_token

    payload = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", f"{janus_main_http}", headers=headers, data=payload)

    return json.loads(response.text)

def attach_to_plugin(session_id,janus_token=None,plugin="janus.plugin.videoroom"):
    payload = json.dumps({
        "janus": "attach",
        "plugin": plugin,
        "transaction": get_rand_transaction(),
        "token": janus_token
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", f"{janus_main_http}/{session_id}", headers=headers, data=payload)

    return json.loads(response.text)

def list_rooms(session_id, handler_id, janus_token=None):
    payload={
        "janus": "message",
        "body" :{
                "request" : "list"
        },
        "transaction": get_rand_transaction()
    }
    if janu_token:
        payload["token"]=janus_token

    payload = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", f"{janus_main_http}/{session_id}/{handler_id}", headers=headers, data=payload)

    return json.loads(response.text)

def add_token(admin_secret, janus_token,plugins=["janus.plugin.videoroom"]):
    transaction = get_rand_transaction()
    if janus_token != "" and janus_token != None:
        payload={
            "janus" : "add_token",
            "token" : janus_token,
            "plugins": plugins,
            "transaction" :transaction,
            "admin_secret": admin_secret
        }

        payload = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", f"{janus_main_http}/{session_id}/{handler_id}", headers=headers, data=payload)

        return json.loads(response.text)
    else:
        response={
            "janus": "error",
            "transaction": transaction,
            "error": {
                "code": 500,
                "reason": "No token was given"
            }
        }
        return str(response)

def remove_token(admin_secret, janus_token):
    transaction = get_rand_transaction()
    if janus_token != "" and janus_token != None:
        payload={
            "janus" : "remove_token",
            "token" : janus_token,
            "transaction" :transaction,
            "admin_secret": admin_secret
        }

        payload = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", f"{janus_main_http}/{session_id}/{handler_id}", headers=headers, data=payload)

        return json.loads(response.text)
    else:
        response={
            "janus": "error",
            "transaction": transaction,
            "error": {
                "code": 500,
                "reason": "No token was given"
            }
        }
        return str(response)