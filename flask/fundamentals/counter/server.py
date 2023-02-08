from flask import Flask, render_template,session, request, redirect
app = Flask(__name__)
app.secret_key = 'keep it secret to keep it safe'
@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
