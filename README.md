Hoover Tower Hyperlapse
-----------------------

Warning: the images in this README are bright and flashy -- if you anticipate
it causing you discomfort, don't scroll to the bottom.

---

How does it work? It's a six-step process:

1. Scrape Flickr for the top 500 images that match the search query "hoover
   tower stanford" and are licensed appropriately. Also collect attributions.
2. For each image, search for the vertical edges of HooTow. The easiest way is
   to isolate edges using a vertical Sobel filter + Canny edge detector, and
then apply a linear Hough transform that selects for nearly-vertical lines.
3. Compute the intersection of the verticals to estimate the vanishing point.
   In principle this is like another inverse-Hough transform, but there is also
a nice closed form for the least-squares distance-minimizing point given a set
of lines in 2D.
4. Isolate Hootow's red dome. This is a horizontal Sobel filter + Canny edge
   detector, sent to a circular Hough transform with appropriate bounds on the
radius. This is the slowest part of the process, and it is worth precomputing
this information to make experimenting easier.
5. Center all images by scaling/shifting so that the dome is in a specific
   location. By manual inspection, filter out images that the CV algorithms
failed on (this is the only non-automated part of the process).
6. Use the (scaled/shifted) vanishing points to sort the images in a nice
   order. A nice way to do this is to plot the vanishing points and treat them
as a DAG where each point has edges to its nearest _k_ neighbors that are
_below it_ (this is a DAG because monotonicity of the y-coordinate is
preserved). Then run a topological sort and find longest paths through this
graph.

![hootow shiny](hootow.gif)

![hootow guts](hootow-guts.gif)

This work is somewhat inspired by [Vermödalen by John
Koenig](https://www.youtube.com/watch?v=8ftDjebw8aA) and this [video by Sam
Morrison](https://www.youtube.com/watch?v=WTGmxCpo89c), but also [this SIGGRAPH
2011 paper](http://graphics.cs.cmu.edu/projects/crossDomainMatching/). And
 maybe it all started back in 2013 when a friend showed me [this video from
Teehan+Lax Labs](https://www.youtube.com/watch?v=ngdAF_QFvRc) in CS class....

Of course, credit goes to all the photographers who made their work available
to artists on Flickr. See [`image-credits.txt`](image-credits.txt) for their
names and Flickr handles, sorted by number of images contributed to this
project.

And a note of appreciation to the tooling that made this possible: Flickr's API
is fantastic, and Python's `requests`, `jupyter`, `numpy`, `matplotlib`,
`skimage`, `bs4`, and `networkx`, as well as Imagemagick, made this a pleasure
to work on -- it took less than a day to go from concept to GIF.
