game_state = list('_________')
game_matrix = [[game_state[j] for j in range(i, i + 3)] for i in range(0, 9, 3)]
rotated_matrix = [[game_state[i-j] for i in range(9, 2, -3)] for j in range(3,0,-1)]

print("---------")
for _ in range(3):
    print("| ", end="")
    for i in range(3):
        temp = game_state.pop(0)
        print(temp + " ", end="")
    print("|")
print("---------")

class tictactoe:
    x=0
    y=0
    flag = False
    pflag = False
    turnCounter = 0
    def getCo(self):
        try:
            self.x, self.y = map(int,input('Enter the coordinates: ').split())
        except ValueError:
            print("You should enter numbers!")
            return False
        if (0 < self.x <= 3) and (0 < self.y <= 3):
            self.checkPlace()
            return True
        else:
            print('Coordinates should be from 1 to 3!')
            return False
    def __init__(self):
        while not self.flag:
            self.flag = self.getCo()
    def checkPlace(self):
        if any(x in rotated_matrix[self.x - 1][self.y - 1] for x in ["X","O"]):
            print("This cell is occupied! Choose another one!")
            self.getCo()
        else:
            if self.turnCounter % 2 == 0:
                rotated_matrix[self.x - 1][self.y - 1] = "X"
            else:
                rotated_matrix[self.x - 1][self.y - 1] = "O"
            self.turnCounter += 1
            self.showState()
            self.pflag = self.checkState()
            if not self.pflag:
                self.__init__()
    def showState(self):
        print("---------")
        for i in range(2,-1,-1):
            print("| ", end="")
            for j in range(3):
                print(rotated_matrix[j][i] + " ", end="")
            print("|")
        print("---------")
    def checkState(self):
        rows=['','','']
        columns=['','','']
        diagonals=['','']
        for i in range(3):
            for j in range(3):
                rows[i] += rotated_matrix[i][j]
        for i in range(3):
            for j in range(3):
                columns[i] += rotated_matrix[j][i]
        for i in range(3):
            for j in range(3):
              if i==j:
                diagonals[0] += rotated_matrix[i][j]
        for i in range(3):
            for j in range(3):
              if i + j == 2:
                diagonals[1] += rotated_matrix[i][j]
        all_possible_results = rows + columns + diagonals
        if 'XXX' in all_possible_results:
            print('X wins')
            return True
        if 'OOO' in all_possible_results:
            print('O wins')
            return True
        if all('_' not in x for x in all_possible_results):
            print('Draw')
            return True
        return False
a1 = tictactoe()
