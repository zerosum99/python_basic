from flask import Flask,request, render_template

app = Flask(__name__)
@app.route('/login',methods=['GET','POST'])
def login():
    #GETreques'
    if request.method=='GET':
        return render_template('login_1.html')
    #POSTREQUEST
    else:
        email=request.form['email']
        password=request.form['password']
        #Checkemail&password
        #TODO
        return " email" + email + " password "+ str(password)

if __name__ == '__main__' :
    app.run(debug=True)