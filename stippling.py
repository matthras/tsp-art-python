# Copyright Matthew Mack (c) 2020 under CC-BY 4.0: https://creativecommons.org/licenses/by/4.0/

import os
import sys
cmd = sys.executable

# The filename of the image you want to stipple goes here.
ORIGINAL_IMAGE = "images/smileyface-inverted.png"

# Enables saving of images.
SAVE_IMAGE = True

# Total number of points to stipple your image with
NUMBER_OF_POINTS = 1024

# Number of iterations for the algorithm to evenly spread out all the points. Increase if it looks like all the points haven't 'settled' after the last few iterations.
NUMBER_OF_ITERATIONS = 25

# Sets of the point size of dots to appear on the final iteration. Currently untested.
POINT_SIZE = "1.0 1.0"

# Size of the window that shows the points and their iterations.
FIGURE_SIZE = 8

# Sets a cutoff point X between black and white (0-255) where any value between X and 255 (white) is considered the 'background' and will not be 'covered' by a dot. 
THRESHOLD = 255

# Forces recalculations. Currently untested, so best to laeve this on True.
FORCE = True

# Display a diagram that shows each iteration of the algorithm, showing the points being arranged into their positions.
INTERACTIVE = True

# Displays the plot of the final iteration. Usually disabled if INTERACTIVE = True, since the diagram will also show the final iteration.  
DISPLAY_FINAL_ITERATION = False

# Save the image of the final iteration as a .png file.
SAVE_AS_PNG = True

# Saves the image of the final iteration as a .pdf file.
SAVE_AS_PDF = False

# Saves the position of all points as a numpy array.
SAVE_AS_NPY = False

full_command = " weighted-voronoi-stippler/stippler.py " + ORIGINAL_IMAGE

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
if(DISPLAY_FINAL_ITERATION):
  full_command += " --display"
if(SAVE_AS_PNG):
  full_command += " --png"
if(SAVE_AS_PDF):
  full_command += " --pdf"
if(SAVE_AS_NPY):
  full_command += " --npy"

os.system(cmd + full_command)