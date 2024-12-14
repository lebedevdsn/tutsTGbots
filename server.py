from flask import Flask, request, jsonify

app = Flask(__name__)

# Хранилище для сообщений
data_store = []

@app.route('/post', methods=['POST'])
def post_message():
    content = request.json
    if not content or 'type' not in content or 'content' not in content:
        return jsonify({"error": "Invalid data"}), 400

    data_store.append(content)
    return jsonify({"message": "Content added successfully!"}), 201

@app.route('/get', methods=['GET'])
def get_messages():
    return jsonify(data_store)

if __name__ == '__main__':
    app.run(debug=True)