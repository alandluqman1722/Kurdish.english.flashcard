from flask import Flask, render_template, request, jsonify
import random
from datetime import datetime

app = Flask(__name__)

# Vocabulary data
vocabulary = {
    "a1": {
        "name": "A1 - Beginner",
        "description": "Basic words and phrases for everyday situations",
        "words": [
            {"word": "a, an", "translation": "یەکێک", "example": "I have an apple."},
            {"word": "about", "translation": "دەربارەی", "example": "Let's talk about you."},
            # ... (other A1 words)
        ]
    },
    "a2": {
        "name": "A2 - Elementary",
        "description": "Vocabulary for simple conversations and routine tasks",
        "words": [
            {"word": "achieve", "translation": "بەدەستهێنان", "example": "He achieved his goals."},
            {"word": "adult", "translation": "پێگەیشتوو", "example": "Adult education is important."},
            # ... (other A2 words)
        ]
    },
    # ... (other levels)
}

# Visitor counter
visitor_count = 0

@app.route('/')
def index():
    global visitor_count
    visitor_count += 1
    return render_template('index.html', 
                         vocabulary=vocabulary,
                         visitor_count=visitor_count)

@app.route('/start_level/<level>')
def start_level(level):
    if level in vocabulary:
        return render_template('flashcards.html', 
                             level_data=vocabulary[level],
                             current_level=level)
    return "Level not found", 404

@app.route('/get_quiz_questions/<level>/<int:count>')
def get_quiz_questions(level, count):
    if level in vocabulary:
        words = vocabulary[level]['words']
        selected = random.sample(words, min(count, len(words)))
        questions = []
        
        for word in selected:
            # Get 3 random wrong answers
            wrong_answers = [w['translation'] for w in random.sample(
                [w for w in words if w['word'] != word['word']], 
                min(3, len(words)-1))]
            
            options = [word['translation']] + wrong_answers
            random.shuffle(options)
            
            questions.append({
                'word': word['word'],
                'correct_answer': word['translation'],
                'options': options,
                'example': word['example']
            })
        
        return jsonify(questions)
    return "Level not found", 404

if __name__ == '__main__':
    app.run(debug=True)