from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/generate_text', methods=['POST'])
def generate_text():
    # get data from the request
    data = request.json
    prompt = data.get('prompt')
    max_tokens = data.get('max_tokens')
    n = data.get('n')
    stop = data.get('stop')

    # extract the API key from the Authorization header
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({'error': 'Missing Authorization header'}), 401
    auth_header_parts = auth_header.split(' ')
    if len(auth_header_parts) != 2 or auth_header_parts[0].lower() != 'bearer':
        return jsonify({'error': 'Invalid Authorization header'}), 401
    api_key = auth_header_parts[1]

    # call OpenAI's API
    url = "https://api.openai.com/v1/engine/davinci/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "prompt": prompt,
        "max_tokens": max_tokens,
        "n": n,
        "stop": stop
    }
    response = requests.post(url, headers=headers, json=payload)
    response_data = response.json()

    # return the response as JSON
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
