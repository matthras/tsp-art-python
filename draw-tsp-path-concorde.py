# Copyright Matthew Mack (c) 2020 under CC-BY 4.0: https://creativecommons.org/licenses/by/4.0/
from PIL import Image, ImageDraw
import os.path

ORIGINAL_IMAGE = "images/smileyface-inverted.png"
IMAGE_TSP = "images/smileyface-inverted-1024-stipple.tsp"
IMAGE_CYC = "images/smileyface-inverted-1024-stipple.cyc"

list_of_nodes = []

with open(IMAGE_TSP) as f:
  for _ in range(6):
    next(f)
  for line in f:
    i,x,y = line.split()
    list_of_nodes.append((int(float(x)),int(float(y))))

tsp_path = []

with open(IMAGE_CYC) as g:
  for line in g:
    tsp_path.append(list_of_nodes[int(line)])
tsp_path.append(list_of_nodes[0])

original_image = Image.open(ORIGINAL_IMAGE)
width, height = original_image.size

tsp_image = Image.new("RGBA",(width,height),color='white')
tsp_image_draw = ImageDraw.Draw(tsp_image)
#tsp_image_draw.point(tsp_path,fill='black')
tsp_image_draw.line(tsp_path,fill='black',width=1)
tsp_image = tsp_image.transpose(Image.FLIP_TOP_BOTTOM)
FINAL_IMAGE = IMAGE_TSP.replace("-stipple.tsp", "-tsp.png")
tsp_image.save(FINAL_IMAGE)
print("TSP solution has been drawn and can be viewed at", FINAL_IMAGE)