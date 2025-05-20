#!/usr/bin/env python3
import random

QUESTIONS = [
    "What is a variable?",
    "Explain the difference between list and tuple.",
    "How does a Python dictionary work?",
    "What is a lambda function?",
    "Describe a list comprehension.",
    "What does the 'self' keyword do?",
    "Explain inheritance in OOP.",
    "What is PEP 8?",
]

def get_quiz(num_questions=5):
    """Shuffle QUESTIONS and return num_questions of them."""
    if num_questions > len(QUESTIONS):
        raise ValueError("Requested more questions than available.")
    pool = QUESTIONS.copy()
    random.shuffle(pool)
    return pool[:num_questions]

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate a random quiz")
    parser.add_argument("-n", "--number", type=int, default=5,
                        help="Number of questions to include")
    args = parser.parse_args()

    quiz = get_quiz(args.number)
    print("Your randomized quiz:")
    for i, q in enumerate(quiz, 1):
        print(f"{i}. {q}")
