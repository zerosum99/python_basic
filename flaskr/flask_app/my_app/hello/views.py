
from my_app import app
from my_app.hello.models import MESSAGES
@app.route('/')
@app.route('/hello')
def hello_world():
    return MESSAGES['default']

@app.route('/show/<key>')
def get_message(key):
    if key == "all" :
        result= ""
        for k,v in MESSAGES.items() :
            result += "key: "+k + 'value :'+v
        return result
    else :
        return MESSAGES.get(key) or "%s not found!" % key

@app.route('/add/<key>/<message>')
def add_or_update_message(key, message):
    MESSAGES[key] = message
    return "%s Added/Updated" % key
