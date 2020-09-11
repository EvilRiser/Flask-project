from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
# __name__ is equivalent to __main__ in normal python

# To increses sec and prevent cookie changes
app.config['SECRET_KEY'] = 'be3412f8c73cfe0ee86bc5fbef1094c4'

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

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
    	flash(f'Account created for {form.username.data}!','success')
    	return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title='Login',form=form)

if __name__ == '__main__':
    app.run(debug=True)