from flask import Flask, abort, jsonify,make_response

app=Flask(__name__)


@app.route('/abort', methods =['GET'])
def get_task():
    
    return  abort(404)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Notfound' }),404)

if __name__ == '__main__' :
    app.run(debug=True)