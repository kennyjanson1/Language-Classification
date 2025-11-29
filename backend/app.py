from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import XLMRobertaTokenizer, XLMRobertaForSequenceClassification, XLMRobertaConfig
from safetensors.torch import load_file
import torch
import json
import os

app = Flask(__name__)
CORS(app)

# Path & Labels
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "content", "results", "checkpoint-1650")

LABELS = {
    0: 'Arabic', 1: 'Chinese', 2: 'Dutch', 3: 'English', 4: 'Estonian',
    5: 'French', 6: 'Hindi', 7: 'Indonesian', 8: 'Japanese', 9: 'Korean',
    10: 'Latin', 11: 'Persian', 12: 'Portugese', 13: 'Pushto', 14: 'Romanian',
    15: 'Russian', 16: 'Spanish', 17: 'Swedish', 18: 'Tamil', 19: 'Thai',
    20: 'Turkish', 21: 'Urdu'
}

# Load Model
try:
    with open(os.path.join(MODEL_PATH, "config.json")) as f:
        config = XLMRobertaConfig.from_dict(json.load(f))
    
    model = XLMRobertaForSequenceClassification(config)
    model.load_state_dict(load_file(os.path.join(MODEL_PATH, "model.safetensors")))
    model.eval()
    
    tokenizer = XLMRobertaTokenizer.from_pretrained("xlm-roberta-base")
    print(f"✅ Model loaded: {len(LABELS)} languages")
except Exception as e:
    print(f"❌ Error: {e}")
    raise

@app.route('/predict', methods=['POST'])
def predict():
    text = request.get_json().get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    try:
        inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
        
        with torch.no_grad():
            logits = model(**inputs).logits
            probs = torch.softmax(logits, dim=1)[0]
            pred = torch.argmax(probs).item()
        
        top3 = torch.topk(probs, k=3).indices.tolist()
        
        return jsonify({
            "language": LABELS[pred],
            "confidence": float(probs[pred]),
            "top3": [{"language": LABELS[i], "confidence": float(probs[i])} for i in top3],
            "status": "success"
        })
    except Exception as e:
        return jsonify({"error": str(e), "status": "failed"}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "num_classes": len(LABELS)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)