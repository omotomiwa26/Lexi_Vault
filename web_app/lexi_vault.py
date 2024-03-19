from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import create_engine
from models import dictionary
from sqlalchemy.orm import sessionmaker




@app.route('/', strict_slashes=False)
def homepage():
    return render_template('index.html')


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
                part_of_speech = 'Please click the link below to add it to list of suggested words'
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


@app.route('/suggest', strict_slashes=False, methods=['GET', 'POST'])
def suggest():
    return render_template('suggest.html')


@app.route('/developers', strict_slashes=False)
def developers():
    return render_template('developers.html')


@app.route('/about', strict_slashes=False)
def about():
    return render_template('about.html')


            
    

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')