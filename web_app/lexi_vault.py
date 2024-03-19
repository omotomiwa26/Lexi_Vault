from flask import Flask, render_template, request, jsonify
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

@app.route('/lexi_vault', strict_slashes=False, methods=['GET', 'POST'])
def lexi_vault():
    dictionary_data = dictionary.query.with_entities(dictionary.words).all()
    all_words = '\n'.join(word[0] for word in dictionary_data)

    if request.method == 'POST':
        word = request.form.get('word')
        if word:
            dictionary_data = dictionary.query.filter_by(words=word).first()
            if dictionary_data:
                word = dictionary_data.words
                meaning = dictionary_data.meanings
                part_of_speech = dictionary_data.part_of_speech
            else:
                meaning = 'Word Not Found'
                part_of_speech = 'Please add to list of suggested words'
            # all_words_data = dictionary.query.with_entities(dictionary.words).all()
            # all_words = '\n'.join(word[0] for word in dictionary_data)
            return render_template('lexi_vault.html', word=word, meaning=meaning, part_of_speech=part_of_speech, all_words=all_words)
            # dictionary_data = dictionary.query.filter_by(words='word').all()
            # return render_template('lexi_vault.html', dictionary=dictionary_data)
    return render_template('lexi_vault.html', all_words=all_words)
    #     #     return render_template('lexi_vault.html', dictionary='Word not found')
    # #dictionary_data = dictionary.query.all()


@app.route('/get_word_details', methods=['POST'])
def get_word_details():
    word = request.form.get('wordtext')
    if word:
        dictionary_data = dictionary.query.filter_by(words=word).first()
        if dictionary_data:
            meaning = dictionary_data.meanings
            part_of_speech = dictionary_data.part_of_speech
            return jsonify({'meaning': meaning, 'part_of_speech': part_of_speech})
    return jsonify({'error': 'Word not found'})

            
    

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')