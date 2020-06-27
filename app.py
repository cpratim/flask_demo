from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/hello')
def hello():
	return 'hello'

@app.route('/login', methods=["GET", 'POST'])
def login():
	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')

		return render_template('logged_in.html', username=username)
	return render_template('form.html')

@app.route('/user/<string:username>/<string:user2>')
def user(username, user2):
	return username + user

if __name__ == '__main__':
	app.run(debug=True)


#Get, POST
