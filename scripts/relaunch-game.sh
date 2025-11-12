#!/usr/bin/env bash
#
# relaunch-game.sh : fully re-package, then play beetus.

set -e

bash -c \
     "${PWD}/scripts/package-game.sh; sleep 1s; ${PWD}/scripts/play-game.sh"
