from dataclasses import dataclass, field
from typing import List

import pyxel
from collections import namedtuple

from beetus.types import SignalType


Point = namedtuple("Point", ["x", "y"])  # Convenience class for coordinates


@dataclass
class SnakeParams:
    """Parameters for the Snake game."""
    col_background: int = 3  # The background color of the game screen.
    col_body: int = 11  # The color of the snake's body.
    col_head: int = 7  # The color of the snake's head.
    col_death: int = 8  # The background color of the death screen.
    col_apple: int = 8  # The color of the apple.
    # The text displayed on the death screen.
    text_death: List[str] = field(default_factory=lambda: [
                                  "GAME OVER", "(Q)UIT", "(R)ESTART"])
    col_text_death: int = 0  # The color of the text on the death screen.
    height_death: int = 5  # The y-coordinate for the death text.
    width: int = 40  # The width of the game screen.
    height: int = 50  # The height of the game screen.
    # The height of the score bar at the top of the screen.
    height_score: int = pyxel.FONT_HEIGHT
    col_score: int = 6  # The color of the score text.
    col_score_background: int = 5  # The background color of the score bar.
    up: Point = Point(0, -1)  # A Point object representing the up direction.
    # A Point object representing the down direction.
    down: Point = Point(0, 1)
    # A Point object representing the right direction.
    right: Point = Point(1, 0)
    # A Point object representing the left direction.
    left: Point = Point(-1, 0)
    # The starting position of the snake.
    start: Point = Point(5, 5 + pyxel.FONT_HEIGHT)


@dataclass
class PlatformParams:
    """Parameters for generating a rectangular platform (width, height, x_offset, y_offset)."""
    signal: SignalType = "c"
    width: float = 100.0
    height: float = 100.0
    x_offset: float = 0.0
    y_offset: float = 0.0


@dataclass
class WaveParams(PlatformParams):
    """Parameters for generating a moving wave-like object."""
    A: float = 1.0  # Amplitude of the wave
    frequency: float = 1.0  # Frequency of the wave
    phase: float = 0.0  # Phase shift of the wave

    @property
    def piece_kwargs(self):
        """Returns a dictionary of wave piece parameters."""
        return {
            "A": self.A,
            "frequency": self.frequency,
            "phase": self.phase
        }
