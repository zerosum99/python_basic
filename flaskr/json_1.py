
#!flask/bin/python
from flask import Flask,jsonify
app=Flask(__name__)
tasks= [
{
'id':1,
'title':u'Buygroceries',
'description':u'Milk,Cheese,Pizza,Fruit,Tylenol',
'done': False
},
{
'id':2,
'title':u'LearnPython',
'description':u'Needto findagoodPythontutorial ontheweb',
'done': False
}
]
@app.route('/json', methods=['GET'])
def get_tasks():
    return  jsonify( tasks)

if __name__ == '__main__' :
    app.run(debug=True)