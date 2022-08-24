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

    def PrintBoard(self):
        print(self.board)
        
        
    def CreatBoard(self):
        for number in range(self.y):
            self.board.append(["O"] * self.x)

        if self.ships > self.x * self.y:
            self.ships = 1
        i = 0
        while not i == self.ships:
            coordinate = (random.randrange(self.x), random.randrange(self.y))
            print(coordinate)
            if self.board[coordinate[1]][coordinate[0]] == "X":
                continue
            self.board[coordinate[1]][coordinate[0]] = "X"
            i += 1
            

NewBoard = Battleship(5, 5, 5)
def main():
    NewBoard.CreatBoard()
    NewBoard.PrintBoard()


if __name__=="__main__":
    main()