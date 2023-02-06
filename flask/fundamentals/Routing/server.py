from flask import Flask, render_template
app = Flask(__name__) #name de l'application

@app.route('/')
def hello():
    return "Hello world"

@app.route('/say/<name>') #il va me trasmettre elli yetekteb ilkol felbarre url
def say_hi(name):
    return f"Hi {name} 👌👍🙌"


@app.route('/repeat/<name>/<int:times>') #ay7aja fi west il url yete9ra string 
def say_hi_times(name,times):
    return f"Hello {name} 👌👍🙌"*(times)

if __name__=='__main__':
    app.run(debug=True,port=5001) 
