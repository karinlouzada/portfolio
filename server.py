import csv
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
print(__name__)

# @app.route('/')
# def hello_world():
# 	return render_template('index.html')

@app.route('/index.html')
def index():
	return render_template('index.html') 

@app.route('/')
def home():
	return render_template('index.html') 

# @app.route('/about.html')
# def about():
# 	return render_template('about.html')

# @app.route('/works.html')
# def works():
# 	return render_template('works.html')

# @app.route('/contact.html')
# def contact():
# 	return render_template('contact.html')

# @app.route('/components.html')
# def components():
# 	return render_template('components.html')

@app.route('/<string:page_name>')
def page(page_name):
	if page_name in ['index','about','works', 'contact', 'components']:
		return render_template(page_name + '.html')
	elif page_name in ['index.html','about.html', 'works.html','contact.html','components.html','thankyou.html']:
		return render_template(page_name)
	else:
		return 'uh oh, no such page'

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv', newline='', mode='a') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database2, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try: 
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('/thankyou.html')
		except:
			return 'did not save to database'
	else:
		return 'error'