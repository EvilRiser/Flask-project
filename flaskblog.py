from flask import Flask, render_template, url_for
app = Flask(__name__)
# __name__ is equivalent to __main__ in normal python

#dummy data
posts=[
		{
			'author':'SS',
			'title':'Blog Post1',
			'content':'First Post content',
			'date_posted':'Sep 9, 2020'
		},
		{
			'author':'ER',
			'title':'Blog Post2',
			'content':'Second Post content',
			'date_posted':'Sep 9, 2020'
		}
	]


# this app.route is called decorator to 
#show the path of all the pages like / -> tells the home page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    # return '<h1>About Page </h1>'
    return render_template('about.html',title='About')

if __name__ == '__main__':
    app.run(debug=True)