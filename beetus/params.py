from dataclasses import dataclass
from collections import namedtuple
from beetus.mytypes import SignalType

Point = namedtuple("Point", ["x", "y"])  # Convenience class for coordinates


@dataclass
class GameParams:
    """Parameters for the Beetus game."""
    title: str = "Beetus"
    screen_width: int = 800
    screen_height: int = 600
    fps: int = 60
    bg_color: tuple = (60, 29, 114)  # RGB


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
