from flask import render_template, request, jsonify
from web_app.app import app, db
from web_app.app import models
from web_app.app.models import dictionary



@app.route('/', strict_slashes=False)
def homepage():
    return render_template('index.html')


@app.route('/lexi_vault', strict_slashes=False, methods=['GET', 'POST'])
def lexi_vault():
    dictionary_data = dictionary.query.with_entities(dictionary.words).all()
    all_words = '\n'.join(word[0] for word in dictionary_data if word[0] is not None)

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
            return render_template('lexi_vault.html', word=word, meaning=meaning, part_of_speech=part_of_speech, all_words=all_words)
    return render_template('lexi_vault.html', all_words=all_words)  

@app.route('/suggest', strict_slashes=False, methods=['GET', 'POST'])
def suggest():
   suggested_words = dictionary.query.with_entities(dictionary.suggest_words).all()
   
   if request.method == 'POST':
        word = request.form.get('word')
        if not word:
            return 'Please provide a word to suggest'

        existing_word = dictionary.query.filter_by(words=word).first()
        if existing_word:
            return 'Word is already in the dictionary'

        suggested_word = dictionary.query.filter_by(suggest_words=word).first()
        if suggested_word:
            return 'Word is already suggested and will be added soon'

        new_word = dictionary(suggest_words=word)
        db.session.add(new_word)
        db.session.commit()
        return 'Word added successfully'

    # Fetch all suggested words from the database
   
   return render_template('suggest.html', suggested_words=suggested_words)


@app.route('/developers', strict_slashes=False)
def developers():
    return render_template('developers.html')


@app.route('/about', strict_slashes=False)
def about():
    return render_template('about.html')


            
    

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')