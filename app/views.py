from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
  user = {'nickname': 'Phil'}
  posts = [
    {
      'author': {'nickname': 'John'},
      'body': 'It\'s nice out here today.'
    },
    {
      'author': {'nickname': 'Richard'},
      'body': 'It\'s indeed a nice day, sir.'
    }
  ]




  return render_template('index.html',
                          title="Home",
                          user=user,
                          posts=posts)
