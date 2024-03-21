#!/usr/bin/python3

from web_app.app import db

# Define the dictionary class
# This class will be used to create the dictionary table
# The table will have the following columns:
# word_id, words, part_of_speech, and meanings
# The word_id column will be the primary key
# The words column will store the words
# The part_of_speech column will store the part of speech of the words
# The meanings column will store the meanings of the words


class dictionary(db.Model):
    word_id = db.Column(db.Integer, primary_key=True)
    words = db.Column(db.String(80), unique=False, nullable=False)
    part_of_speech = db.Column(db.String(80), unique=False, nullable=False)
    meanings = db.Column(db.String(800), unique=False, nullable=False)
    suggest_words = db.Column(db.String(80), unique=False, nullable=False)