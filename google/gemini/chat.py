#!/usr/bin/env python3

import vertexai.preview.generative_models as m

gemini = m.GenerativeModel("gemini-pro")
chat = gemini.start_chat()

while True:
    user_input = input("User: ")
    if user_input == "quit" or user_input == "q" or user_input == ":q":
        break
    response = chat.send_message(user_input)

    print()
    print(f"Gemini: {response.text}")
    print("---")
