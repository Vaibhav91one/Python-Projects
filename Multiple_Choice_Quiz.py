from Question_Prompt import question_prompt

questions_and_options = ["Who is Known as The king of the jungle?\n (a)Tiger (b)Lion (c)Sheep\n",
                         "Who invented The light bulb?\n (a)Albert Einstein (b)Thomas Edison (c)Isaac Newton\n",
                         "What is the color of an Orange\n (a)Red (b)Blue (c)Orange\n"]

questions_and_answers = [question_prompt(questions_and_options[0], "b"),
                         question_prompt(questions_and_options[1], "b"),
                         question_prompt(questions_and_options[2], "c")]


def run_test(questions_and_answers):
    score = 0
    for question in questions_and_answers:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions_and_answers)) + "correct")


run_test(questions_and_answers)
