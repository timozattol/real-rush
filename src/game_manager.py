from pygame.mixer import music

from constants import MENU_MUSIC
from menu import Menu
from player import Player
from level_01 import Level01

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
        self.levels = [Level01(self.player, self.display)]

    def reset_level(self):
        curr_index = self.levels.index(self.current_panel)
        self.reset_levels()
        self.current_panel = self.levels[curr_index]

    def open_menu(self):
        self.current_panel = Menu(Player(), self.display)
        music.load(MENU_MUSIC)
        music.play(-1)

    def start_game(self):
        self.reset_levels()
        self.current_panel = self.levels[0]

    def mouse_left_click(self, cursor_pos):
        self.current_panel.mouse_left_click(cursor_pos, self)
