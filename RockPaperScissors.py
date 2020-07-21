# Write your code here
import random
class RPC:
    user_input = ''
    name = ''
    score = 0
    def get_score(self, name):
        with open('rating.txt', 'r') as file:
            for line in file:
                if name == line.split()[0]:
                    self.score = int(line.split()[1])
    def user(self):
        self.name = input('Enter your name: ')
        print(f'Hello, {self.name}')
        self.get_score(self.name)
    def game(self):
        choices = input().split(',')
        print("Okay, let's start")
        if choices == ['']:
            choices = ['rock', 'paper', 'scissors']
            while self.user_input != '!exit':
                self.user_input = input()
                if self.user_input == '!exit':
                    continue
                if self.user_input == '!rating':
                    print(self.score)
                    continue
                if self.user_input not in choices:
                    print('Invalid input')
                    continue
                win_dict = {"rock":"paper", "paper":"scissors", "scissors":"rock"}
                comp_choice = random.choice(choices)
                if win_dict[self.user_input] == comp_choice:
                    print(f'Sorry, but computer chose {comp_choice}')
                if win_dict[comp_choice] == self.user_input:
                    self.score += 100
                    print(f'Well done. Computer chose {comp_choice} and failed')
                elif comp_choice == self.user_input:
                    self.score += 50
                    print(f'There is a draw ({comp_choice})')
        else:
            while self.user_input != '!exit':
                self.user_input = input()
                if self.user_input == '!exit':
                    continue
                if self.user_input == '!rating':
                    print(self.score)
                    continue
                if self.user_input not in choices:
                    print('Invalid input')
                    continue
                comp_choice = random.choice(choices)
                lose_list = []
                win_list =[]
                if choices.index(self.user_input) > len(choices) // 2:
                    for i in range(1, (len(choices) // 2) + 1):
                        lose_list.append(choices[choices.index(self.user_input) - i])
                    for a in choices:
                        if a not in lose_list:
                            win_list.append(a)
                    win_list.remove(self.user_input)
                else:
                    for i in range(1, (len(choices) // 2) + 1):
                        win_list.append(choices[choices.index(self.user_input) + i])
                    for a in choices:
                        if a not in win_list:
                            lose_list.append(a)
                    lose_list.remove(self.user_input)
                if comp_choice == self.user_input:
                    self.score += 50
                    print(f'There is a draw ({comp_choice})')          
                elif comp_choice in win_list:
                    print(f'Sorry, but computer chose {comp_choice}')
                elif comp_choice in lose_list:
                    self.score += 100
                    print(f'Well done. Computer chose {comp_choice} and failed')

        print('Bye!')
a1 = RPC()
a1.user()
a1.game()
