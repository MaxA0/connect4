class connect4:
    def __init__(self):
        self.go = 1
        self.row = []
        for i in range(6):
            self.row.append(["x","x","x","x","x","x","x"])
        self.turn()

    def turn(self):
        column = int(input("Which column would you like to put it in?"))
        column -=1
        empty = -1
        for i in range(6):
            if self.row[i][column] == "x":
                empty = i
                break
        if empty == -1:
            print("not valid!")
            self.turn()
        else:
            if self.go == 1:
                self.row[empty][column] = "z"
                self.go = 0
            else:
                self.row[empty][column] = "y"
                self.go =1
        self.output()
        check = self.checkw()
        if check == None:
            self.turn()
        else:
            print(f"player {check} won!")
        self.turn()
    
    def checkw(self):
        checks = [self.diagleft, self.diagright, self.horwin, self.verwin]
        for i in range(len(checks)):
            if checks[i]() != None:
                return checks[i]()
        return None
        
    def horwin(self):
        for i in range(len(self.row)):
            z=0
            y=0
            for j in range(len(self.row[i])):
                if self.row[i][j] == "z":
                    z+=1
                    y = 0
                elif self.row[i][j] == "y":
                    y+=1
                    z=0
                if z==4:
                    return("z")
                if y==4:
                    return("y")
        return None

    def verwin(self):
        for i in range(len(self.row[0])):
            z = 0
            y = 0
            for j in range(len(self.row)):
                if self.row[j][i] == "z":
                    z+=1
                    y =0
                elif self.row[j][i] =="y":
                    y+=1
                if z==4:
                    return("z")
                if y==4:
                    return("y")
        return None


    def diagright(self):
        for z in range(3):
            y = z
            for i in range(len(self.row[0])):
                x = i
                keyi = 1
                start = self.row[y][x]
                
                if (start == "x"):
                    continue
                while True: 
                    try:
                        if self.row[y+1][x+1] == start:
                            keyi+=1
                        else:
                            start = self.row[y+1][x+1]
                        x+=1
                        y+=1
                        if ((keyi == 4) and (start != "x")):
                            return start
                    except:
                        break
        return None
                    
    
    def diagleft(self):
        for z in range(3):
            y=z
            for i in range(len(self.row[0])-1, -1, -1):
                x = i
                keyi = 1
                start = self.row[y][x]
                if (start == "x"):
                    continue
                while True: 
                    try:
                        if self.row[y+1][x-1] == start:
                            keyi+=1
                        else:
                            start = self.row[y+1][x-1]
                        x-=1
                        y+=1
                        if ((keyi == 4) and (start != "x")):
                            return start
                    except:
                        break
        return None
        
    def output(self):
        for i in range(6):
            print(self.row[5-i])

game = connect4()
