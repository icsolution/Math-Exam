import random


class Exam:

    def __init__(self):
        self.result = None
        self.guess = None
        self.log = []
        self.start()

    def start(self):
        level_1 = 1, 'simple operations with numbers 2-9'
        level_2 = 2, 'integral squares of 11-29'
        print('Which level do you want? Enter a number:')
        print(f'{level_1[0]} - {level_1[1]}')
        print(f'{level_2[0]} - {level_2[1]}')
        choice = input()
        if choice == '1':
            self.test(choice, level_1)
        elif choice == '2':
            self.test(choice, level_2)
        else:
            print('Incorrect format.')
            self.start()

    def level_1(self):
        number = random.choices([str(number) for number in range(2, 10)], k=2)
        operation = random.choice(['+', '-', '*'])
        equation = f'{number[0]} {operation} {number[1]}'
        self.result = eval(equation)
        print(equation)

    def level_2(self):
        number = random.randrange(11, 30)
        self.result = number ** 2
        print(number)

    def test(self, choice, level):
        tests = 0
        score = 0
        while tests < 5:
            if choice == '1':
                self.level_1()
            elif choice == '2':
                self.level_2()
            self.check_input()
            if self.guess == self.result:
                print('Right!')
                score += 1
            else:
                print('Wrong!')
            tests += 1
            self.log.append(f'User: {tests}/5 in Level {level[0]} ({level[1]})')
        self.log_result(score, tests)

    def check_input(self):
        guess = input()
        try:
            self.guess = int(guess)
        except ValueError:
            print('Incorrect format.')
            self.check_input()

    def log_result(self, score, tests):
        save = input(f'Your mark is {score}/{tests}. Would you like to save the result? Enter yes or no.\n')
        if save.lower() == 'yes' or save.lower() == 'y':
            name = input('What is your name?\n')
            summary = '\n'.join(self.log).replace('User', name)
            with open('results.txt', 'a+') as file:
                file.write(summary)
            print('The results are saved in "results.txt".')
            quit()
        else:
            quit()


Exam()
