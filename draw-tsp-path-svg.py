import cairo
from PIL import Image

# Change these file names to the relevant files.
ORIGINAL_IMAGE = "example-output/smileyface-inverted.png"
IMAGE_TSP = "example-output/smileyface-inverted-1024-stipple.tsp"
IMAGE_CYC = "example-output/smileyface-inverted-1024-stipple.cyc"

def obtain_list_of_nodes():
  list_of_nodes = []
  with open(IMAGE_TSP) as f:
    for _ in range(6):
      next(f)
    for line in f:
      i,x,y = line.split()
      list_of_nodes.append((int(float(x)),int(float(y))))
  return list_of_nodes

def obtain_concorde_solution(list_of_nodes):
  tsp_path = []
  with open(IMAGE_CYC) as g:
    for line in g:
      tsp_path.append(list_of_nodes[int(line)])
  tsp_path.append(list_of_nodes[0]) # The .cyc file does not include the starting node
  return tsp_path

def draw_svg(tsp_path):
  im = Image.open(ORIGINAL_IMAGE)
  WIDTH, HEIGHT = im.size
  FINAL_IMAGE_SVG = IMAGE_TSP.replace("-stipple.tsp", "-tsp.svg")
  #surface = cairo.ImageSurface(cairo.FORMAT_ARGB32,WIDTH,HEIGHT)
  surface = cairo.SVGSurface(FINAL_IMAGE_SVG,WIDTH,HEIGHT)
  ctx = cairo.Context(surface)
  #ctx.scale(WIDTH,HEIGHT) # Not sure about this, seems redundant if image dimensions are already specified by surface
  # Transform to normal cartesian coordinate system
  m = cairo.Matrix(yy=-1, y0=HEIGHT)
  ctx.transform(m)
  # Paint the background white
  ctx.save()
  ctx.set_source_rgb(1,1,1)
  ctx.paint()
  ctx.restore()
  # Draw lines
  ctx.move_to(tsp_path[0][0], tsp_path[0][1])
  for node in range(1,len(tsp_path)):
    ctx.line_to(tsp_path[node][0],tsp_path[node][1])
  ctx.save()
  ctx.set_source_rgb(0,0,0)
  ctx.set_line_width(1)
  ctx.stroke_preserve()
  ctx.restore()  
  #FINAL_IMAGE_PNG = IMAGE_TSP.replace("-stipple.tsp", "-tsp.png")
  #surface.write_to_png(FINAL_IMAGE)
  surface.finish()

def main():
  list_of_nodes = obtain_list_of_nodes()
  tsp_path = obtain_concorde_solution(list_of_nodes) # Later change to if-no-concorde, then use OR-tools
  draw_svg(tsp_path)

if __name__ == '__main__':
    main()