from flask import Flask,request,jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)

CORS(app)

conn =  mysql.connector.connect(
    host='db1',
    port=3306, 
    user='root',
    password='example1',
    database='dbUsers'
)

@app.route("/users/load", methods=["GET"])
def load():
    cursor = conn.cursor()
    cursor.execute("Select U.id_user, U.username, U.password, UI.name, UI.email, UI.description " \
    "FROM Users U, Users_Info UI WHERE U.id_user=UI.id_user;")

    usersjson = cursor.fetchall()

    result = [{
        'id_user': row[0],
        'username': row[1],
        'password': row[2],
        'name': row[3],
        'email': row[4],
        'description': row[5]}
        for row in usersjson]
    
    cursor.close()

    return{'result':result}

@app.route("/insertuser", methods=["POST"])
def insertausers():
    username = request.form['username']
    password = request.form['password']
    name = request.form['name']
    email = request.form['email']
    description = request.form['description']

    cursor = conn.cursor()
    
    cursor.execute("insert into Users (username,password) values (%s,%s);",(username,password))

    query = "select id_user from Users where username = %s;"
    cursor.execute(query, (username,))
    id_user = cursor.fetchall()
    
    cursor.execute("insert into Users_Info (id_user,name,email,description) values (%s, %s, %s, %s);", (id_user[0][0],name,email,description))
    
    conn.commit()
    cursor.close()

    return jsonify({'message' : 'usuario insertado correctamente'})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=666) 


