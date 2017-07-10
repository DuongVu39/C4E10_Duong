import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds151222.mlab.com:51222/us_music

host = "ds151222.mlab.com"
port = 51222
db_name = "us_music"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())