# title: Snake!
# author: Marcus Croucher
# desc: A Pyxel snake game example
# site: https://github.com/kitao/pyxel
# license: MIT
# version: 1.0

from collections import deque

import pyxel

from beetus.params import SnakeParams, Point
from beetus.games.base import *
from beetus.games.perlin_noise import PerlinNoiseApp


class Snake(GameApp):
    """The class that sets up and runs the snake game."""

    def __init__(self, params: SnakeParams, on_quit_callback=dummy_method):
        """Initiate pyxel, set up initial game variables, and run."""
        super().__init__(on_quit_callback=on_quit_callback)
        self.params = params
        define_sound_and_music()
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        """Initiate key variables (direction, snake, apple, score, etc.)"""
        self.direction = self.params.right
        self.snake = deque()
        self.snake.append(self.params.start)
        self.death = False
        self.score = 0
        self.generate_apple()
        pyxel.playm(0, loop=True)

    ##############
    # Game logic #
    ##############

    def update(self):
        """Update logic of game.
        Updates the snake and checks for scoring/win condition."""

        if not self.death:
            self.update_direction()
            self.update_snake()
            self.check_death()
            self.check_apple()

        if pyxel.btnp(pyxel.KEY_R) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_START):
            self.reset()

    def update_direction(self):
        """Watch the keys and change direction."""

        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            if self.direction is not self.params.down:
                self.direction = self.params.up

        elif pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            if self.direction is not self.params.up:
                self.direction = self.params.down

        elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            if self.direction is not self.params.right:
                self.direction = self.params.left

        elif pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            if self.direction is not self.params.left:
                self.direction = self.params.right

    def update_snake(self):
        """Move the snake based on the direction."""

        old_head = self.snake[0]
        new_head = Point(old_head.x + self.direction.x,
                         old_head.y + self.direction.y)
        self.snake.appendleft(new_head)
        self.popped_point = self.snake.pop()

    def check_apple(self):
        """Check whether the snake is on an apple."""

        if self.snake[0] == self.apple:
            self.score += 1
            self.snake.append(self.popped_point)
            self.generate_apple()
            pyxel.play(0, 0)

    def generate_apple(self):
        """Generate an apple randomly."""
        snake_pixels = set(self.snake)
        self.apple = self.snake[0]
        while self.apple in snake_pixels:
            x = pyxel.rndi(0, self.params.width - 1)
            y = pyxel.rndi(self.params.height_score +
                           1, self.params.height - 1)
            self.apple = Point(x, y)

    def check_death(self):
        """Check whether the snake has died (out of bounds or doubled up.)"""

        head = self.snake[0]
        if head.x < 0 or head.y < self.params.height_score or head.x >= self.params.width or head.y >= self.params.height:
            self.death_event()
        elif len(self.snake) != len(set(self.snake)):
            self.death_event()

    def death_event(self):
        """Kill the game (bring up end screen)."""

        self.death = True  # Check having run into self
        pyxel.stop()
        pyxel.play(0, 1)

    ##############
    # Draw logic #
    ##############

    def draw(self):
        """Draw the background, snake, score, and apple OR the end screen."""

        if not self.death:
            pyxel.cls(col=self.params.col_background)
            self.draw_snake()
            self.draw_score()
            pyxel.pset(self.apple.x, self.apple.y, col=self.params.col_apple)
        else:
            self.draw_death()

    def draw_snake(self):
        """Draw the snake with a distinct head by iterating through deque."""

        for i, point in enumerate(self.snake):
            if i == 0:
                colour = self.params.col_head
            else:
                colour = self.params.col_body
            pyxel.pset(point.x, point.y, col=colour)

    def draw_score(self):
        """Draw the score at the top."""

        score = f"{self.score:04}"
        pyxel.rect(0, 0, self.params.width, self.params.height_score,
                   self.params.col_score_background)
        pyxel.text(1, 1, score, self.params.col_score)

    def draw_death(self):
        """Draw a blank screen with some text."""

        pyxel.cls(col=self.params.col_death)

        display_text = self.params.text_death[:]
        display_text.insert(1, f"{self.score:04}")

        for i, text in enumerate(display_text):
            y_offset = (pyxel.FONT_HEIGHT + 2) * i
            text_x = self.center_text(text, self.params.width)
            pyxel.text(text_x, self.params.height_death +
                       y_offset, text, self.params.col_text_death)

    @staticmethod
    def center_text(text, page_width, char_width=pyxel.FONT_WIDTH):
        """Helper function for calculating the start x value for centered text."""

        text_width = len(text) * char_width
        return (page_width - text_width) // 2


###########################
# Music and sound effects #
###########################


def define_sound_and_music():
    """Define sound and music."""

    # Sound effects
    pyxel.sounds[0].set(
        notes="c3e3g3c4c4", tones="s", volumes="4", effects=("n" * 4 + "f"), speed=7
    )
    pyxel.sounds[1].set(
        notes="f3 b2 f2 b1  f1 f1 f1 f1",
        tones="p",
        volumes=("4" * 4 + "4321"),
        effects=("n" * 7 + "f"),
        speed=9,
    )

    melody1 = (
        "c3 c3 c3 d3 e3 r e3 r"
        + ("r" * 8)
        + "e3 e3 e3 f3 d3 r c3 r"
        + ("r" * 8)
        + "c3 c3 c3 d3 e3 r e3 r"
        + ("r" * 8)
        + "b2 b2 b2 f3 d3 r c3 r"
        + ("r" * 8)
    )
    melody2 = (
        "rrrr e3e3e3e3 d3d3c3c3 b2b2c3c3"
        + "a2a2a2a2 c3c3c3c3 d3d3d3d3 e3e3e3e3"
        + "rrrr e3e3e3e3 d3d3c3c3 b2b2c3c3"
        + "a2a2a2a2 g2g2g2g2 c3c3c3c3 g2g2a2a2"
        + "rrrr e3e3e3e3 d3d3c3c3 b2b2c3c3"
        + "a2a2a2a2 c3c3c3c3 d3d3d3d3 e3e3e3e3"
        + "f3f3f3a3 a3a3a3a3 g3g3g3b3 b3b3b3b3"
        + "b3b3b3b4 rrrr e3d3c3g3 a2g2e2d2"
    )

    # Music
    pyxel.sounds[2].set(
        notes=melody1 * 2 + melody2 * 2,
        tones="s",
        volumes=("3"),
        effects=("nnnsffff"),
        speed=20,
    )

    harmony1 = (
        "a1 a1 a1 b1  f1 f1 c2 c2  c2 c2 c2 c2  g1 g1 b1 b1" * 3
        + "f1 f1 f1 f1 f1 f1 f1 f1 g1 g1 g1 g1 g1 g1 g1 g1"
    )
    harmony2 = (
        ("f1" * 8 + "g1" * 8 + "a1" * 8 + ("c2" * 7 + "d2")) *
        3 + "f1" * 16 + "g1" * 16
    )

    pyxel.sounds[3].set(
        notes=harmony1 * 2 + harmony2 * 2, tones="t", volumes="5", effects="f", speed=20
    )
    pyxel.sounds[4].set(
        notes=("f0 r a4 r  f0 f0 a4 r  f0 r a4 r  f0 f0 a4 f0"),
        tones="n",
        volumes="6622 6622 6622 6426",
        effects="f",
        speed=20,
    )

    pyxel.musics[0].set([], [2], [3], [4])
