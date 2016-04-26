import sys
sys.path.insert(1,'/home/luiz/Projects/Checkers/scripts/classes')
sys.path.insert(1,'/home/luiz/Projects/Checkers/scripts/game')
import game_board, piece, position, track, start
import pygame
from pygame.locals import *




class MainInterface(object):
    def __init__(self, sreen_size, tab):
        pygame.init()
        self.screen = pygame.display.set_mode(sreen_size)
        self.tab = tab
        self.rects = []
        self.rect_width = 75
        self.circle_width = 36
        self.get_rects()
        self.event()

    def get_rects(self):
        self.rects = []
        for line in range(len(tab)):
            for column in range(len(tab[0])):
                tab[line][column].rect = pygame.Rect((column * self.rect_width, line * self.rect_width), (self.rect_width, self.rect_width))
                self.rects.append([tab[line][column].rect, tab[line][column]])
                if tab[line][column].is_occupied():
                    piece_color = (252,43,106)
                    if tab[line][column].occupation.player.number == 1:
                        piece_color = (64,101,125)
                    tab[line][column].piece_circle = (self.screen, piece_color, ((self.rect_width * column) + self.circle_width, (self.rect_width * line) + self.circle_width), 30)

    def show_rects(self):
        self.get_rects()
        for rect in self.rects:
            color = (0, 0, 0)
            if rect[1].color == "white":
                color = (255, 255, 255)
            if rect[1].clicked:
                color = (230, 120, 230)
            pygame.draw.rect(self.screen, color, rect[0])
            if rect[1].piece_circle:
                a = rect[1].piece_circle
                pygame.draw.circle(a[0], a[1], a[2], a[3])

    def move_piece(self):
        self.clicked.occupation.move(self.destiny, self.tab)
        self.clicked = []
        self.destiny = []






    def event (self):
        self.done = False
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        self.done = True
                if event.type == MOUSEBUTTONDOWN:
                    try:
                        self.tab[int(pos[1] / self.rect_width)][int(pos[0] / self.rect_width)].clicked = False
                        self.clicked = self.tab[int(pos[1] / self.rect_width)][int(pos[0] / self.rect_width)]
                    except: pass
                    pos = pygame.mouse.get_pos()
                    if self.tab[int(pos[1] / self.rect_width)][int(pos[0] / self.rect_width)].color != "white":
                        self.tab[int(pos[1] / self.rect_width)][int(pos[0] / self.rect_width)].clicked = True
                        self.clicked_pos = self.tab[int(pos[1] / self.rect_width)][int(pos[0] / self.rect_width)]
                        self.destiny = self.clicked_pos
                if event.type == KEYDOWN:
                    if event.key == "K_ESCAPE":
                        pygame.QUIT
                        self.done = True
            
            self.screen.fill((255,0,0))
            self.show_rects()

            try:self.move_piece()
            except: pass

            pygame.display.flip()
            

tab = game_board.Board()
start.set_pieces(tab)
tela = MainInterface((620,620), tab)

