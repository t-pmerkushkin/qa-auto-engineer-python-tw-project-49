from secrets import choice


def brain_calc():
    correct = 0
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")
    while correct < 3:
        num1, num2 = choice(range(1, 100)), choice(range(1, 100))
        if num2 > num1:
            num1, num2 = num2, num1
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
        }
        operation = choice(list(operations.keys()))
        result = operations[operation](num1, num2)
        print(f"Question: {num1} {operation} {num2}")
        try:
            user_answer = int(input('Your answer: '))
            if user_answer == result:
                correct += 1
                print('Correct')
            else:
                print(f"""'{user_answer}' is wrong answer ;(. 
                \nCorrect answer was '{result}'.\nLet's try again, {name}!""")
                return
        except ValueError:
            print('Incorrect, you need enter a number')
            return
    print(f"Congratulations, {name}!")


def main():
    brain_calc()


if __name__ == '__main__':
    main()