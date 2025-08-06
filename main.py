from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "🎲 Dice API is running!"

@app.route('/roll_dice_sets', methods=['GET'])
def roll_dice_sets():
    fixed_counts = {i: 5 for i in range(1, 7)}
    dice_faces = []
    for face, count in fixed_counts.items():
        dice_faces.extend([face] * count)
    random.shuffle(dice_faces)
    sets = [dice_faces[i:i+3] for i in range(0, 30, 3)]
    random.shuffle(sets)
    result = {f"Set {i+1}": sets[i] for i in range(10)}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
