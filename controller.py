import sqlite3 as sql
from models import add_test

option = input("operation:")
if option == "add":
    test = input("time(yyyy-mm-dd) subject content:")
    test = test.split(" ")
    time = test[0]
    subject = test[1]
    content = test[2]
    add_test(time, subject, content)
    print("complete")
