from flask import Flask, render_template, request, redirect
from models import *
import datetime
import config

app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == 'GET':
        year = int(datetime.datetime.now().strftime("%Y"))
        month = int(datetime.datetime.now().strftime("%m"))
    if request.method == 'POST':
        time = request.form.get('time').split('-')
        year = int(time[0])
        month = int(time[1])
    cal = make_calendar(year, month, config.subject_colors)
    colors = "<div>" + "<br>".join([c + " - " + config.subject_colors[c] for c in config.subject_colors]) + "</div>"
    return render_template('index.html', test_table = cal, colors = colors)



@app.route('/admin', methods = ['GET', 'POST'])
def admin_page():
    if request.method == 'GET':
        return render_template('admin.html')
    if request.method == 'POST':
        time = request.form.get('time')
        subject = request.form.get('subject')
        content = request.form.get('content')
        pin = request.form.get('pin')
        if pin == config.PIN:
            add_test(time, subject, content)
            return redirect('/')
        return 'Verify fail.'


if __name__ == "__main__":
    app.run(port=8080, debug=True)
