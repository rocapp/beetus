import pyxel
from beetus.games.base import *


class PerlinNoiseApp(GameApp):
    def __init__(self, on_quit_callback=dummy_method):
        super().__init__(on_quit_callback=on_quit_callback)
        pyxel.init(64, 64, title="Perlin Noise", capture_scale=4)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        self.generate_perlin_noise()

    @staticmethod
    def generate_perlin_noise():
        for y in range(64):
            for x in range(64):
                n = pyxel.noise(
                    x / 10,
                    y / 10,
                    pyxel.frame_count / 40,
                )
                col = 7 if n > 0.4 else 6 if n > 0 else 12 if n > -0.4 else 0
                pyxel.pset(x, y, col)
