from flask import Flask, render_template, request, jsonify
from scale import process_swarams

app = Flask(__name__)

@app.route('/')   # <-- serve the homepage at /
def index():
    return render_template('Front_End.html')  # filename must match exactly

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    scale = data['scale']
    swarams = data['swarams']

    result = process_swarams(scale, swarams)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)