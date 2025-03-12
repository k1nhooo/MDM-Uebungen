from flask import Flask, render_template, request, jsonify

def alternate_case(text):
    return ''.join([char.upper() if i % 2 else char.lower() for i, char in enumerate(text)])

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transform', methods=['POST'])
def transform():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Kein Text angegeben"}), 400
    
    text = data["text"]
    transformed_text = alternate_case(text)
    return jsonify({"result": transformed