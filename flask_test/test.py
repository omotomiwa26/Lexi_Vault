from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import create_engine

# Replace 'username', 'password', 'hostname', 'port', and 'database_name' with your actual credentials
username = 'test'
password = 'pass'
hostname = 'localhost'  # or your MySQL server's IP address
port = '3306'  # or your MySQL server's port
database_name = 'employees'

# Construct the MySQL connection URL
url = f"mysql+pymysql://{username}:{password}@{hostname}:{port}/{database_name}"
print(url)

# Create the SQLAlchemy engine
engine = create_engine(url)

# Now you can use this engine object to interact with your MySQL database


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class employees(db.Model):
    emp_no = db.Column(db.Integer, primary_key=True)
    birth_date = db.Column(db.String(80), unique=False, nullable=False)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=False)
    hire_date = db.Column(db.String(80), unique=False, nullable=False)

@app.route('/')
def index():
    employees_data = employees.query.all()
    return render_template('index.html', employees=employees_data)

if __name__ == '__main__':
    app.run(debug=True)