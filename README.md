# Travelling Salesman Problem (TSP) Art in Python

The intention of this repo is to provide a beginner-programmer-friendly way to enable people to make their own TSP Art using Python, and to highlight a few tips and tricks for bettering your art.

# Outline of Algorithm

There are two major steps to the algorithm:

1. Stippling (or 'pointillism') - the image is represented by small black dots of identical size in a way such that darker areas have more dots clustered closely together than lighter areas. The method used here is 'weighted voronoi stippling'.

2. Drawing the Travelling Salesman Problem Path - the [Travelling Salesman Problem](https://simple.wikipedia.org/wiki/Travelling_salesman_problem) is a classic mathematical optimisation problem where given a list of locations, we are to find a single path that travels through all the locations only once and returns to the starting point. Here we use the dots drawn in the first step as our locations and use an algorithm called the 'nearest neighbour algorithm'.

# Requirements & Instructions

At the bare minimum you'll need installed:

* [Python 3](https://www.python.org/downloads/)
* [Git](https://git-scm.com/)
* Optional: An appropriate image editing program e.g. [GIMP](https://www.gimp.org/)

## Installation Instructions


## Producing TSP Art Instructions

### 1. Image Preprocessing

Skip this step if you're a first timer. This step will only be relevant after you've run through a few images and want to tweak things a little.

What can sometimes happen is that visually there is not enough comparative density between different sections of the image, making it hard to properly identify areas where an image is meant to have more shading. The way to fix this is to increase the contrast on the image, and this can be done in GIMP.

Some examples using the Twitter croissant emoji (which is also included in the input files):


### 2. Stippling


### 3. Drawing the TSP Solution


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