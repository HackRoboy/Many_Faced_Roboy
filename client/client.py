import json, requests

SERVERURL = "http://localhost:5000"


def send_updates(updates):
    r = requests.post(SERVERURL + "/sendUpdates", json={"ok": True, "updates":updates})


def make_update(utype, data):
    return {"type":utype, "data":data}

if __name__ == '__main__':
    send_updates([make_update("ball", {"x":5, "y":5, "z":5})])
