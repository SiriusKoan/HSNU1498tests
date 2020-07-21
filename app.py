from flask import Flask, render_template, request
from models import *
import datetime
#import config

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    year = int(datetime.datetime.now().strftime('%Y'))
    month = int(datetime.datetime.now().strftime('%m'))
    cal = make_calendar(year, month)
    return cal

if __name__ == '__main__':
    app.run(port = 8080, debug = True)