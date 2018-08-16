from flask import Flask, url_for, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template ('hello.html', name=name)


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    if isinstance(post_id, int):
        return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % subpath


@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/text/<string:my_shiny_string>')
def my_string(my_shiny_string):
    return 'String %s ' % my_shiny_string


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

