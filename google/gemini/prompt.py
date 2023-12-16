#!/usr/bin/env python3

import vertexai.preview.generative_models as m
import sys

gemini = m.GenerativeModel("gemini-pro")
responses = gemini.generate_content(sys.argv[1], stream=True)

for response in responses:
    print(response.text)

