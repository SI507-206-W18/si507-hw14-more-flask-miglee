import json
from datetime import datetime


GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id = 0

def init():
    global entries
    global next_id
    try:

        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
        id_list = []
        for a in entries:
            is_list.append(a['id'])
        max_id = 0
        for a in is_list:
            if a > max_id:
                max_id=a
        next_id = max_id+1


    except:
        print('Couldn\'t open', GUESTBOOK_ENTRIES_FILE)
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text,):
    global entries, GUESTBOOK_ENTRIES_FILE,next_id
    now = datetime.now()
    time_string = now.strftime("%Y-%m-%d %H:%M:%S")
    entry = {"author": name, "text": text, "timestamp": time_string, "id": str(next_id)}
    next_id +=1
    entries.insert(0, entry) ## add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")


def delete_entry(id_):
    global entries, GUESTBOOK_ENTRIES_FILE
    for entry in entries:
###==
        if entry['id'] == id_:
                del entry['id']

    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

