#! /usr/bin/env python3
import os
import sys
cmd = sys.executable

os.system(cmd + " " + "weighted-voronoi-stippler/stippler.py sample-images/figure.png --save --n_point 2048 --n_iter 25 --pointsize 1.0 1.0 --figsize 6 --threshold 255 --force --interactive --png")

# os.system(cmd + " " + "weighted-voronoi-stippler/stippler.py sample-images/figure.png --save --n_point 2048 --n_iter 50 --pointsize 1.0 1.0 --figsize 6 --threshold 255 --force --interactive --png")