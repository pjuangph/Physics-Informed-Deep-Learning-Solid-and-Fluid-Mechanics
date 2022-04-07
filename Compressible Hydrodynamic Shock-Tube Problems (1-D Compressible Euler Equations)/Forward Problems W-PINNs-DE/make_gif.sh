#!/bin/bash
# Install imagemagick if not there
# sudo apt-get install imagemagick
convert -resize 50% -delay 10 -loop 0 ml_plots/Sod_Shock* sod_shock.gif