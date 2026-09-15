#Python Quiz Game

questions = (
    "What is my name?",
    "what is the verison curently am I?",
    "Who is the creator of Me?",
    "Am I opensource project or private project?"
)
options =(
    ("a. Rust","b. Golang","c. Python","d. C++"),
    ("a. 0.1","b. 0.12","c. 12.3","d. 3.13"),
    ("a. Tharun","b. Theja","c. Priya","d. Susrutha"),
    ("a. MayBe","b. Open-Source","c. Private","d. Not Both of Them")
)
answers = (
    "c","d","a","b"
)
guesses = []
score = 0
question_nums= 0

for question in questions:
    print("===*===*===*===*===*===*===")
    print(question)
    for option in options[question_nums]:
        print(option)
    guess = input("Enter your guess(a,b,c,d): ")
    guesses.append(guess)
    if guess == answers[question_nums]:
        score += 1
        print("You guessed right!")
    else :
        print("Wrong Answer!")
        print(f"{answers[question_nums]} is Correct!")
    question_nums+=1

percentage = score/len(questions)*100
print("===============================")
print("            Results            ")
print(f"=======Your score is {percentage}====")
print("===============================")