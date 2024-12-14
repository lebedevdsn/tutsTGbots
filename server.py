from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Логирование
logging.basicConfig(level=logging.INFO)

# Список для хранения контента
content_list = []

# API для получения контента
@app.route('/get', methods=['GET'])
def get_content():
    return jsonify(content_list), 200

# API для получения контента
@app.route('/post', methods=['POST'])
def post_content():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    # Сохраняем контент
    content_type = data.get("type")
    content = data.get("content")
    
    # Добавляем новый элемент в список
    content_list.append({"type": content_type, "content": content})

    logging.info(f"Received {content_type} with content: {content}")
    
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    # Запускаем сервер на 0.0.0.0 для доступа извне
    app.run(host='0.0.0.0', port=5000, debug=True)