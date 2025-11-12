# #
# beetus/main.py : games menu entrypoint
# #

import pyxel

from beetus.games.snake import Snake


class App:
    def __init__(self):
        pyxel.init(160, 120, title="Welcome to beetus 🩸. Hope you have a pfun time.")
        pyxel.images[0].load(0, 0, "assets/pfun-cutielogo-icon.png")
        self.current_game = None # State: None for menu, object for current game
        pyxel.run(self.update, self.draw)

    def return_to_menu(self):
        """Callback to switch state from game back to menu."""
        self.current_game = None
        pyxel.stop() # Stop game music/sounds

    def update(self):
        if self.current_game:
            # delegate update to the current running game instance
            self.current_game.update()
            return
        
        # Menu update logic
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_S):
            # Start the Snake game, passing the callback for when it quits
            self.current_game = Snake(on_quit_callback=self.return_to_menu)

    def draw(self):
        if self.current_game:
            # Delegate draw to the running game instance
            self.current_game.draw()
            return

        # Menu draw logic
        pyxel.cls(0)
        # Instructions:
        pyxel.text(55, 41, "Select a game", pyxel.frame_count % 16)
        # Draw the logo sprite below
        pyxel.blt(61, 66, 0, 0, 0, 38, 16)
        
        pyxel.text(55, 85, "[S]nake", pyxel.frame_count % 16)


App()
