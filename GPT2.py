import openai
import os

os.environ['API_KEY'] = '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'
openai.api_key = os.getenv('API_KEY')

instructions = 'Write me a short story about a rabbit named Bob who lives in a forest'
details = 'Bob is a detective and is solving a crime. The period of the story should be set in the edwardian era'

prompt = instructions + details

response = openai.Completion.create(
    engine='text-davinci-003',
    prompt = prompt,
    max_tokens = 500
)

print(response['choices'][0]['text'])