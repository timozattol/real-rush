from pygame.mixer import music

from constants import MENU_MUSIC, LEVEL1_MUSIC
from menu import Menu
from player import Player
from level_01 import Level01
from level_02 import Level02
from level_03 import Level03

class GameManager:

    def __init__(self, display):
        self.display = display
        self.reset_levels()
        self.menu = Menu(Player(), self.display)
        self.current_panel = None
        self.open_menu()

    def update(self, elapsed_time):
        self.current_panel.update(elapsed_time)
        self.current_panel.draw()

    def reset_levels(self):
        self.player = Player()
        self.levels = [Level01(self.player, self.display), Level02(self.player, self.display), Level03(self.player,self.display)]

    def reset_level(self):
        curr_index = self.levels.index(self.current_panel)
        self.reset_levels()
        self.current_panel = self.levels[curr_index]

    def open_menu(self):
        self.current_panel = Menu(Player(), self.display)
        self.current_panel.load_music()

    def start_game(self):
        self.reset_levels()
        self.current_panel = self.levels[0]
        self.current_panel.load_music()

    def next_level(self):
        curr_index = self.levels.index(self.current_panel)
        if curr_index+1 > len(self.levels)-1:
            self.open_menu()
        else: 
            self.current_panel = self.levels[curr_index+1]
            self.current_panel.load_music()

    def mouse_left_click(self, cursor_pos):
        self.current_panel.mouse_left_click(cursor_pos, self)
