#! /usr/bin/env python3
# -----------------------------------------------------------------------------
# Weighted Voronoi Stippler
# Copyright (2017) Nicolas P. Rougier - BSD license
# Edited by Matthew Mack
#
# Implementation of:
#   Weighted Voronoi Stippling, Adrian Secord
#   Symposium on Non-Photorealistic Animation and Rendering (NPAR), 2002
# -----------------------------------------------------------------------------
# Some usage examples
#
# stippler.py boots.jpg --save --force --n_point 20000 --n_iter 50
#                       --pointsize 0.5 2.5 --figsize 8 --interactive
# stippler.py plant.png --save --force --n_point 20000 --n_iter 50
#                       --pointsize 0.5 1.5 --figsize 8
# stippler.py gradient.png --save --force --n_point 5000 --n_iter 50
#                          --pointsize 1.0 1.0 --figsize 6
# -----------------------------------------------------------------------------
# usage: stippler.py [-h] [--n_iter n] [--n_point n] [--epsilon n]
#                    [--pointsize min,max) (min,max] [--figsize w,h] [--force]
#                    [--save] [--display] [--interactive]
#                    image filename
#
# Weighted Vororonoi Stippler
#
# positional arguments:
#   image filename        Density image filename
#
# optional arguments:
#   -h, --help            show this help message and exit
#   --n_iter n            Maximum number of iterations
#   --n_point n           Number of points
#   --epsilon n           Early stop criterion
#   --pointsize (min,max) (min,max)
#                         Point mix/max size for final display
#   --figsize w,h         Figure size
#   --force               Force recomputation
#   --save                Save computed points
#   --display             Display final result
#   --interactive         Display intermediate results (slower)
# -----------------------------------------------------------------------------
import tqdm
import voronoi
import os.path
import scipy.ndimage
import imageio
import numpy as np

def normalize(D):
    Vmin, Vmax = D.min(), D.max()
    if Vmax - Vmin > 1e-5:
        D = (D-Vmin)/(Vmax-Vmin)
    else:
        D = np.zeros_like(D)
    return D


def initialization(n, D):
    """
    Return n points distributed over [xmin, xmax] x [ymin, ymax]
    according to (normalized) density distribution.

    with xmin, xmax = 0, density.shape[1]
         ymin, ymax = 0, density.shape[0]

    The algorithm here is a simple rejection sampling.
    """

    samples = []
    while len(samples) < n:
        # X = np.random.randint(0, density.shape[1], 10*n)
        # Y = np.random.randint(0, density.shape[0], 10*n)
        X = np.random.uniform(0, density.shape[1], 10*n)
        Y = np.random.uniform(0, density.shape[0], 10*n)
        P = np.random.uniform(0, 1, 10*n)
        index = 0
        while index < len(X) and len(samples) < n:
            x, y = X[index], Y[index]
            x_, y_ = int(np.floor(x)), int(np.floor(y))
            if P[index] < D[y_, x_]:
                samples.append([x, y])
            index += 1
    return np.array(samples)



if __name__ == '__main__':
    import argparse
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation

    default = {
        "n_point": 5000,
        "n_iter": 50,
        "threshold": 255,
        "force": False,
        "save": False,
        "figsize": 6,
        "display": False,
        "interactive": False,
        "pointsize": (1.0, 1.0),
        "pdf": False,
        "png": False,
        "npy": False
    }

    description = "Weighted Vororonoi Stippler"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('filename', metavar='image filename', type=str,
                        help='Density image filename ')
    parser.add_argument('--n_iter', metavar='n', type=int,
                        default=default["n_iter"],
                        help='Maximum number of iterations')
    parser.add_argument('--n_point', metavar='n', type=int,
                        default=default["n_point"],
                        help='Number of points')
    parser.add_argument('--pointsize', metavar='(min,max)', type=float,
                        nargs=2, default=default["pointsize"],
                        help='Point mix/max size for final display')
    parser.add_argument('--figsize', metavar='w,h', type=int,
                        default=default["figsize"],
                        help='Figure size')
    parser.add_argument('--force', action='store_true',
                        default=default["force"],
                        help='Force recomputation')
    parser.add_argument('--threshold', metavar='n', type=int,
                        default=default["threshold"],
                        help='Grey level threshold')
    parser.add_argument('--save', action='store_true',
                        default=default["save"],
                        help='Save computed points')
    parser.add_argument('--display', action='store_true',
                        default=default["display"],
                        help='Display final result')
    parser.add_argument('--interactive', action='store_true',
                        default=default["interactive"],
                        help='Display intermediate results (slower)')
    parser.add_argument('--pdf', action='store_true', 
                        default=default["pdf"], 
                        help='Save image as pdf')
    parser.add_argument('--png', action='store_true', 
                        default=default["png"], 
                        help='Save image as png')
    parser.add_argument('--npy', action='store_true', 
                        default=default["npy"], 
                        help='Save points as npy file')
    args = parser.parse_args()

    filename = args.filename
    density = imageio.imread(filename, as_gray=True, pilmode='L') # Flattens into a grayscale image, 8 bit pixels, black and white

    # We want (approximately) 500 pixels per voronoi region
    zoom = (args.n_point * 500) / (density.shape[0]*density.shape[1]) # Dividing # of pixels*points by image dimensions
    zoom = int(round(np.sqrt(zoom)))
    #density = scipy.ndimage.zoom(density, zoom, order=0) # This is the bit that resizes the image based on the calculations in the last two lines.
    # Apply threshold onto image
    # Any color > threshold will be white
    density = np.minimum(density, args.threshold) # Obtains minimum value for checking against threshold

    density = 1.0 - normalize(density)
    density = density[::-1, :] # Flips the image upside down? (why? Probably because image coordinate axes are upside down)
    density_P = density.cumsum(axis=1)
    density_Q = density_P.cumsum(axis=1)

    # Setting filenames
    dirname = os.path.dirname(filename)
    basename = (os.path.basename(filename).split('.'))[0]
    pdf_filename = os.path.join(dirname, basename + "-" + str(args.n_point) + "-stipple.pdf")
    png_filename = os.path.join(dirname, basename + "-" + str(args.n_point) + "-stipple.png")
    dat_filename = os.path.join(dirname, basename + "-" + str(args.n_point) + "-stipple.tsp")

    # Initialization
    if not os.path.exists(dat_filename) or args.force:
        points = initialization(args.n_point, density)
        print("Number of points:", args.n_point)
        print("Number of iterations:", args.n_iter)
    else:
        points = np.load(dat_filename)
        print("Number of points:", len(points))
        print("Number of iterations: -")
    if (args.pdf): 
        print("PDF: %s " % pdf_filename)
    if (args.png):
        print("PNG: %s " % png_filename)
    print("TSP: %s " % dat_filename)

    xmin, xmax = 0, density.shape[1]
    ymin, ymax = 0, density.shape[0]
    bbox = np.array([xmin, xmax, ymin, ymax])
    ratio = (xmax-xmin)/(ymax-ymin)

    # Interactive display
    if args.interactive:

        # Setup figure
        fig = plt.figure(figsize=(args.figsize, args.figsize/ratio),
                         facecolor="white")
        ax = fig.add_axes([0, 0, 1, 1], frameon=False)
        ax.set_xlim([xmin, xmax])
        ax.set_xticks([])
        ax.set_ylim([ymin, ymax])
        ax.set_yticks([])
        scatter = ax.scatter(points[:, 0], points[:, 1], s=1,
                             facecolor="k", edgecolor="None")

        def update(frame):
            global points
            # Recompute weighted centroids
            regions, points = voronoi.centroids(points, density, density_P, density_Q)

            # Update figure
            Pi = points.astype(int)
            X = np.maximum(np.minimum(Pi[:, 0], density.shape[1]-1), 0)
            Y = np.maximum(np.minimum(Pi[:, 1], density.shape[0]-1), 0)
            sizes = (args.pointsize[0] +
                     (args.pointsize[1]-args.pointsize[0])*density[Y, X])
            scatter.set_offsets(points)
            scatter.set_sizes(sizes)
            bar.update()

            # Save result at last frame
            if (frame == args.n_iter-2 and
                      (not os.path.exists(dat_filename) or args.save)):
                
                tspfileheader = "NAME : " + filename + "\nTYPE : TSP\nCOMMENT: Stipple of " + filename + " with " + str(len(points)) + " points\nDIMENSION: " + str(len(points)) + "\nEDGE_WEIGHT_TYPE: ATT\nNODE_COORD_SECTION"
                nodeindexes = np.arange(1,len(points)+1)[:,np.newaxis]
                np.savetxt(dat_filename, np.concatenate((nodeindexes,points),axis=1), ['%d','%d','%d'], header=tspfileheader, comments='')
                if (args.pdf): 
                    plt.savefig(pdf_filename)
                if (args.png):
                    plt.savefig(png_filename)
                if (args.npy):
                    np.save(dat_filename, points)

        bar = tqdm.tqdm(total=args.n_iter)
        animation = FuncAnimation(fig, update,
                                  repeat=False, frames=args.n_iter-1)
        plt.show()

    elif not os.path.exists(dat_filename) or args.force:
        for i in tqdm.trange(args.n_iter):
            regions, points = voronoi.centroids(points, density, density_P, density_Q)

            
    if (args.save or args.display) and not args.interactive:
        fig = plt.figure(figsize=(args.figsize, args.figsize/ratio),
                         facecolor="white")
        ax = fig.add_axes([0, 0, 1, 1], frameon=False)
        ax.set_xlim([xmin, xmax])
        ax.set_xticks([])
        ax.set_ylim([ymin, ymax])
        ax.set_yticks([])
        scatter = ax.scatter(points[:, 0], points[:, 1], s=1, 
                             facecolor="k", edgecolor="None")
        Pi = points.astype(int)
        X = np.maximum(np.minimum(Pi[:, 0], density.shape[1]-1), 0)
        Y = np.maximum(np.minimum(Pi[:, 1], density.shape[0]-1), 0)
        sizes = (args.pointsize[0] +
                 (args.pointsize[1]-args.pointsize[0])*density[Y, X])
        scatter.set_offsets(points)
        scatter.set_sizes(sizes)

        # Save stipple points and tippled image
        if not os.path.exists(dat_filename) or args.save:
            tspfileheader = "NAME : " + filename + "\nTYPE : TSP\nCOMMENT: Stipple of " + filename + " with " + str(len(points)) + " points\nDIMENSION: " + str(len(points)) + "\nEDGE_WEIGHT_TYPE: ATT\nNODE_COORD_SECTION"
            nodeindexes = np.arange(1,len(points)+1)[:,np.newaxis]
            np.savetxt(dat_filename, np.concatenate((nodeindexes,points),axis=1), ['%d','%d','%d'], header=tspfileheader, comments='')
            if (args.npy):
                np.save(dat_filename, points)
            if (args.pdf):
                plt.savefig(pdf_filename)
            if (args.png):
                plt.savefig(png_filename)

        if args.display:
            plt.show()

    # Plot voronoi regions if you want
    # for region in vor.filtered_regions:
    #     vertices = vor.vertices[region, :]
    #     ax.plot(vertices[:, 0], vertices[:, 1], linewidth=.5, color='.5' )
