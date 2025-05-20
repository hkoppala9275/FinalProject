# File: advanced/random_quiz.py
#!/usr/bin/env python3
"""
A simple script to shuffle quiz questions and select a random subset using the standard random module.
"""
import random  # Provides functions for randomization

# Predefined pool of quiz questions\ nQUESTIONS = [
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
    """
    Shuffle QUESTIONS and return a list of num_questions items.
    Raises ValueError if requested more questions than available.
    """
    if num_questions > len(QUESTIONS):
        raise ValueError(f"Requested {num_questions} questions, but only {len(QUESTIONS)} available.")
    pool = QUESTIONS.copy()            # Make a shallow copy to avoid modifying the original list
    random.shuffle(pool)               # In-place shuffle of the copy
    selected = pool[:num_questions]    # Take the first num_questions questions
    return selected

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Generate a randomized quiz from a fixed question pool"
    )
    parser.add_argument(
        "-n", "--number", type=int, default=5,
        help="Number of questions to include (default: 5)"
    )
    args = parser.parse_args()

    # Generate quiz and print each question with numbering
    quiz = get_quiz(args.number)
    print("Your randomized quiz:")
    for idx, q in enumerate(quiz, start=1):
        print(f"{idx}. {q}")
