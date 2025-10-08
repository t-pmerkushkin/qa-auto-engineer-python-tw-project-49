from random import randint

def brain_progression():
    name = input("May I have your name? ")
    correct_rounds = 0
    print(f"Hello, {name}!")
    print('What number is missing in this progression?')
    while correct_rounds < 3:
        start = randint(1, 10)
        step = randint(1, 5)
        length = 5
        hidden_index = randint(0, length - 1)
        progression = [start + step * i for i in range(length)]
        correct = progression[hidden_index]
        progression[hidden_index] = '..'
        print(f"Question: {progression}")
        user_answer = int(input('Your answer: ').strip())
        if user_answer == correct:
            correct_rounds += 1
            print('Correct')
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {correct}. Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


def main():
    brain_progression()

if __name__ == '__main__':
    main()