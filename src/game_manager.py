from pygame.mixer import music

from constants import MENU_MUSIC

class GameManager:

    def __init__(self, menu, levels):
        self.menu = menu
        self.levels = list(levels)
        self.open_menu()

    def update(self, elapsed_time):
        self.current_panel.update(elapsed_time)
        self.current_panel.draw()

    def reset_level(self):
        pass

    def open_menu(self):
        self.current_panel = self.menu
        music.load(MENU_MUSIC)
        music.play(-1)