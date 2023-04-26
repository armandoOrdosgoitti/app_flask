from flask import Flask,render_template,redirect,url_for
from flask import request
import mysql.connector
conector = mysql.connector.connect(host = 'localhost', user= "root",password = '',database = 'app_flask')
cursor = conector.cursor()

app=Flask(__name__)

@app.route('/')
def index():
    cursor.execute('select * from registro')
    data = cursor.fetchall()
    return render_template('index.html',datos = data)

@app.route('/user',methods=['POST'])
def user():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        nacionalidad = request.form['nacionalidad']
        sql ='INSERT INTO registro(nombre,apellido,edad,nacionalidad)VALUES(%s,%s,%s,%s)'
        datos = (nombre,apellido,edad,nacionalidad)
        cursor.execute(sql,datos)
        conector.commit()
    return redirect(url_for('index'))

