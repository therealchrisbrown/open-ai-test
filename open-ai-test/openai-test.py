from decouple import config

OPEN_AI_API_KEY=config('OPENAI_API_KEY')

import openai
openai.api_key=OPEN_AI_API_KEY

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt="Ich würde gerne einen Flug buchen",
  max_tokens=60
)

answer = response.choices[0].text
print(answer)
