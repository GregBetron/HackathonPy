#import tensorflow as tf
import numpy as np
import aikey    #secure ai key from Google Gemini
import os
import google.generativeai as genai

genai.configure(api_key=os.environ[aikey])

file = genai.upload_file(media / "papertrash.jpg")
print(f"{file=}")

model = genai.GenerativeModel("gemini-1.5-flash")
result = model.generate_content(
    [file, "\n\n", "Can you tell me about what object is in this photo?"]
)
print(result.text)