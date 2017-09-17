from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "SecretySecretSeccccccret"


@app.route('/')
def index():
    try:
        session['count'] += 1
    except:
        session['count'] = 1
    return render_template("index.html")

@app.route('/plus2')
def add2():
    session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)
