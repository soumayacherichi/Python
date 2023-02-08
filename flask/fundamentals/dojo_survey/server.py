from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '1234567890'

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/process", methods=["post"])
def process():
    print (f"FORM from request=={request.form}")
    session['username'] = request.form['username']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect("/result")

@app.route("/result")
def result():
    return render_template("result.html") # bech n5arjouha fel display html

@app.route("/clear")
def clear_session():
    session.clear()
    return redirect("/")

if __name__ == '__main__':
    app.run (debug=True,port=5000)

