from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from cerebras.cloud.sdk import Cerebras

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize the Cerebras client with the API key
client = Cerebras(api_key="csk-pc39jkypw585669k943fm2d8ekx5jwpmddydedk9vcxk35xx")

def get_cerebras_response(user_message):
    try:
        # Create a chat completion request with the desired model
        chat_completion = client.chat.completions.create(
            model="llama3.1-8b",  # Adjust model name as needed
            messages=[
                {"role": "user", "content": user_message},
            ]
        )
        # Access the response content correctly
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
