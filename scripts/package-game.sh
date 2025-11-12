#!/usr/bin/env bash
#
# package-game.sh: Package the game using the Pyxel app file in the current directory.

set -e

pyxel package beetus beetus/main.py
