from flask import Flask, render_template
from flask import url_for
from forms import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = ''


@app.route('/')
@app.route('/home')
def home():  # put application's code here
    return render_template('home.html')


@app.route('/projects')
def projects():
    pass


@app.route('/about')
def about():
    pass


@app.route('/contact_me', methods=['GET', 'POST'])
def contact_me():
    form = ContactForm()
    if form.validate_on_submit():
        pass
    return render_template('contact_me.html', form=form)


@app.route('/cv')
def cv():
    pass


if __name__ == '__main__':
    app.run(debug=True)
