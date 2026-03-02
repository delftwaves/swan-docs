what is SWAN?
=============

physics
-------

SWAN accounts for the following physics:

* wave propagation in time and space, shoaling, refraction due to current and depth, frequency shifting due to currents and non-stationary depth
* wave generation by wind
* three- and four-wave interactions
* whitecapping, bottom friction and depth-induced breaking
* dissipation due to aquatic vegetation, turbulent flow and viscous fluid mud
* wave-induced set-up
* propagation from laboratory up to global scales
* transmission through and reflection (specular and diffuse) against obstacles
* diffraction

computations
------------

SWAN computations can be made on a regular, a curvilinear grid and a triangular mesh in a Cartesian or spherical coordinate system.
Nested runs, using input from either SWAN, WAVEWATCH III or WAM can be made with SWAN.

SWAN runs can be done serial, i.e. one SWAN program on one processor, as well as parallel, i.e. one SWAN program on more than one processor.
For the latter, two parallelization strategies are available:

* distributed-memory paradigm using MPI and
* shared-memory paradigm using OpenMP.

output quantities
-----------------

SWAN provides the following output quantities (files containing tables, maps and timeseries):

* one- and two-dimensional spectra,
* significant wave height and wave periods,
* average wave direction and directional spreading,
* one- and two-dimensional spectral source terms,
* root-mean-square of the orbital near-bottom motion,
* dissipation,
* wave-induced force (based on the radiation-stress gradients),
* set-up,
* diffraction parameter,
* and many more.
