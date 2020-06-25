import os
import sys
cmd = sys.executable

# Your filename goes here
ORIGINAL_FILE = "sample-images/figure.png"

# This saves the 
SAVE_IMAGE = True

NUMBER_OF_POINTS = 2048

NUMBER_OF_ITERATIONS = 50

POINT_SIZE = "1.0 1.0"

FIGURE_SIZE = 6

THRESHOLD = 255

FORCE = True

INTERACTIVE = True

full_command = "cmd weighted-voronoi-stippler/stippler.py " + ORIGINAL_FILE

if(SAVE_IMAGE):
  full_command += " --save"
full_command += " --n_point " + str(NUMBER_OF_POINTS)
full_command += " --n_iter " + str(NUMBER_OF_ITERATIONS)
full_command += " --pointsize " + POINT_SIZE
full_command += " --figsize " + str(FIGURE_SIZE)
full_command += " --threshold " + str(THRESHOLD)
if(FORCE):
  full_command += " --force"
if(INTERACTIVE):
  full_command += " --interactive"

os.system(full_command)