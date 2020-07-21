import sqlite3 as sql
option = input('operation:')
if option == 'add':
    test = input('time(yyyy-mm-dd) subject content:')
    test = test.split(' ')
    time = test[0]
    subject = test[1]
    content = test[2]
    con  = sql.connect('data.db')
    cur = con.cursor()
    cur.execute('INSERT INTO tests (time, subject, content) VALUES (?, ?, ?)', (time, subject, content))
    con.commit()
    con.close()
    print('complete')