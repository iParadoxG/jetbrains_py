import random, string
print("H A N G M A N")

def game(option):
  while option == "play":
    listy = ['java']
    ran = random.choice(listy)
    b = set()
    flag = "lose"
    life = 8
    print()
    while flag == "lose" and life > 0:
        temp = [ran[i] if (ran[i] in b) else "-" for i in range(len(ran))]
        joined = "".join(temp)
        if joined == ran:
          flag = "win"
          continue
        print(joined)
        tempb = input("Input a letter:")
        if not len(tempb) == 1:
          print("You should input a single letter\n")
          continue
        if tempb not in string.ascii_lowercase:
          print("It is not an ASCII lowercase letter\n")
          continue
        if tempb in b:
          print("You already typed this letter")
        elif tempb not in ran:
          print("No such letter in the word")
          life -=1
        b.add(tempb)
        if life == 0:
          print("You are hanged!")
          break
        print()
    else:
      print(joined)
      print("""\
    You guessed the word!
    You survived!""")
    print()
    option = input("Type \"play\" to play the game, \"exit\" to quit:")
option = input("Type \"play\" to play the game, \"exit\" to quit:")
game(option)
