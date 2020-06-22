# Travelling Salesman Problem (TSP) Art in Python

The intention of this repo is to provide a beginner-programmer-friendly way to enable people to make their own TSP Art using Python, and to highlight a few tips and tricks for bettering your art.

The following is written assuming a system with Windows 10. Pull requests are welcome for Linux and MacOS.

# Outline of Algorithm

There are two major steps to the algorithm:

1. Stippling (or 'pointillism') - the image is represented by small black dots of identical size in a way such that darker areas have more dots clustered closely together than lighter areas. The method used here is 'weighted voronoi stippling'.

2. Drawing the Travelling Salesman Problem Path - the [Travelling Salesman Problem](https://simple.wikipedia.org/wiki/Travelling_salesman_problem) is a classic mathematical optimisation problem where given a list of locations, we are to find a single path that travels through all the locations only once and returns to the starting point. Here we use the dots drawn in the first step as our locations and use the Concorde solver to draw an appropriate path.

# Requirements & Instructions

* [Python 3](https://www.python.org/downloads/)
* Optional: [Concorde TSP Solver](http://www.math.uwaterloo.ca/tsp/concorde/index.html)
* Optional: [Git](https://git-scm.com/)
* Optional: Image editing program. Free/open-source ones: [Krita](https://krita.org/en/), [GIMP](https://www.gimp.org/)

## Installation Instructions


## Producing TSP Art Instructions

For reference, we'll assume that the initial image is `figure.png` which is placed in the `images` folder.

### 0. Setup 

Download the repository by clicking the green 'Clone or Download' button, and select 'Download ZIP' and unzip to the folder of your choice. Alternatively if you have Git installed, `git clone https://github.com/matthras/tsp-art-python` into the folder of your choice.

Install the required Python libraries by typing `pip install -r requirements.txt` 

### 1. Image Preprocessing

Skip this step if you're a first timer. This step will only be relevant after you've run through a few images and want to tweak things a little.

What can sometimes happen is that visually there is not enough comparative density between different sections of the image, making it hard to properly identify areas where an image is meant to have more shading. The way to fix this is to increase the contrast on the image, and this can be done in your image editing program.

### 2. Stippling


### 3. Drawing the TSP Solution

#### Using OR-Tools in Python

Open `draw-tsp-path.py` in your editor, and change the variables as follows:

* `ORIGINAL_IMAGE` should be the same initial image you used for Step 2: `images/figure.png`
* `IMAGE_TSP` should refer to the stipple `.tsp` file that is generated after Step 2: `images/figure-stipple.tsp`

Run the file, wait for Python to do its job and when it's done, the final image will be generated as `images/figure-tsp.png`.

#### Using Concorde (Windows GUI)

Open Concorde either by double clicking on `figure-stipple.tsp` or opening the program separately and then loading `figure-stipple.tsp` file into it. Concorde should then display a series of dots that should resemble what you see in `figure-stipple.png`.

There are two ways to go about this:

1. [Recommended if you have more than 1024 points] Click on 'Heuristics' and select 'Lin Kernighan', then click OK.
2. [NOT recommended if you have more than 1024 points] Click on 'Solver', uncheck Verbose, and click OK.

Once Concorde has established an optimal tour, save the tour as a file by going `File > Save Tour`. In our example we'll save it as `figure-tour.cyc` (i.e. type 'figure-tour', click OK and the .cyc extension is automatically applied).

Open `draw-tsp-path-concorde.py` in your editor and change the filenames at the top of the file

* `ORIGINAL_IMAGE` should be the same initial image you used for Step 2: `images/figure.png`
* `IMAGE_TSP` should refer to the stipple `.tsp` file that is generated after Step 2: `images/figure-stipple.tsp`
* `IMAGE_CYC` should refer to the `.cyc` file that is generated from Concorde.

Run the file and the script should generate the final image at `images/figure-tsp.png`.

#### When do I use Concorde over OR-Tools?

Generally speaking you'll only want to use Concorde over OR-Tools if you're looking for a better TSP result, at the cost of increased computational time. Sometimes the OR-Tools algorithm may result in paths that 'cross-over' areas where you don't want them to, whereas the Concorde solver won't. This is where I encourage experimenting a bit.

### 4. Touch-ups


## Potential Problems



# Collection of Reference Links

[Robert (Bob) Bosch's TSP Art Website](http://www2.oberlin.edu/math/faculty/bosch/tspart-page.html)

[Robert Bosch's Outline of the TSPArt Creation Process](http://www2.oberlin.edu/math/faculty/bosch/making-tspart-page.html)

[EvilMadScientist - StippleGen](https://www.evilmadscientist.com/2012/stipplegen-weighted-voronoi-stippling-and-tsp-paths-in-processing/)

[EvilMadScientist - Generating TSP art from a stippled image](https://wiki.evilmadscientist.com/Generating_TSP_art_from_a_stippled_image)

[Grant Trebbin - Voronoi Stippling](https://www.grant-trebbin.com/2017/02/voronoi-stippling.html)

[Adrian Secord's pre-print paper on the Weighted Voronoi Stippling Algorithm](https://mrl.nyu.edu/~ajsecord/npar2002/npar2002_ajsecord_preprint.pdf)

[Weighted Voronoi Stippling Repo that implements Adrian Secord's Weighted Voronoi Stippling Algorithm](https://github.com/ReScience-Archives/Rougier-2017)

[Jack Morris - Creating Travelling Salesman Art with Weighted Voronoi Stippling](http://jackxmorris.com/posts/traveling-salesman-art)

[Craig S. Kaplan - TSP Art](http://www.cgl.uwaterloo.ca/csk/projects/tsp/)