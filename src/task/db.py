"""
This is a module bbz
"""
import json

def read_db(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def next_id(db):
    if db:
        return int(max(db.keys())) + 1
    else:
        return 1

def write_db(data, path):
    with open(path, "w") as f:
        json.dump(data, f)
