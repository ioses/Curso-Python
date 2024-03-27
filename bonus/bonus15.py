import json

with open('questions.json', 'r') as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print (index, "-", alternative)
    user_choice = int(input("Enter your answer: "))
    question ["user_choice"] = user_choice

    if question["user_choice"] == question ["correct_answer"]:
        score =+1
        result = "Correct answer"
    else:
        result = "Wrong answer"

for question in data:
    message = f"{index + 1} {result} - Your answer: {question['user_choice']}, " \
                f"Correct answer: {question['correct_answer']}"
    
    print (message)

print (score, "/", len(data))



