from flask import Flask, request, jsonify
from flask_cors import CORS
from similarity_utils import combined_similarity

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return {"message": "IntelliCode API running 🚀"}

@app.route('/compare', methods=['POST'])
def compare_code():
    data = request.get_json()
    code1 = data.get('code1', '')
    code2 = data.get('code2', '')

    if not code1 or not code2:
        return jsonify({"error": "Both code inputs are required"}), 400

    similarity_score = combined_similarity(code1, code2)

    return jsonify({
        "similarity": similarity_score,
        "message": f"Similarity: {similarity_score}%"
    })

if __name__ == '__main__':
    app.run(debug=True)
