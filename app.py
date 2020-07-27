from flask import Flask, render_template, request, redirect
from models import *
import datetime
import config

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        year = int(datetime.datetime.now().strftime("%Y"))
        month = int(datetime.datetime.now().strftime("%m"))
        cal = make_calendar(year, month, config.subject_colors)
        colors = config.subject_colors
        return render_template("index.html", test_table=cal, colors=colors)
    if request.method == "POST":
        time = request.form.get("time")
        if time:
            time = time.split("-")
            year = int(time[0])
            month = int(time[1])
            cal = make_calendar(year, month, config.subject_colors)
            colors = config.subject_colors
            return render_template("index.html", test_table=cal, colors=colors)
        return "Error", 400


@app.route("/admin", methods=["GET", "POST"])
def admin_page():
    if request.method == "GET":
        return render_template("admin.html")
    if request.method == "POST":
        time = request.form.get("time")
        subject = request.form.get("subject")
        content = request.form.get("content")
        pin = request.form.get("pin")
        if pin == config.PIN:
            if time and subject and content:
                add_test(time, subject, content)
                return redirect("/")
            return "Error", 400
        return 'Verify fail.<br><img src="https://http.cat/401"></img>', 401


@app.route("/api", methods=["POST"])
def api_page():
    try:
        payload = request.get_json()
        time = payload["time"]
        subject = payload["subject"]
        content = payload["content"]
        pin = payload["pin"]
        if pin == config.PIN:
            add_test(time, subject, content)
            return 200
        return "Verify fail", 401
    except:
        return "Error", 400


if __name__ == "__main__":
    app.run(port=8080, debug=True)
