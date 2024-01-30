class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [Question("Which country has Moscow as its capital? ", "Russia"),Question("What is the longest river in the world? ", "Nile"),Question("Which is the largest planet? ", "Sun"),Question("Who painted the Mona Lisa? ", "Leonardo da Vinci"),Question("Which planet has the Moon as its satellite? ", "Earth"),Question("What is the symbol for the element iron? ", "Fe"),Question("What is the tallest mountain? ", "Everest"), Question("Which language is spoken the most? ", "Chinese"),Question("In which year did the conquest of Istanbul occur? ", "1453"),   Question("Which is the largest continent? ", "Asia")]

def run_quiz(questions):
    score = 0
    wrong_answers = []
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            wrong_answers.append((question.prompt, question.answer))
        print("Your current score is:", score, "/", len(questions))
    
    print("\nIncorrect answers:")
    for prompt, answer in wrong_answers:
        print(prompt, "Correct answer:", answer)

    print("\nYour final score is:", score, "/", len(questions))

run_quiz(questions)
