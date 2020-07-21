import calendar
import sqlite3 as sql

class CustomHTMLCalendar(calendar.HTMLCalendar):
    def __init__(self, firstweekday, time):
        super(CustomHTMLCalendar, self).__init__()
        self.time = time
    def formatday(self, day, weekday):
        """
        Return a day as a table cell.
        """
        if day == 0:
            # day outside month
            return '<td class="%s">&nbsp;</td>' % self.cssclass_noday
        else:
            tests_list = make_tests_list(get_tests(self.time + format(day, '=02')))
            return '<td class="%s">%d %s</td>' % (self.cssclasses[weekday], day, tests_list)
    def formatyear(self, theyear, width=3):
        """
        Return a formatted year as a table of tables.
        """
        January = 1
        v = []
        a = v.append
        width = max(width, 1)
        a('<table border="0" cellpadding="10" cellspacing="10" class="%s">' %
          self.cssclass_year)
        a('\n')
        a('<tr><th colspan="%d" class="%s">%s</th></tr>' % (
            width, self.cssclass_year_head, theyear))
        for i in range(January, January+12, width):
            # months in this row
            months = range(i, min(i+width, 13))
            a('<tr>')
            for m in months:
                a('<td>')
                a(self.formatmonth(theyear, m, withyear=False))
                a('</td>')
            a('</tr>')
        a('</table>')
        return ''.join(v)

def make_calendar(year, month):
    cal = CustomHTMLCalendar(firstweekday = 7, time = format(year, '=02') + '-' + format(month, '=02') + '-')
    return cal.formatmonth(year, month)

def make_tests_list(tests):
    html = '<ol style="margin: 0px">'
    for test in tests:
        html += '<li>%s</li>'%test[1] # test[1]: content
    html += '</ol>'
    return html

def get_tests(time):
    # time format: '2020-07-01'
    # [[date, subject, content], ...]
    con = sql.connect('data.db')
    cur = con.cursor()
    cur.execute('SELECT subject, content FROM tests WHERE time = ?', (time,))
    tests = cur.fetchall()
    con.close()
    return tests # needs editing format