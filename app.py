from multiprocessing import connection
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')
#It will route to update page   
@app.route('/update')
def updatemain():
   return render_template('update.html')

#It will route to range page
@app.route('/range')
def range():
   return render_template('range.html')
@app.route('/yearrange')
def yearrange():
   return render_template('yearrange.html')
@app.route('/numrange')
def numrange():
   return render_template('numrange.html')
#It will search the record from the table by using name
@app.route('/namesearch', methods=['POST','GET'])
def list():
    connection = sqlite3.connect('quiz1db.db')
    cursor = connection.cursor()
    field=str(request.form['name'])
    querry="Select * from datan WHERE Name =  '"+field+"' "
    cursor.execute(querry)
    rows = cursor.fetchall()
    connection.close()
    return render_template("getpicture.html",rows = rows)
#It will retrieve all the data from table
@app.route('/all', methods=['POST','GET'])
def fulllist():
    connection = sqlite3.connect('quiz1db.db')
    cursor = connection.cursor()
    querry="Select * from datan "
    cursor.execute(querry)
    rows = cursor.fetchall()
    connection.close()
    return render_template("list.html",rows = rows)
#It will update keyword of the record from the table by using name
@app.route('/keyupdate',methods=['POST','GET'])
def update():
    if (request.method=='POST'):
        connection = sqlite3.connect('quiz1db.db')
        cursor = connection.cursor()
        name= str(request.form['name'])
        keyword= str(request.form['keyword'])
        num= str(request.form['num'])
        querry=""
        if num and not(keyword):
            querry = "UPDATE datan SET num = '"+num+"'   WHERE Name ='"+name+"' "
        elif keyword and not(num):
            querry="UPDATE datan SET comments = '"+keyword+"'   WHERE Name ='"+name+"' "
        elif num and keyword:
            querry="UPDATE datan SET comments = '"+keyword+"', num = '"+num+"'   WHERE Name ='"+name+"' "
        cursor.execute(querry)
        connection.commit()
        querry2="Select * from datan "
        cursor.execute(querry2)
        rows = cursor.fetchall()
        connection.close()
    return render_template("list.html",rows = rows)

@app.route('/year',methods=['POST','GET'])
def yearran():
    if (request.method=='POST'):
        connection = sqlite3.connect('quiz1db.db')
        cursor = connection.cursor()
        range1= (request.form['range1'])
        range2= (request.form['range2'])
        querry="select * from datan WHERE year  between'"+range1+"'and'"+range2+"' "
        cursor.execute(querry)
        rows = cursor.fetchall()
        connection.close()
    return render_template("getpicture.html",rows = rows)

@app.route('/num', methods=['GET', 'POST'])
def notmatch():
    if (request.method=='POST'):
        connection = sqlite3.connect('quiz1db.db')
        cursor = connection.cursor()
        range1= (request.form['range1'])
        range2= (request.form['range2'])
        querry="select * from datan WHERE num  between'"+range1+"'and'"+range2+"' "
        cursor.execute(querry)
        rows = cursor.fetchall()
        connection.close()
    return render_template("getpicture.html",rows = rows)

if __name__ =="__main__":
    app.run(debug=True)
    