from flask import Flask, render_template, request, jsonify
from transformers import pipeline
import torch

app = Flask(__name__)

# Carregar o modelo uma vez ao iniciar o app
print("Carregando modelo...")
analyzer = pipeline("sentiment-analysis")
print("Modelo carregado!")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json.get('text', '')
    if not text:
        return jsonify({'error': 'Texto vazio'}), 400
    
    try:
        result = analyzer(text)[0]
        return jsonify({
            'sentiment': result['label'],
            'confidence': f"{result['score']:.2%}"
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)