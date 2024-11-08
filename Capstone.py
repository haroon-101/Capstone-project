import random


def results(names, score):
    i = 1
    final_leaderboard = sorted(zip(names, score), key=lambda x: x[1], reverse=True)
    for player, result in final_leaderboard:
        print(f"{i}. {player} - {result:.2f}%")
        i += 1


def get_name():
    while True:
        name = input("Please enter your name: ").strip()
        if name:
            return name


def get_level():
    while True:
        try:
            lev = int(input("Level: "))
            if lev in [1, 2, 3]:
                return lev
            else:
                raise ValueError
        except ValueError:
            pass
        

def generate_integer(level):
    if level == 1:
        x = random.randint(1, 9)
        y = random.randint(1, 9)
    elif level == 2:
        x = random.randint(1, 99)
        y = random.randint(1, 99)
    elif level == 3:
        x = random.randint(1, 999)
        y = random.randint(1, 999)
    return x, y


def answer(questions, op, x, y):
    while True:
        q = input(f"Question {questions}:\n{x} {op} {y} = ")
        if q.strip() == "" or (not q.isdigit() and q[0] != "-"):
            pass
        else:
            break
    return int(q)


def sol(x, y, op):
    if op == "+":
        solution = x + y
    else:
        solution = x - y
    return solution


def final_score(score):
    f_score = 10 * score
    print(f"Score: {f_score:.2f}%")


def problem(level):
    questions = 1
    score = 0
    while questions <= 10:
        try:
            op = random.choice(["+", "-"])
            x, y = generate_integer(level)
            solution = sol(x, y, op)
            q = answer(questions, op, x, y)
            if q == solution:
                questions += 1
                score += 1
            else:
                times = 1
                while times < 2:
                    penalty = 0.5
                    print("Incorrect")
                    q = answer(questions, op, x, y)
                    if q != solution:
                        times += 1
                    else:
                        score += penalty
                        break
                if times == 2:
                    print(f"{x} {op} {y} = {solution}\n")
                questions += 1
        except ValueError:
            pass
    final_score(score)
    return score


def main():
    leaderboard = []
    names = []
    print("Welcome to my maths game.\nYou can choose from 3 levels. "
          "You have to answer 10 questions, and you have 2 attempts to answer every question. Good luck!\n")
    while True:
        name = get_name()
        names.append(name)
        level = get_level()
        score = problem(level)
        leaderboard.append(score * 10)
        again = input("Do you want to play again? ").strip().lower()
        if again.startswith("y"):
            pass
        else:
            break
    print("\nLEADERBOARD:")
    results(names, leaderboard)
    print("\nThanks for playing!")


if __name__ == "__main__":
    main()
