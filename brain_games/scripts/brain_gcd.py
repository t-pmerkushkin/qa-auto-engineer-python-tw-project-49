from math import gcd
from secrets import choice


def brain_gcd():
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")
    correct = 0
    while correct < 3:
        question = [choice(range(1, 100)), choice(range(1, 100))]
        print(f"Question: {question[0]} {question[1]}")
        user_answer = int(input('Your answer: '))
        result = gcd(question[0], question[1])
        try:
            if (question[0] % user_answer == 0
                    and question[1] % user_answer == 0):
                print('Correct')
                correct += 1
            else:
                print(f"""'{user_answer}' is wrong answer ;(. 
                \nCorrect answer was '{result}'.\nLet's try again, {name}!""")
                return
        except ValueError:
            print('Incorrect, you need enter a number')
            return
    print(f"Congratulations, {name}!")


def main():
    brain_gcd()


if __name__ == '__main__':
    main()