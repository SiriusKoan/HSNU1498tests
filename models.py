import calendar
import sqlite3 as sql


class CustomHTMLCalendar(calendar.HTMLCalendar):
    def __init__(self, firstweekday, time, subject_colors):
        super(CustomHTMLCalendar, self).__init__()
        self.time = time
        self.subject_colors = subject_colors

    def formatday(self, day, weekday):
        """
        Return a day as a table cell.
        """
        if day == 0:
            # day outside month
            return '<td class="%s">&nbsp;</td>' % self.cssclass_noday
        else:
            tests_list = make_tests_list(
                get_tests(self.time + format(day, "=02")), self.subject_colors
            )
            return '<td class="%s" style="text-align: left; vertical-align: top;"><b>%d</b> %s</td>' % (
                self.cssclasses[weekday],
                day,
                tests_list,
            )

    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """
        v = []
        a = v.append
        a(
            '<table border="1" cellpadding="30" cellspacing="0" class="%s">'
            % (self.cssclass_month)
        )
        a("\n")
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a("\n")
        a(self.formatweekheader())
        a("\n")
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week))
            a("\n")
        a("</table>")
        a("\n")
        return "".join(v)


def make_calendar(year, month, subject_colors):
    # default: current month
    cal = CustomHTMLCalendar(
        firstweekday = 7,
        time=format(year, "=02") + "-" + format(month, "=02") + "-",
        subject_colors = subject_colors,
    )
    return cal.formatmonth(year, month)


def make_tests_list(tests, subject_colors):
    html = '<ol style="margin: 0px">'
    for test in tests:
        html += '<li style="color: %s">%s</li>' % (subject_colors[test[0]], test[1])
    html += "</ol>"
    return html


def get_tests(time):
    # time format: '2020-07-01'
    con = sql.connect("data.db")
    cur = con.cursor()
    cur.execute("SELECT subject, content FROM tests WHERE time = ?", (time,))
    tests = cur.fetchall()
    con.close()
    return tests


def add_test(time, subject, content):
    con = sql.connect("data.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO tests (time, subject, content) VALUES (?, ?, ?)",
        (time, subject, content),
    )
    con.commit()
    con.close()