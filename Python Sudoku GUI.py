from tkinter import *
from tkinter import ttk
from Sudoku_Checker import solved


class Sudoku(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, borderwidth = 5)
        self.pack()

        temp = [9]*9
        for row in problem:
            for col in row:
                if col != -1 and col != 0:
                    temp[col-1] -= 1
        self.numbersLeft = temp
        print(self.numbersLeft)

        self.create_widgets()

    def create_widgets(self):
        for vr in range(9):
            for hr in range(9):
                if problem[vr][hr] != 0:
                    if (vr//3+hr//3)%2 == 0:
                        label = ttk.Label(self, text = problem[vr][hr], width = 4, relief = "groove") #flat, groove, raised, ridge, solid, or sunken
                    else:
                        label = ttk.Label(self, text = problem[vr][hr], width = 4, relief = "groove", background = "#bdbdbd")
                    label.grid(column = hr, row = vr, sticky = (N,W,E,S))
                    label.configure(anchor = "center")
                else:
                    button = ttk.Button(self, width = 4)
                    button.bind("<Button-1>", self.selectBtn)
                    button.grid(column = hr, row = vr, sticky = (N, W, E, S))

        col = 9
        for h in range(9):
            label = ttk.Label(self, width = 5)
            label.grid(column = col, row = h, sticky = (N,W,E,S))

        col += 1
        for h in range(9):
            label = ttk.Label(self, text = h+1 , width = 3)
            label.grid(column = col, row = h, sticky = (N,W,E,S))

        col += 1
        for h in range(1,10):
            button = ttk.Button(self, textvariable = self.numbersLeft[h-1], width = 3)
            button.grid(column = col, row = h-1, sticky = (N,W,E,S))

    def selectBtn(self, event):
        global valueentry
        global problem
        name = event.widget["text"]
        temp = valueentry.get()
        try:
            temp = int(temp)
            if 1 <= temp <= 9:
                event.widget["text"] = temp
                print(event.widget["text"])
                print(dir(event))
                print(int(event.grid["row"]), int(event.grid["column"]))
                print("hi")
                problem[int(event.widget["row"])][int(event.widget["column"])] = temp
        except TypeError:
            pass


class SudokuApp(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, borderwidth = 10)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        sudokuInfo = ttk.Frame(self)
        sudokuInfo.pack()

        timerlabel = ttk.Label(sudokuInfo, text = "Time : ")
        timerlabel.pack(side = "left")
        timerentry = ttk.Entry(sudokuInfo)
        timerentry.pack(side = "left")
        valuelabel = ttk.Label(sudokuInfo, text = "\tValue : ")
        valuelabel.pack(side = "left")
        global valueentry
        valueentry = ttk.Entry(sudokuInfo)
        valueentry.pack(side = "left")

        checkBtn = ttk.Button(sudokuInfo, text = "Check Answer")
        checkBtn.bind("<Button-1>", self.checkAns)
        checkBtn.pack(side = "bottom")

        Sudoku(self)

    def checkAns(self,event):
        global problem
        if solved(problem):
            print("Done")
        else:
            print("Wrong answer / incomplete")
        for a in problem:
            print(a)


def use_Example():
    # problem = [[0, 2, 0, 5, 0, 1, 0, 9, 0],
    #            [8, 0, 0, 2, 0, 3, 0, 0, 6],
    #            [0, 3, 0, 0, 6, 0, 0, 7, 0],
    #            [0, 0, 1, 0, 0, 0, 6, 0, 0],
    #            [5, 4, 0, 0, 0, 0, 0, 1, 9],
    #            [0, 0, 2, 0, 0, 0, 7, 0, 0],
    #            [0, 9, 0, 0, 3, 0, 0, 8, 0],
    #            [2, 0, 0, 8, 0, 4, 0, 0, 7],
    #            [0, 1, 0, 9, 0, 7, 0, 6, 0]]
    problem = []
    file = open("Example_easy_2.txt", "r")
    for line in file:
        problem.append(list(map(int, line.split())))
    print(problem)
    return problem

def use_Solution():
    problem = [[4, 2, 6, 5, 7, 1, 3, 9, 8],
               [8, 5, 7, 2, 9, 3, 1, 4, 6],
               [1, 3, 9, 4, 6, 8, 2, 7, 5],
               [9, 7, 1, 3, 8, 5, 6, 2, 4],
               [5, 4, 3, 7, 2, 6, 8, 1, 9],
               [6, 8, 2, 1, 4, 9, 7, 5, 3],
               [7, 9, 4, 6, 3, 2, 5, 8, 1],
               [2, 6, 5, 8, 1, 4, 9, 3, 7],
               [3, 1, 8, 9, 5, 7, 4, 6, 2]]
    return problem


if __name__ == "__main__":
    # problem = use_Solution()
    problem = use_Example()

    master = Tk()
    master.title("Python Sudoku")
    SudokuApp(master)
    master.geometry("600x400")
    master.mainloop()