from flask import Flask, jsonify, request
from flask_cors import CORS  # Import the CORS module
from gpt import generate_response  # Import the generate_response function

app = Flask(__name__)
CORS(app)


@app.route("/api/chat", methods=["POST"])
def chat():
    """
    Handles POST requests to the /api/chat endpoint. Retrieves the prompt from
    the client's JSON data, generates a response using the OpenAI model, and
    returns the response as a JSON object.
    Returns:
        A JSON object containing the AI-generated response or an error message.
    """
    data = request.get_json()
    prompt = data.get("prompt")
    if prompt:
        response = generate_response(prompt)
        return jsonify({"response": response})
    else:
        return jsonify({"error": "No prompt provided."})


if __name__ == "__main__":
    app.run(port=8000, debug=True)
