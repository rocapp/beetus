# #
# games/base.py: defines the base GameApp class for all game apps
# #
__all__ = ["GameApp", "dummy_method"]

import pyxel


def dummy_method():
    """does nothing (as if...)"""
    pass


class GameApp:
    """Base class for all game apps."""

    @property
    def on_quit_callback(self):
        """Callback to switch state from game back to menu."""
        return self._on_quit_callback

    def __init__(self, *args, on_quit_callback=dummy_method, **kwargs):
        self._on_quit_callback = on_quit_callback

    def update(self):
        """Update logic of game."""
        if pyxel.btn(pyxel.KEY_Q):
            # perform the specified quit callback method
            self.on_quit_callback()
