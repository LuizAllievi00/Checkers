from track import Track
class Piece(object):

    def __init__(self, position, player):
        self.position = position
        self.player = player
        self.last_piece = False
        self.last_position = False

    def move(self, destiny, tab):
        """
        try:
            for item in track:
                if not tab[item[0]][item[1]].isoccupied():
                    self.last_piece = False
                    self.last_position = True
                else:
                    self.last_position = False
                    self.last_piece = True
                if self.last_piece:
                    print("capture")
                    pass
                    #capture
                if self.last_position:
                    if not tab[item[0]][item[1]].isoccupied():
                        index = track.index(item) - 1
                        self.final_destiny = track[index]
                    else:
                        print("capture")
                        pass
                        #capture
                if self.final_destiny:
                    tab[self.final_destiny[0]][self.final_destiny[1]].occupation = self
                    self.position.occupation = []
                    self.position.piece_circle = []
                    self.position = tab[track[self.final_destiny][0]][self.final_destiny[1]]
                    return True

            return True
        except: return False
        """
        try:
            print(destiny)
            track = Track(self.position, destiny)
            track = track.get_track()
            tab[track[-1][0]][track[-1][1]].occupation = self
            self.position.occupation = []
            self.position.piece_circle = []
            self.position = tab[track[-1][0]][track[-1][1]]
            return True
        except:return False
        print(track.get_track())
    def __str__(self):
        return "Piece : %s " % self.player
