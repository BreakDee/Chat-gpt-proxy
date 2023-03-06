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

    # call OpenAI's API
    url = "https://api.openai.com/v1/engine/davinci/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"
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
    app.run(debug=True)
