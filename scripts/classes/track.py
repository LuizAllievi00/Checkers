class Track(object):

    def __init__(self, start, destiny):
        self.start = start.localization
        self.destiny = destiny.localization
        self.track_list = []
        self.set_track_list()

    def set_track_list(self):
        if self.start[0] < self.destiny[0]:
            if self.start[1] < self.destiny[1]:
                x_step = 1
                y_step = 1
            else:
                x_step = 1
                y_step = -1
        else:
            if self.start[1] < self.destiny[1]:
                x_step = -1
                y_step = 1
            else:
                x_step = -1
                y_step = -1
        for x, y in zip(range(self.start[0] + x_step, self.destiny[0] + x_step, x_step), range(self.start[1] + y_step, self.destiny[1] + y_step, y_step)):
            print(x,y)
            self.track_list.append([x,y])
            print(self.track_list)


    def get_track(self):
        return self.track_list

    def __str__(self):
        string = 'Track \n'
        for item in self.track_list:
            string += item + " "
        return string

