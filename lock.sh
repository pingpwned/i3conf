#!/bin/sh

scrot ~/.config/i3/wp.png

python3 ~/.config/i3/blur.py ~/.config/i3/wp.png

i3lock -n -f -i ~/.config/i3/wp.png

rm ~/.config/i3/wp.png

