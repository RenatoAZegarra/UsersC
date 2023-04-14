from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Configure MySQL Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database= " users_db "
)

# Create Cursor Object
mycursor = mydb.cursor()

# Define routes
@app.route('/')
def index():
    # Get all users
    mycursor.execute("SELECT * FROM users")
    users = mycursor.fetchall()
    return render_template('index.html', users=users)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Get form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        
        # Insert new user
        sql = "INSERT INTO users (first_name, last_name, email) VALUES (%s, %s, %s)"
        val = (first_name, last_name, email)
        mycursor.execute(sql, val)
        mydb.commit()
        
        # Redirect to read page
        return redirect('/')
    else:
        return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)