from flask import Flask, render_template

app=Flask(__name__)


@app.route('/')
@app.route('/<name>')
def get_task(name=None):
    
    return  render_template('var.html', name=name)

if __name__ == '__main__' :
    app.run(debug=True)