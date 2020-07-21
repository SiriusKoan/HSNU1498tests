from flask import Flask, render_template, request
from models import *
import datetime
#import config

app = Flask(__name__)

subject_colors = {'English': 'red', 'Math': 'green', 'Chinese': 'red', 'Physics': 'blue', 'Chemical': 'lightblue', 'EarthScience': 'brown', 'Biology': 'green'}

@app.route('/', methods = ['GET'])
def index():
    year = int(datetime.datetime.now().strftime('%Y'))
    month = int(datetime.datetime.now().strftime('%m'))
    cal = make_calendar(year, month, subject_colors)
    colors = '<br>'.join([c + ' - ' + subject_colors[c] for c in subject_colors])
    return cal + '<hr>' + colors

if __name__ == '__main__':
    app.run(port = 8080, debug = True)