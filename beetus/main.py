# #
# beetus/main.py : game loop for Beetus
# #
import sys
import logging
import asyncio
import pygame
import pygame.locals as plocals
from beetus.params import GameParams


logging.basicConfig(level=logging.INFO)


class BeetusGame:
    """Main game class
    """

    def __init__(self, game_params: GameParams):
        self.game_params = game_params
        # Initialize screen
        self.screen = pygame.display.set_mode(
            (self.game_params.screen_width, self.game_params.screen_height))
        # Initialize caption
        pygame.display.set_caption(self.game_params.title)
        # Initialize clock
        self.clock = pygame.time.Clock()
        self.running = True

    def setup_bg(self):
        """Setup background
        """
        # Fill background
        self.background: pygame.Surface = pygame.Surface(
            self.screen.get_size())  # type: ignore
        self.background: pygame.Surface = \
            self.background.convert()  # type: ignore
        self.background.fill(self.game_params.bg_color)

    def display_text(
        self,
        input_text: str,
        position: tuple,
        font_size: int = 36,
        color: tuple = (255, 255, 255)
    ):
        """Display text on the screen
        """
        font = pygame.font.Font(None, font_size)
        text = font.render(input_text, 1, color)
        textpos = text.get_rect()
        # move to position
        textpos.centerx = self.background.get_rect().centerx + position[0]
        textpos.centery = self.background.get_rect().centery + position[1]
        self.background.blit(text, textpos)

    def setup(self):
        """Setup game elements
        """
        self.setup_bg()
        self.display_text("Welcome to Beetus!", (0, -50), font_size=48)
        self.display_text("Press any key to start", (0, 50), font_size=36)

    async def _blit_everything(self):
        """Blit everything to the screen
        """
        # Blit everything to the screen
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
        await asyncio.sleep(0)

    async def run(self):
        """Main game loop
        """
        self.setup()  # Setup game elements
        await self._blit_everything()  # Initial blit
        logging.info("Starting main game loop.")
        while self.running:
            self.clock.tick(self.game_params.fps)
            print(pygame.event.get())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    logging.info("Quit event detected. Exiting game loop.")
                    self.running = False
            await self._blit_everything()


async def main():
    """Main function (entry point)
    """
    # Initialize pygame (some linters may report pygame has no 'init' member)
    try:
        pygame.init()  # type: ignore[no-member]  # pylint: disable=no-member
    except Exception:
        # If pygame is stubbed/missing, continue gracefully
        logging.warning("Pygame initialization failed.")
    game_params = GameParams()
    game = BeetusGame(game_params)
    await game.run()
    try:
        pygame.quit()  # type: ignore[no-member]  # pylint: disable=no-member
    except Exception:
        logging.warning("Pygame quit failed.")
    # Exit the program gracefully
    sys.exit()


if __name__ == "__main__":
    asyncio.run(main())
# # End of beetus/main.py #
