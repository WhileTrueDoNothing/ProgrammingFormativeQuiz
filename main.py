import quiz_utils as q

play_again = True
separator_string = "-----------"
print("Welcome to the UK postcode area quiz!")
print("How well do you think you know your postcode areas?")

while play_again:
    print(separator_string)
    print(
        "Difficulty options:\na) Normal (Multiple choices make things easier!)\nb) Hard (No hints here, just you and a free text input!)"
    )

    selected_difficulty = ""
    question_list = []

    while selected_difficulty == "":

        selected_difficulty = input("Select a difficulty: ")

        # generate questions of the selected difficulty or reset the input if it's invalid
        if selected_difficulty.lower() in ["a", "normal"]:
            print(separator_string)
            
            question_list = q.gen_questions_csv(
                "postcode_areas.csv",
                [
                    ("What is the postcode area for {postcode_area_name}?", "postcode_area"),
                    ("What is the full name of the postcode area {postcode_area}?", "postcode_area_name")
                ]
            )

            print("Good luck!")

        elif selected_difficulty in ["b", "hard"]:
            print(separator_string)

            question_list = q.gen_questions_csv(
                "postcode_areas.csv",
                [
                    ("What is the postcode area for {postcode_area_name}?", "postcode_area"),
                    ("What is the full name of the postcode area {postcode_area}?", "postcode_area_name")
                ],
                multi_choice=False
            )

            print("I hope you're ready for this.")

        else:
            print("That's not a difficulty option!")
            selected_difficulty = ""

    q.run_quiz(question_list, question_separator=separator_string)

    replay_input = input("Would you like to play again? (y/n): ")

    if replay_input.lower() == "y":
        print("Here we go again!")
    else:
        print("Thanks for playing!")
        play_again = False
