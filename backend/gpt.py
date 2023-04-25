import openai
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_response(prompt):
    """
    Generates a conversational response using the OpenAI GPT model with
    the `text-curie-001` engine, based on the provided prompt.

    Args:
        prompt (str): The input prompt for the GPT model.

    Returns:
        str: The AI-generated response as a string.
    """
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message
