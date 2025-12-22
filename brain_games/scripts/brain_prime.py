from math import sqrt
from secrets import choice


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def brain_prime():
    name = input("May I have your name? ")
    correct_rounds = 0
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")
    while correct_rounds < 3:
        n = choice(range(1, 100))
        correct_answer = 'yes' if is_prime(n) else 'no'
        print(f"Question: {n}")
        user_answer = input("Your answer: ")
        if ((user_answer == "yes" and is_prime(n))
                or (user_answer == "no" and not is_prime(n))):
            correct_rounds += 1
            print('Correct')
        else:
            print(f"""'{user_answer}' is wrong answer ;(. 
            \nCorrect answer was '{correct_answer}'.
            \nLet's try again, {name}!""")
            return
    print(f"Congratulations, {name}!")


def main():
    brain_prime()


if __name__ == '__main__':
    main()
