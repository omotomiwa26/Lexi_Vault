from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import create_engine

# Replace 'username', 'password', 'hostname', 'port', and 'database_name' with your actual credentials
username = 'lexi_vault'
password = 'lexipass'
hostname = 'localhost'  # or your MySQL server's IP address
port = '3306'  # or your MySQL server's port
database_name = 'lexi_vault_db'

# Construct the MySQL connection URL
url = f"mysql+pymysql://{username}:{password}@{hostname}:{port}/{database_name}"

# Create the SQLAlchemy engine
engine = create_engine(url)

# Now you can use this engine object to interact with your MySQL database


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class dictionary(db.Model):
    word_id = db.Column(db.Integer, primary_key=True)
    words = db.Column(db.String(80), unique=False, nullable=False)
    part_of_speech = db.Column(db.String(80), unique=False, nullable=False)
    meanings = db.Column(db.String(800), unique=False, nullable=False)

@app.route('/Lexi_Vault', strict_slashes=False, methods=['GET', 'POST'])
def lexi_vault():
   #dictionary_data = dictionary.query.all()
    dictionary_data = dictionary.query.with_entities(dictionary.words).all()
    
    all_words = '\n'.join(word[0] for word in dictionary_data)
    #dictionary_data = dictionary.query.filter_by(words="cage").all()
    return render_template('lexi_vault.html', dictionary=all_words)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')