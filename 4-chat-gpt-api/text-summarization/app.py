import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

userInput = input("You: ")

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a text summarization chatbot. Your goal is to summarize the text that is given to you by the user."},
        {"role": "user", "content": userInput},

    ],
    temperature=0
)

response = completion.choices[0].message.content

print('Summarized Text: ', response)
