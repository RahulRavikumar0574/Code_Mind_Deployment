from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/explain', methods=['POST'])
def explain():
    code = request.json.get('code', '')
    explanation = f"This code has {len(code.splitlines())} lines. Look at classes and functions in the code."
    return jsonify({"explanation": explanation})

if __name__ == "__main__":
    app.run(port=5000)
