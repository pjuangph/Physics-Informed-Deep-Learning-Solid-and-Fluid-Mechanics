#!/bin/bash
# Install imagemagick if not there
# sudo apt-get install imagemagick
convert -resize 70% -delay 2 -loop 0 ml_plots/Sod_Shock* sod_shock.gif
convert -resize 70% -delay 2 -loop 0 ml_plots/Double_Expansion* double_expansion.gif