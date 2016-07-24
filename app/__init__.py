from flask import Flask

app = Flask(__name__)
# use the config file
app.config.from_object('config')
from app import views
