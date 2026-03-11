Linux
=====

The most common Linux distributions are

- RHEL, CentOS Stream, Rocky Linux, Fedora (RPM-based Linux)
- Debian, Ubuntu, Mint (Debian-based Linux)

with which the installation instructions below can be applied.

.. _prerequisitesl:

prerequisites
-------------

The following packages must be installed first:

- gfortran
- cmake
- ninja
- perl

These packages can be installed using OS-specific package managers.

RPM-based Linux distributions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default package manager is ``dnf``. First, update the system

.. code-block:: bash

   sudo dnf update

Next, run the following command to install GCC (GNU Compiler Collection) on the system

.. code-block:: bash

   sudo dnf install gcc

and then ``gfortran``

.. code-block:: bash

   sudo dnf install gcc-gfortran

To install ``cmake``, enter

.. code-block:: bash

   sudo dnf install cmake

Finally, install ``ninja`` by running the following command

.. code-block:: bash

   dnf install ninja-build

Before installing ``perl``, check if it is already present on your Linux distribution, by typing

.. code-block:: bash

   perl -v

If ``perl`` is not installed, the shell reports that this command is not found.
In that case, install the perl interpreter as follows

.. code-block:: bash

   sudo dnf install perl

Debian-based Linux distributions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The package manager is ``apt-get``. Open a command line terminal and run the following commands:

.. code-block:: bash

   sudo apt-get update

followed by

.. code-block:: bash

   sudo apt-get install build-essential cmake ninja-build gfortran

.. note::

   The ``build-essential`` package installs essential tools and libraries for compiling the source code, including ``gcc`` and ``make``.

The Linux flavors Debian, Ubuntu and Mint have ``perl`` installed by default.

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

.. code-block:: bash

   git clone https://gitlab.tudelft.nl/citg/wavemodels/swan.git && cd swan

Paste this into a shell terminal.

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

You can check the new value of ``PATH`` by echoing it: ``echo $PATH``. However, to set this permanently, you need to add it to
your ``~/.bash_profile`` (or ``~/.bashrc`` file), as follows

.. code-block:: bash

   echo export PATH=$PATH:$HOME/wavemodels/swan >> ~/.bash_profile

options for configuring SWAN
----------------------------

If desired, the build can be configured by passing one or more options below to ``make config``.

    ===================  ==================================================================
    ``fc=<compiler>``    the Fortran90 compiler to use [default is determined by ``CMake``]
    ``mpi=on``           enable build of SWAN with MPI [``off`` by default]
    ``prefix=<folder>``  set the installation folder [``$HOME/wavemodels/swan by`` default]
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

Before installing Open MPI, make sure that your system is up to date and that GCC has been installed, see :ref:`prerequisites <prerequisitesl>`.

To install Open MPI on a RPM-based Linux (e.g., Rocky Linux), run

.. code-block:: bash

   dnf install openmpi openmpi-devel

To install Open MPI on a Debian-based Linux (e.g., Ubuntu), run

.. code-block:: bash

   sudo apt install openmpi-bin libopenmpi-dev

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
