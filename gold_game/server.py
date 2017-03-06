import random
from flask import Flask,render_template,request,redirect,session  # Import Flask to allow us to create our app.
app = Flask(__name__)   
app.secret_key = 'ThisIsSecret' 

@app.route('/')
def hello_world():
	return render_template('index.html',)


@app.route('/process_money',methods=['POST'])
def form():
	random_farm=random.randrange(10, 20)
	random_cave=random.randrange(5, 10)
	random_house=random.randrange(2, 5)
	random_casino=random.randrange(-50, 50)
	if request.form['action'] == 'farm': 
		session['coins']+=random_farm
		session['activity']=session['activity'],'You earned',str(random_farm)
	elif request.form['action'] == 'cave': 
		session['coins']+=random_cave
		session['activity']=session['activity'],'You earned',str(random_cave)
	elif request.form['action'] == 'house': 
		session['coins']+=random_house
		session['activity']=session['activity'],'You earned',str(random_house)
	else:
		session['coins']+=random.randrange(-50, 50)
		session['activity']=session['activity'],'You earned',str(random_casino)
	
	return redirect('/')

app.run(debug=True) 