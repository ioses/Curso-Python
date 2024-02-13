import openai
import os

os.environ['API_KEY'] = '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'
openai.api_key = os.getenv('API_KEY')


def create_prompt(topic, num_qs, num_possible_answers):
    instructions = f'Create a multiple choice quiz on the topic of {topic}'
    details = f'The quiz should consist of {num_qs} questions. Each question should have {num_possible_answers} options, with one possible correct answer'
    example = 'for example "Q1. What type of programming language is Python? "'\
        +'A. Scripting language'\
        +'B. Assembly language '\
        +'C. Object Oriented language'\
        +'D. Functional language'\
        +'Answer: C. Object Oriented language'
    direct = 'the quiz should be challenging but not overly complex. The correct answe should be selected randomly' \
        +'from the available answers'
    
    quantitative = 'Each question should have a difficulty level of 7 on a scale of 1 to 10'

    return instructions + details + example + direct + quantitative

print (create_prompt('python',3,3))


response = openai.Completion.create(
    engine='text-davinci-003',
    prompt = create_prompt('python',3,3),
    max_tokens = 256
)

print(response['choices'][0]['text'])
