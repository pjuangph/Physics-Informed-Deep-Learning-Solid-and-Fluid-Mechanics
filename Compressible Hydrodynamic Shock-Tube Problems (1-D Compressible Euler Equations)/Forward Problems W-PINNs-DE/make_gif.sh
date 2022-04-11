#!/bin/bash
# Install imagemagick if not there
# sudo apt-get install imagemagick
convert  -delay 10 -loop 0 ml_plots/Sod_Shock* sod_shock.gif
convert  -delay 10 -loop 0 ml_plots/Double_Expansion* double_expansion.gif