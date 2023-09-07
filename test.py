import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat():
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
    )

    print(completion.choices[0].message)

def image():
    data = openai.Image.create(
    prompt="A picture shows after life, 4k details, show the environment",
    n=10,
    size="1024x1024"
    )

    print(data)
    return data
