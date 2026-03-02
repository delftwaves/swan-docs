local copy of built SWAN
========================

The provided run scripts (``swanrun`` and ``swanrun.bat``) enable the user to properly and easily run SWAN both serial as well as parallel.

For Windows users, open a terminal (hit the Window key + R, type ``cmd`` and click OK), navigate to the folder containing your SWAN input files
(command file, grid, bathymetry, etc.), copy and paste the following command, then replace ``<SWAN-command-file-without-extension>``
by the name of your SWAN command file without extension (assuming it is ``sws``), and hit Enter::

   swanrun <SWAN-command-file-without-extension>

while for Linux and Mac users, type in an opened terminal the following command::

   swanrun -input <SWAN-command-file-without-extension>

.. important::

   The script ``swanrun`` needs to be made executable first, as follows::

     chmod +rx swanrun

To redirect screen output to a file, use the sign ``>``. Use an ampersand to run SWAN in the background. An example::

   swanrun -input mytest > swanout &

For a parallel MPI run, you must specify the number of processors ``<nprocs>`` that will be launched, as follows:

.. code-block:: text

   swanrun <SWAN-command-file-without-extension> <nprocs>

in case of Windows, or

.. code-block:: bash

   swanrun -input <SWAN-command-file-without-extension> -mpi <nprocs>

in case of Linux/Mac. By default, ``nprocs = 1``.
