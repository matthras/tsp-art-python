from PIL import Image, ImageDraw
import os.path

ORIGINAL_IMAGE = "images/aboriginalflag.png"
IMAGE_TSP = "images/aboriginalflag-stipple.tsp"
IMAGE_CYC = "images/aboriginalflag.cyc"

dirname = os.path.dirname(ORIGINAL_IMAGE)
basename = (os.path.basename(ORIGINAL_IMAGE).split('.'))[0]
FINAL_IMAGE = os.path.join(dirname,basename + "-tsp.png")

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
tsp_image.save(FINAL_IMAGE)