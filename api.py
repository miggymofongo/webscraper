from flask import Flask, jsonify, request
import json
import random

app = Flask(__name__)

# load quotes from JSON 
def load_quotes():
    with open('quotes.json', 'r') as file:
        return json.load(file)

# API endpoint for getting a random quote
@app.route('/api/random-quote', methods=['GET'])
def random_quote():
    quotes = load_quotes()
    return jsonify(random.choice(quotes))

if __name__ == '__main__':
    app.run(debug=True)
