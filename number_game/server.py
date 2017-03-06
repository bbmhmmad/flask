from flask import Flask, render_template, request, redirect
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 
# our index route will handle rendering our form
@app.route('/')
def index():
	session={}
	if 'number' in session:
		pass
	else:
		session['number']=random.randrange(0, 101)
	print session['number']
	return render_template("index.html")
@app.route('/guess', methods=["POST"])
def handle_guess():
	session['guess']=request.form['guess']
	last_guess=session['guess']
	print last_guess
	return redirect ('/')

app.run(debug=True)
