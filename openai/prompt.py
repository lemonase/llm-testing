#!/usr/bin/env python3

import sys

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

messages = [{"role": "user", "content": sys.argv[1]}]
model = "gpt-4"

chat_completion = client.chat.completions.create(messages=messages,
                                                 model=model)

print(chat_completion.choices[0].message.content)

