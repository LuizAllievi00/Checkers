class Position(object):

    def __init__(self, localization, color):
        self.occupation = []
        self.localization = (localization[0], localization[1])
        self.color = color
        self.rect = []
        self.piece_circle = []
        self.clicked = False

    def get_near(self, tab):
        self.set_near(tab)
        string = ""
        for pos in self.near:
            string += str(pos) + "\n"
        return string

    def set_near(self, tab):

        base = [
            (self.localization[0] - 1, self.localization[1] - 1),
            (self.localization[0] - 1, self.localization[1] + 1),
            (self.localization[0] + 1, self.localization[1] - 1),
            (self.localization[0] + 1, self.localization[1] + 1)
        ]

        if (self.localization[0] == 0 and self.localization[1] == 0):
            self.near = [tab[base[3][0]][base[3][1]]]
            return 0

        if (self.localization[0] == 7 and self.localization[1] == 0):
            self.near = [tab[base[1][0]][base[1][1]]]
            return 0

        if (self.localization[0] == 0 and self.localization[1] == 7):
            self.near = [tab[base[2][0]][base[2][1]]]
            return 0

        if (self.localization[0] == 7 and self.localization[1] == 7):
            self.near = [tab[base[0][0]][base[0][1]]]
            return 0

        if (self.localization[0] == 7):
            self.near = [tab[base[0][0]][base[0][1]], tab[base[1][0]][base[1][1]]]
            return 0

        if (self.localization[0] == 0):
            self.near = [tab[base[2][0]][base[2][1]], tab[base[3][0]][base[3][1]]]
            return 0

        if (self.localization[1] == 0):
            self.near = [tab[base[0][0]][base[0][1]], tab[base[2][0]][base[2][1]]]
            return 0

        if (self.localization == 7):
            self.near = [tab[base[3][0]][base[3][1]], tab[base[1][0]][base[1][1]]]
            return 0



        self.near = [tab[base[0][0]][base[0][1]], tab[base[1][0]][base[1][1]], tab[base[2][0]][base[2][1]], tab[base[3][0]][base[3][1]]]
        return 0

    def get_draw(self):
        if not self.is_occupied():
            if self.color == "white":
                return "[ ]"
            else:
               return "[|]"
        if self.is_occupied():
            return "[O]"

    def is_occupied(self):
        if (self.occupation):
            return True
        return False

    def insert_piece(self, piece):
        self.piece = piece

    def delete_piece(self):
        self.piece = []

    def __str__(self):
        return "Line: %d | Column: %d | Ocupation: %s | Color: %s" % (self.localization[0], self.localization[1], self.occupation, self.color)