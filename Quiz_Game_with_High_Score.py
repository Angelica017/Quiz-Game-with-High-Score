# QUIZ GAME WITH HIGH SCORE

questions = [
    {
        "question": "What does CPU stand for?",
        "choices": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Utility",
            "D. Control Processing User"
        ],
        "answer": "A"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "choices": [
            "A. //",
            "B. #",
            "C. /*",
            "D. --"
        ],
        "answer": "B"
    },
    {
        "question": "Which function is used to display output in Python?",
        "choices": [
            "A. input()",
            "B. display()",
            "C. print()",
            "D. output()"
        ],
        "answer": "C"
    },
    {
        "question": "Which data type stores whole numbers?",
        "choices": [
            "A. float",
            "B. str",
            "C. bool",
            "D. int"
        ],
        "answer": "D"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "choices": [
            "A. function",
            "B. create",
            "C. def",
            "D. func"
        ],
        "answer": "C"
    },
    {
        "question": "Which loop is commonly used to repeat through a list?",
        "choices": [
            "A. for",
            "B. switch",
            "C. case",
            "D. select"
        ],
        "answer": "A"
    },
    {
        "question": "Which function is used to get input from the user?",
        "choices": [
            "A. print()",
            "B. input()",
            "C. write()",
            "D. read()"
        ],
        "answer": "B"
    },
    {
        "question": "Which operator checks if two values are equal?",
        "choices": [
            "A. =",
            "B. !=",
            "C. ==",
            "D. >="
        ],
        "answer": "C"
    },
    {
        "question": "Which data type stores text?",
        "choices": [
            "A. str",
            "B. int",
            "C. float",
            "D. bool"
        ],
        "answer": "A"
    },
    {
        "question": "What does the break statement do?",
        "choices": [
            "A. Starts a loop",
            "B. Stops a loop",
            "C. Prints a message",
            "D. Creates a function"
        ],
        "answer": "B"
    }
]


def show_question(question_data):
    print("\n" + question_data["question"])

    for choice in question_data["choices"]:
        print(choice)

    while True:
        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer in ["A", "B", "C", "D"]:
            return answer
        else:
            print("Invalid input. Please enter A, B, C, or D.")


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        print("Correct answer:", correct_answer)
        return 0


def run_quiz():
    score = 0

    print("\n==============================")
    print("        QUIZ GAME")
    print("==============================")

    for question in questions:
        user_answer = show_question(question)
        score += check_answer(user_answer, question["answer"])

    return score


def show_result(player_name, score, total_questions):
    percentage = (score / total_questions) * 100

    print("\n==============================")
    print("        QUIZ RESULT")
    print("==============================")
    print("Player:", player_name)
    print("Score:", score, "/", total_questions)
    print("Percentage:", percentage, "%")

    if percentage >= 80:
        print("Excellent performance!")
    elif percentage >= 60:
        print("Good job!")
    else:
        print("Keep practicing!")


def main():
    print("==============================")
    print("  QUIZ GAME WITH HIGH SCORE")
    print("==============================")

    player_name = input("Enter your name: ")
    high_score = 0

    while True:
        score = run_quiz()

        show_result(player_name, score, len(questions))

        if score > high_score:
            high_score = score
            print("\nNew High Score!")

        print("Current High Score:", high_score, "/", len(questions))

        play_again = input("\nDo you want to play again? (Y/N): ").upper()

        if play_again != "Y":
            print("\nThank you for playing,", player_name + "!")
            print("Final High Score:", high_score)
            break


main()
