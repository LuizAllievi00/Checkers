from track import Track
class Piece(object):

    def __init__(self, position, player):
        self.position = position
        self.player = player
        self.is_piece = False
        self.is_position = False

    def move(self, destiny, tab):

        try:
            track = Track(self.position, destiny)
            track = track.get_track()
            if len(track) > 1:
                for item in track:
                    #checking if there is more than a position consecutively
                    try:
                        if not tab[item[0]][item[1]].is_occupied() and free: return False
                        if not tab[item[0]][item[1]].is_occupied(): free = True
                        else: free = False
                    except: pass

            for item in track:
                #checking if there's a piece of the same player in track
                 try:
                     if tab[item[0]][item[1]].occupation.player == self.player: return False
                 except:
                    pass
            for item in track:
                #checking if there's two pieces consecutively
                try:
                    if tab[item[0]][item[1]].is_occupied() and occupied_1: return False
                    if tab[item[0]][item[1]].is_occupied():
                        occupied_1 = True
                    else:
                        occupied_1 = False
                except:
                    pass
            if tab[track[-1][0]][track[-1][1]].is_occupied(): return False
            for item in track:
                if not tab[item[0]][item[1]].is_occupied():
                    #goes here if the actual position in free and set the last position as free
                    self.is_position = True
                else:
                    #here set the last position as occupied
                    self.is_piece = True

                if self.is_position:
                    if self.is_piece:
                        self.is_position = False
                        self.is_piece = False
                        index = track.index(item) - 1
                        tab[track[index][0]][track[index][1]].occupation = []
                        tab[track[index][0]][track[index][1]].piece_circle = []
                        self.position.occupation = []
                        self.position.piece_circle = []
                        tab[item[0]][item[1]].occupation = self
                        self.position = tab[item[0]][item[1]]
                    else:
                        self.is_position = False
                        self.position.occupation = []
                        self.position.piece_circle = []
                        tab[item[0]][item[1]].occupation = self
                        self.position = tab[item[0]][item[1]]
        except:
            return False


    def __str__(self):
        return "Piece : %s " % self.player

