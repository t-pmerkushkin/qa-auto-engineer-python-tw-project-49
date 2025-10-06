from random import randint


def is_even(num):
    return num % 2 == 0

def even_odd_game():
    correct = 0
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Answer 'yes' if number even otherwise answer 'no'.")
    while correct < 3:
        num = randint(1, 20)
        print(f"Question: {num}")
        user_answer = input("Your answer: ").strip().lower()
        if (is_even(num) and user_answer.strip().lower() == 'yes') or (
                not is_even(num) and user_answer.strip().lower() == 'no'):
            correct += 1
            print('Correct!')


        else:
            print(
                f"{user_answer} is wrong answer ;(. Correct answer was {'yes' if is_even(num) else 'no'}.\nLet's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

def main():
    even_odd_game()

if __name__ == '__main__':
    main()