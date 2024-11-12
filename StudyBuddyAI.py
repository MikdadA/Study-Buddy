from flask import Flask, request, jsonify
from flask_cors import CORS  
from cerebras.cloud.sdk import Cerebras

app = Flask(__name__)
CORS(app) 

client = Cerebras(api_key="csk-pc39jkypw585669k943fm2d8ekx5jwpmddydedk9vcxk35xx")

def get_cerebras_response(user_message):
    try:

        chat_completion = client.chat.completions.create(
            model="llama3.1-8b", 
            messages=[
                {"role": "user", "content": user_message},
            ]
        )

        response_content = chat_completion.choices[0].message.content
        return response_content
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = get_cerebras_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
