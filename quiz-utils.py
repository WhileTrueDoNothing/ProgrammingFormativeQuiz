"""Tools for creating questions and quizzes."""

from random import shuffle
from string import ascii_lowercase


class Question:
    """A question that can be answered by a free text input."""

    question: str
    answers: list[str]

    def __init__(self, question, answers):
        """
        Create a new Question.

        Args:
            question (str): The text for the question to be asked.
            answers (list[str]): The correct answer(s) for the question.
        """
        self.question = question
        self.answers = answers

    def ask(self):
        """
        Asks the user the question. Returns 1 if the user inputs the correct answer, or 0 otherwise.
        """
        print(self.question)
        user_answer = input("Your answer: ")
        if user_answer.lower() in [answer.lower() for answer in self.answers]:
            print("Correct!")
            return 1
        else:
            print("Incorrect!")
            return 0


class MultiChoiceQuestion(Question):
    """A multiple choice question. Supports up to 26 options."""

    wrong_answers: list[str]

    def __init__(self, question, answers, wrong_answers):
        """
        Create a new MultiChoiceQuestion.

        Args:
            question (str): The text for the question to be asked.
            answers (list[str]): The correct answer(s) for the question.
            wrong_answers (list[str]): Other options for the question.

        Raises:
            ValueError: If the combined length of correct and incorrect answer lists is higher than 26.
        """
        if len(answers) + len(wrong_answers) > 26:
            raise ValueError(
                "Combined length of correct and incorrect answer lists must be 26 or less. Total options received: {total}".format(
                    total=len(answers) + len(wrong_answers)
                )
            )
        self.wrong_answers = wrong_answers
        super().__init__(question, answers)

    def ask(self):
        """
        Asks the user the question, loops until an option is selected. Returns 1 if the user inputs the correct answer, or 0 otherwise.
        """
        all_options = self.answers + self.wrong_answers
        shuffle(all_options)

        option_list = {}

        for letter, option in zip(list(ascii_lowercase), all_options):
            option_list[letter] = option

        full_question_text = (
            self.question
            + "\n"
            + "\n".join(
                "{index}) {option}".format(index=key, option=value)
                for key, value in option_list.items()
            )
        )

        print(full_question_text)

        valid_input = False

        while not valid_input:
            user_answer = input("Your answer: ")
            if user_answer.lower() in option_list.keys():
                valid_input = True
                if option_list[user_answer.lower()] in self.answers:
                    print("Correct!")
                    return 1
                else:
                    print("Incorrect!")
                    return 0
            elif user_answer.lower() in [
                option.lower() for option in option_list.values()
            ]:
                valid_input = True
                if user_answer.lower() in [answer.lower() for answer in self.answers]:
                    print("Correct!")
                    return 1
                else:
                    print("Incorrect!")
                    return 0
            else:
                print("Please enter one of the options!")
        print("How is this method still running?")
        return 0


def run_quiz(
    questions: list[Question],
    score_per_question: int = 1,
    question_separator: str = "-----------",
    first_question_num: int = 1,
):
    """
    Runs a quiz.

    Args:
        questions (list[Question]): The list of questions to ask.
        score_per_question (int, optional): The score for a correct answer. Defaults to 1.
        question_separator (str, optional): A string to separate questions in the terminal. Defaults to -----------.
        first_question_num (int, optional): The number of the first question in the quiz. Defaults to 1.

    Returns:
        int: The total score for the quiz.
    """
    if len(questions) == 0:
        raise ValueError("A quiz needs to have questions!")

    score = 0

    for i in range(0, len(questions)):
        print(question_separator)
        print("Question {q_num}".format(q_num=i + first_question_num))
        print(question_separator)
        score += questions[i].ask()

    print(question_separator)
    print("Your score: {total}".format(total=score))
    print(question_separator)
    return score
