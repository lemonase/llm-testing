#!/usr/bin/env python3

import os

from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def chat_with_gpt(prompt):
    model = "gpt-4"
    temperature = 0.7
    max_tokens = 150

    stream = client.chat.completions.create(
        model=model,
        messages=[{
            "role": "user",
            "content": prompt
        }],
        temperature=temperature,
        max_tokens=max_tokens,
        stream=True,
    )
    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")
    print("---")
    print()


if __name__ == "__main__":
    print("ChatGPT Bot: Hello! Type 'exit' to end the conversation.")
    while True:
        user_input = input(f'You: ({os.environ.get("USER")}): ')

        if user_input.lower() == 'exit':
            print("ChatGPT Bot: Goodbye!")
            break
        chat_with_gpt(user_input)


# Code for getting some kind of memory with previous prompts added as messages
# while not user_messages[0]['content'] == "exit":
#     response = client.chat.completions.create(messages=system_messages + chat[-10:] + user_messages,
#                                             model=model,
#                                             stream=True)
#     reply = ""
#     for delta in response:
#         if not delta['choices'][0]['finish_reason']:
#             word = delta['choices'][0]['delta']['content']
#             reply += word
#             print(word, end="")
#     chat += user_messages + [{"role": "assistant", "content": reply}]
#     user_messages = [{"role": "user", "content": input("\nUser: ")}]
