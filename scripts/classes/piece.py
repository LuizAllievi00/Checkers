from track import Track
class Piece(object):

    def __init__(self, position, player):
        self.position = position
        self.player = player

    def move(self, destiny, tab):
        track = Track(self.position, destiny)
        for item in track:

            if not tab[item[0]][item[1]].isoccupied():

        print(track.get_track())
    def __str__(self):
        return "Piece : %s " % self.player
