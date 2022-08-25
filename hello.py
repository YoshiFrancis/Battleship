import random 
class Yoshi: 
    def __init__(self, name, color, hobby):
        self.name = name
        self.color = color
        self.hobby = hobby
    
    def __str__(self):
        return f"{self.name}, {self.color}, {self.hobby}"

    
    def SayPhrase(self):
        print("Yoshi!")

    def SayHobby(self):
        print(f"I like {self.hobby} as something to do in my spare time")


Francis = Yoshi("Francis", "black", "learning")

class Battleship: 
    def __init__(self, x, y, ships):
        self.x = x
        self.y = y
        self.ships = ships
        self.board = []
        self.coords = {}
        self.miss = 0
        self.correct = 0

    def PrintBoard(self):
        copy = self.board[:]
        TmpBoard = ''
        for num in range(len(self.board)):    
            copy[num] = " ".join(copy[num])
            TmpBoard += copy[num] + '\n'
        print(TmpBoard.replace('x', 'O'))
        print((3, 2) == (3, 2))
        
    def CreatBoard(self):
        for number in range(self.y):
            self.board.append(["O"] * self.x)

        if self.ships > self.x * self.y:
            self.ships = 1

        i = 0
        while not i == self.ships:
            coordinate = (random.randrange(1, self.x + 1), random.randrange(1, self.y + 1))
            if self.board[coordinate[1] - 1][coordinate[0] - 1] == "x":
                continue
            self.board[coordinate[1] - 1][coordinate[0] - 1] = "x"
            self.coords[f'{i}'] = [coordinate, False]
            i += 1
            
        print(self.coords)

    def AskInput(self):
        while self.correct < self.ships and self.miss < 5:
            cancel = False
            print("Input your guess! \n")
            XGuess = int(input("X coordinate: "))
            YGuess = int(input("Y coordinate: "))
            print(f'({XGuess}, {YGuess}) was your guess!')
            for coord in self.coords:
                if (XGuess, YGuess) == self.coords[coord][0]:
                    self.coords[coord][1] = True
                    self.correct += 1
                    print("HIT!!!")
                    cancel = True
                    self.board[XGuess - 1][YGuess - 1] = "X"
                    break
            if not cancel:
                print("MISS!!!")
                self.miss += 1
            
            print(f'Correct: {self.correct} \nMisses: {self.miss} out of 5')
            self.PrintBoard()
        
        print(f'You got {self.correct} correct!')
            
                    
NewBoard = Battleship(10, 10, 5)
def main():
    NewBoard.CreatBoard()
    NewBoard.PrintBoard()
    NewBoard.AskInput()


if __name__=="__main__":
    main()