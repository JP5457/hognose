import os
from openai import OpenAI

class AiManager:
    def __init__(self, key):
        self.apikey = key
        self.client = OpenAI(api_key=self.apikey)

    def generate_text(self, prompt):
        chat_completion = self.client.chat.completions.create(
            messages = [
                {
                "role": "user",
                "content": prompt
                }
            ],
            model="gpt-4o-mini"
        )
        return chat_completion.choices[0].message.content