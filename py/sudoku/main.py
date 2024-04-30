import os

class Board:
    # 2d array to store numbers
    current = [ [0]*9 for i in range(9) ]
    # first indice = column
    # second = row
    # 0 = empty
 
    # initialisation
    def __init__(self):
        self.current = [ # random sudoku
            [0,1,0,8,0,0,9,0,0],
            [0,2,9,0,0,5,3,7,0],
            [0,6,0,0,2,4,1,0,5],
            [7,5,0,0,3,0,0,9,0],
            [6,9,3,5,0,0,0,0,0],
            [4,8,0,6,0,0,7,5,3],
            [0,0,6,4,8,0,5,0,0],
            [0,0,8,7,0,2,6,4,9],
            [0,0,0,0,0,0,0,2,0]
        ]

        self.solution = [
            [5,1,4,8,7,3,9,6,2],
            [8,2,9,1,6,5,3,7,4],
            [3,6,7,9,2,4,1,8,5],
            [7,5,1,2,3,8,4,9,6],
            [6,9,3,5,4,7,2,1,8],
            [4,8,2,6,9,1,7,5,3],
            [2,7,6,4,8,9,5,3,1],
            [1,3,8,7,5,2,6,4,9],
            [9,4,5,3,1,6,8,2,7]
        ]
 
    # get specific tile
    def get_tile(self, x, y, against):
        return against[x][y]
 
    # get 3x3 square
    def get_square(self, x, y, against): 
        # need to use coords of last item in square
        # e.g. 2,2 or 5,5
        out = [row[x-2:x+1] for row in against][x-2:y+1]
        return out
 
    # get specific row
    def get_row(self, y, against):
        out = against[y:y+1][0]
        return out
 
    # get specific column
    def get_column(self, x, against):
        out = [n[0] for n in [row[x:x+1] for row in against]]
        return out

    def print_board(self):
        s = ""
        for i in range(0,len(self.current)):
            si = ""
            for j in self.get_row(i,self.current):
                s += " "+str(j)
            s += si+"\n"
        print(s)

    # place a number
    def place_num(self, x, y, n):
        # 0 = ok
        # 1 = invalid
        # 2 = wrong
        if self.get_tile(x,y,self.current) != 0: return 1
        elif n in self.get_column(x,self.current): return 1
        elif n in self.get_row(y,self.current): return 1
        elif n in self.get_square((x%3+2), (y%3+2), self.current): return 1
        elif self.get_tile(x,y,self.solution) != n: 
            return 2
        else: 
            self.current[x][y] = n
            return 0

b = Board()

# print(b.get_tile(0,0))
# print(b.get_tile(2,1))
# print(b.get_square(2,2))
# print(b.get_row(1))
#print(b.get_column(0, b.solution))

#print(b.get_tile(0,0,b.solution))
#b.print_board()
#print(b.place_num(0,0,5))
#b.print_board()

res = 0

while b.current != b.solution:
    os.system("cls" if os.name == "nt" else "clear")
    
    if (res == 1): print("invalid")
    elif (res == 2): print("incorrect")

    b.print_board()
    x = int(input("column: "))
    y = int(input("row: "))
    n = int(input("number: "))

    res = b.place_num(x-1, y-1, n)