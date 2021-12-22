'''
database with sqlite 3
-------------------------

'''

import sqlite3 
from datetime import datetime


class Database:
    def __init__(self) -> None:
        self.conn=sqlite3.connect('Library.sqlite3')
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS tblbook(id INTEGER PRIMARY KEY, title VARCHAR(50),author VARCHAR(50), year INTEGER,pdate DATE )")
        self.conn.commit()

    def adddata (self):
        print('Add your record: ')
        print('='*40)
        t1=input('Title: ')
        a1=input('Author: ')
        y1=input('Year : ')

        self.cur.execute("INSERT  INTO tblbook(title,author,year,pdate) VALUES(?,?,?,?)",(t1,a1,y1,datetime.today()))
        self.conn.commit()


    def showdata(self):
        self.cur.execute('SELECT * FROM tblbook')
        print("\n\n%-5s %-20s %-15s %-10s %-10s "%('ID','TITLE','AUTHOR','YEAR','PDATE'))
        print('='*80)
        for data in self.cur.fetchall() :
            print("%-5s %-20s %-15s %-10s %-10s "%(data[0],data[1],data[2],data[3],data[4]))

       
db= Database()
db.adddata()   
db.showdata()