class CoffeeMachine():
    water = 0
    milk = 0
    beans = 0
    cups = 0
    money = 0
    n_machine = 0
    def __next__(cls):
        if cls.n_machine == 0:
            cls.n_machine += 1
            return object.__new__(cls)
        return None

    def __init__(self, water, milk, beans, cups, money):
        self.cups = cups
        self.beans = beans
        self.milk = milk
        self.money = money
        self.water = water

    def out(self):
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.beans) + " of coffee beans")
        print(str(self.cups) + " of disposable cups")
        print(str(self.money) + " of money")

    def take(self):
        print("I gave you $" + str(self.money))
        self.money = 0

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))

    def transaction(self, money, water = 0, milk = 0, beans = 0):
        bap = min(self.water - water, self.beans - beans, self.milk - milk, self.cups)
        if bap > 0:
            print("I have enough resources, making you a coffee!")
            self.cups -= 1
            self.water -= water
            self.milk -= milk
            self.beans -= beans
            self.money += money
        else:
            if self.water < water:
                print("Sorry, not enough water!")
            if self.beans < beans:
                print("Sorry, not enough coffee beans!")
            if self.milk < milk:
                print("Sorry, not enough milk!")
            if self.cups <= 0:
                print("Sorry, not enough cups!")

flag = "place"
cf1 = CoffeeMachine(400, 540, 120, 9, 550)
while flag != "exit":
    flag=input("Write action (buy, fill, take, remaining, exit):")
    if flag == "take":
        cf1.take();
    elif flag == "fill":
        cf1.fill()
    elif flag == "buy":
        opt = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if opt == '1':
            cf1.transaction(4, water = 250, beans = 16)
        elif opt == '2':
            cf1.transaction(7, water = 350, milk = 75, beans=20)
        elif opt == '3':
            cf1.transaction(6, water = 200, milk = 100, beans=12)
        elif opt == "back":
            continue
    elif flag == "remaining":
        cf1.out()
