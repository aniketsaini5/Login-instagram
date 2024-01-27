from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# Database configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)


@app.route('/login', methods=['POST'])
def login():

    username = request.form.get('username')
    password = request.form.get('password')

 
    with db.cursor() as cursor:
        try:
            cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
            db.commit()
        except mysql.connector.IntegrityError as e:
            if e.errno == 1062:  
                return "Username already exists!"
            else:
                return "Error occurred while processing your request."

    return "login successfully!"

if __name__ == '__main__':
    app.run(debug=True)
