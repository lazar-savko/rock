from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.json.get('choice')
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(user_choice, computer_choice)
    return jsonify({'user_choice': user_choice, 'computer_choice': computer_choice, 'result': result})

def determine_winner(user, computer):
    outcomes = {
        ('rock', 'scissors'): 'win',
        ('scissors', 'paper'): 'win',
        ('paper', 'rock'): 'win',
        ('scissors', 'rock'): 'lose',
        ('paper', 'scissors'): 'lose',
        ('rock', 'paper'): 'lose'
    }
    if user == computer:
        return 'draw'
    return outcomes.get((user, computer), 'draw')

if __name__ == '__main__':
    app.run(debug=True)
