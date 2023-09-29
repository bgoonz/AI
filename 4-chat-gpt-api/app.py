import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


messages = []

while True:

    userInput = input("You: ")

    messages.append({"role": "user", "content": userInput})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,

    )

    response = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": response})

    # print(completion)
    print('RESPONSE:', response)
