macOS
=====

.. _prerequisitesm:

prerequisites
-------------

The following packages must be installed first:

- gfortran
- cmake
- ninja
- perl

These packages can be installed using system package managers such as Homebrew, MacPorts and Fink.
Here, we will use `Homebrew <https://brew.sh>`_.
You may install Homebrew first (visit its homepage, copy the installation command, open a terminal and paste it into your terminal, and press Enter)
or update it: ``brew update``.

With the command ``brew list`` you can check the installed packages (or *formulae*) on your macOS. If desired, upgrade these packages first by
typing ``brew upgrade``. Below are the instructions for installing the required packages.

First, install GCC (GNU Compiler Collection) that includes ``gfortran`` by opening a terminal (Applications > Utilities and search for the
Terminal app) and typing the following command

.. code-block:: bash

   brew install gcc

To verify the installation, type ``which gfortran`` in the terminal. It should return a path where ``gfortran`` has been installed.
On Apple Silicon, the compiler will be installed into the folder ``/opt/homebrew/bin/``, while on an older Intel Mac, it will be
installed in ``/usr/local/bin``.

Alternatively, type ``gfortran --version`` in the terminal. It should return a version number.

Next, open a terminal and run the following command

.. code-block:: bash

   brew install cmake

and then

.. code-block:: bash

   brew install ninja

These commands will installed ``CMake`` and ``ninja`` on your machine.

Usually, ``perl`` is pre-installed on macOS. This can be checked with the command ``perl -v``.
Otherwise, you may install it by running the command ``brew install perl``.

verify installations
~~~~~~~~~~~~~~~~~~~~

Verify the required installations by checking their versions, as follows

.. code-block:: bash

   gfortran --version

   cmake --version

   ninja --version

   perl --version

If no error is reported, then the installation was successful.

.. important::

   - The ``CMake`` version must be at least 3.20 or newer.
   - The ``perl`` version is 5 or higher.

installation SWAN
-----------------

Once the prerequisites are taken care of, installing SWAN on your machine is a four-step process.

1. download SWAN

Open a Terminal app, copy the command below to paste into the terminal, and press Enter.

.. code-block:: bash

   git clone https://gitlab.tudelft.nl/citg/wavemodels/swan.git && cd swan

2. configure SWAN

.. code-block:: bash

   make config

3. build SWAN

.. code-block:: bash

   make

4. install SWAN

.. code-block:: bash

   make install

SWAN is installed at folder ``$HOME/wavemodels/swan`` by default.
To run SWAN, you need to make sure that this directory is added to your system's ``PATH``.
Open the terminal and enter

.. code-block:: bash

   export PATH=$PATH:$HOME/wavemodels/swan

You can check the new value of ``PATH`` by echoing it: ``echo $PATH``. However, to set this permanently, you need to add it to your
``~/.bash_profile`` or ``~/.bashrc`` file.

options for configuring SWAN
----------------------------

If desired, the build can be configured by passing one or more options below to ``make config``.

    ===================  ==================================================================
    ``fc=<compiler>``    the Fortran90 compiler to use [default is determined by ``CMake``]
    ``mpi=on``           enable build of SWAN with MPI [``off`` by default]
    ``prefix=<folder>``  set the installation folder [``$HOME/wavemodels/swan`` by default]
    ===================  ==================================================================

For example, the following command

.. code-block:: bash

   make config fc=gfortran prefix=/usr/local/swan

will configure SWAN to be built using ``gfortran`` and then install it at ``/usr/local/swan``.

building with MPI support
-------------------------

The SWAN source code also supports memory-distributed parallelism for high performance computing applications.
A message passing approach is employed based on the Message Passing Interface (MPI) standard that enables communication between independent processors.

Popular implementations are `Open MPI <https://www.open-mpi.org>`_ and `MPICH <https://www.mpich.org>`_.
The first one is typically offered by the package managers of Linux and macOS and can be combined with GCC such as gfortran.
The easiest way to install Open MPI is by using the Homebrew package manager.

Before installing Open MPI, make sure that your system is up to date and that GCC has been installed, see :ref:`prerequisites <prerequisitesm>`.
To install Open MPI, run

.. code-block:: bash

   brew install openmpi

To verify whether the installation was successful, run the following command

.. code-block:: bash

   ompi_info --version

or

.. code-block:: bash

   mpirun --version

Once Open MPI is operational, we proceed to build SWAN. First, we configure SWAN to be built with support for Open MPI, as follows

.. code-block:: bash

   make config fc=mpifort mpi=on

The actual building is done by typing

.. code-block:: bash

   make

Finally, to install SWAN, run the following command

.. code-block:: bash

   make install

SWAN is now ready for high performance computing.

clean up
--------

To remove all files installed by ``make install``, type the following command

.. code-block:: bash

   make uninstall

If you want to remove the build directory and all files that have been created after running ``make`` or ``make build``, then run

.. code-block:: bash

   make clobber
