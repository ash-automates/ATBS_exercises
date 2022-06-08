import pyinputplus as pyip, random, time

numOfQuestions = 10
correctAnswers = 0

for question in range(numOfQuestions):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    print(f"{num1} x {num2} = ?")
    try:
        res = pyip.inputStr(
            prompt="> ",
            allowRegexes=[r"^%s$" % (num1 * num2)],
            blockRegexes=[(".*", "Incorrect")],
            timeout=8,
            limit=3,
        )
    except pyip.TimeoutException:
        print("Out of time!")
    except pyip.RetryLimitException:
        print("You got 3 guesses wrong, moving on!")

    else:
        print("Correct!")
        correctAnswers += 1
        time.sleep(1)

print(f"Final score: {correctAnswers}/{numOfQuestions}.")
