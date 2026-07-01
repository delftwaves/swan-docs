local copy of built SWAN
========================

The provided run scripts (``swanrun`` and ``swanrun.bat``) enable the user to properly and easily run SWAN both serial as well as parallel.

For Windows users, open a terminal (hit the Window key + R, type ``cmd`` and click OK), navigate to the folder containing your SWAN input files
(command file, grid, bathymetry, etc.), copy and paste the following command, then replace ``<SWAN-command-file-without-extension>``
by the name of your SWAN command file without extension (assuming it is ``swn``), and hit Enter::

   swanrun <SWAN-command-file-without-extension>

while for Linux and Mac users, type in an opened terminal the following command::

   swanrun -input <SWAN-command-file-without-extension>

.. important::

   - Open an :ref:`Intel oneAPI command prompt <ioap>` in Windows if you have installed the :ref:`Intel Fortran Compiler <intelwin>`.
   - In case of Linux/macOS, the script ``swanrun`` needs to be made executable first, as follows::

       chmod +rx swanrun

To redirect screen output to a file, use the sign ``>``. Use an ampersand to run SWAN in the background. An example::

   swanrun -input mytest > swanout &

where ``mytest.swn`` is your SWAN command file.

.. note::

   To run SWAN on Windows in the background, type the built-in ``start`` command in command prompt, as follows::

      start "" /min cmd /c "swanrun mytest > swanout 2>&1"

For a parallel MPI run, you must specify the number of processors ``<nprocs>`` that will be launched, as follows:

.. code-block:: text

   swanrun <SWAN-command-file-without-extension> <nprocs>

in case of Windows, or

.. code-block:: bash

   swanrun -input <SWAN-command-file-without-extension> -mpi <nprocs>

in case of Linux/Mac. By default, ``nprocs = 1``.

As an example, assume that the command file is named ``mysim.swn`` while the corresponding simulation needs to be run on 5 cores.
In case of Windows, type the following command in an :ref:`Intel oneAPI command prompt <ioap>`::

   start "" /min cmd /c "swanrun mysim 5 > swanout 2>&1"

while run the following command in a Linux/Mac terminal::

   swanrun -input mysim -mpi 5 > swanout &
