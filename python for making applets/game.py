import pygame
from menu import *


class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 800, 600
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.COLOR, self.WHITE = (0, 100, 100), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        bg = pygame.image.load("Bondi/indoor.jpg")
        bg = pygame.transform.scale(bg, (100, 100))
        bg1 = pygame.image.load("Bondi/green.jpg")
        bg1 = pygame.transform.scale(bg1, (100, 100))
        bg2 = pygame.image.load("Bondi/sunflower.jpg")
        bg2 = pygame.transform.scale(bg2, (100, 100))
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.COLOR)
            self.draw_text("Food Garden", 10, self.DISPLAY_W / 2, 20)
            self.draw_text("Indoor", 10, 145, 220)
            self.draw_text("Green", 10, 550, 220)
            self.draw_text("Sunflower", 10, 350, 420)
            self.window.blit(self.display, (0, 0))
            self.window.blit(bg, (100, 100))
            self.window.blit(bg1, (500, 100))
            self.window.blit(bg2, (300, 300))
            pygame.display.update()
            self.reset_keys()



    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.SysFont('comicsans', 40)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)