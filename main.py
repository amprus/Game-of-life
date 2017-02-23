# main.py
#
# Includes main logic for the Conway's game of life


import pygame


class GameOfLife:
    WIDTH = 640

    def __init__(self):
        self._screen = None
        self._running = False

        # Game objects

    def on_init(self):
        pygame.init()
        self._screen = pygame.display.set_mode((GameOfLife.WIDTH, GameOfLife.WIDTH))
        self._running = True

    def on_cleanup(self):
        pygame.quit()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_update(self):
        pass

    def on_render(self):
        pygame.display.flip()

    def on_execute(self):
        self.on_init()
        try:
            while self._running:
                for event in pygame.event.get():
                    self.on_event(event=event)
                self.on_update()
                self.on_render()
        except Exception as e:
            print(e)
        finally:
            self.on_cleanup()


def main():
    gol = GameOfLife()
    gol.on_execute()


if __name__ == '__main__':
    main()
