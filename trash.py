
num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
questions = random.sample(list(QUESTIONS.items()),k=num_questions)

num_correct = 0
for num, (question, alternatives) in enumerate(questions,start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(
        zip(ascii_lowercase, random.sample(alternatives,k=len(alternatives)))
        )
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice?")) not in labeled_alternatives:
        print(f"Please enter one of {', '.join(labeled_alternatives)}")
    answer = labeled_alternatives[answer_label]

    if answer == correct_answer:
        num_correct += 1
        print("✅ Correct!")
    else:
        print(f"The correct answer is {correct_answer!r}, not {answer!r}")
        
print(f"\nYou got {num_correct} correct out of {num} questions")

