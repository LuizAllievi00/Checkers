from position import *

class Board(object):

    def __init__(self):
        super(Board, self).__init__()
        self.board = [[0 for i in range(8)] for i in range(8)]
        self.__create_positions__()


    def __create_positions__(self):

        for item in range(0, 8):
            for i in range(0, 8):
                if (item + i) % 2 == 0:
                    self.board[item][i] = Position((item, i), "white")
                else:
                    self.board[item][i] = Position((item, i), "black")

    def __getitem__(self, index):
        return self.board[index]


    def __str__(self):
        string = ""
        for line in range(0,8):
            for column in range(0,8):
                string += self.board[line][column].color +  "  "
            string += "\n"
        return string

    def __len__(self):
        return len(self.board)

    def reset_clicked(self):
        for line in self.board:
            for elem in line:
                elem.clicked = False