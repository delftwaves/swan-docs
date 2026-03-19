install SWAN on SUSE Linux
==========================

.. _prerequisitesls:

prerequisites
-------------

The following packages must be installed first:

- gfortran
- cmake
- ninja
- perl
- git

These packages can be installed using the package manager ``zypper``.

Open a command line terminal and run the following commands:

.. code-block:: bash

   sudo zypper update -y

followed by

.. code-block:: bash

   sudo zypper install -y gcc gcc-fortran cmake ninja git

The package ``perl`` is installed by default.

verify installations
~~~~~~~~~~~~~~~~~~~~

Verify the required installations by checking their versions, as follows

.. code-block:: bash

   gfortran --version

   cmake --version

   ninja --version

   perl --version

   git --version

If no error is reported, then the installation was successful.

.. important::

   - The ``CMake`` version must be at least 3.20 or newer.
   - The ``ninja`` version should be at least 1.10.
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
To run SWAN, you need to make sure that the ``/bin`` folder in this directory is added to your system's ``PATH``.
Open the terminal and enter

.. code-block:: bash

   export PATH=$PATH:$HOME/wavemodels/swan/bin

You can check the new value of ``PATH`` by echoing it: ``echo $PATH``.
However, to set this permanently, you need to add it to your ``~/.bashrc``, as follows

.. code-block:: bash

   echo export PATH=$PATH:$HOME/wavemodels/swan/bin >> ~/.bashrc
   source ~/.bashrc

options for configuring SWAN
----------------------------

If desired, the build can be configured by passing one or more options below to ``make config``.

    ===================  ==================================================================
    ``fc=<compiler>``    the Fortran90 compiler to use [default is determined by ``CMake``]
    ``mpi=on``           enable build of SWAN with MPI [``off`` by default]
    ``metis=on``         enable build of SWAN with Metis [``off`` by default]
    ``prefix=<folder>``  set the installation folder [``$HOME/wavemodels/swan`` by default]
    ===================  ==================================================================

For example, the following command

.. code-block:: bash

   make config fc=gfortran prefix=/usr/local/swan

will configure SWAN to be built using ``gfortran`` and then install it at ``/usr/local/swan``.

.. _bmpis:

building with MPI support
-------------------------

The SWAN source code also supports memory-distributed parallelism for high performance computing applications.
A message passing approach is employed based on the Message Passing Interface (MPI) standard that enables communication between independent processors.

Popular implementations are `Open MPI <https://www.open-mpi.org>`_ and `MPICH <https://www.mpich.org>`_.
The first one is typically offered by the package managers of Linux and macOS and can be combined with GCC such as gfortran.

Before installing Open MPI, make sure that your system is up to date and that GCC has been installed, see :ref:`prerequisites <prerequisitesls>`.

To install Open MPI on SUSE Linux, run

.. code-block:: bash

   sudo zypper install -y openmpi openmpi-devel

and then

.. code-block:: bash

   echo export PATH=$PATH:/usr/lib64/mpi/gcc/openmpi5/bin/ >> ~/.bashrc
   echo export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib64/mpi/gcc/openmpi5/lib64/ >> ~/.bashrc
   source ~/.bashrc

To verify whether the installation was successful, run the following command

.. code-block:: bash

   ompi_info --version

or

.. code-block:: bash

   mpirun --version

.. warning::

   If Open MPI is not found, replace ``openmpi5`` by ``openmpi`` in the above paths.

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

building with Metis support
---------------------------

SWAN can be compiled with support for Metis to partition an unstructured mesh so that simulations can be carried out on distributed-memory machines.
For this, an MPI implementation is still required, click :ref:`here <bmpis>` for details.

The actual mesh partitioning implemented in SWAN is the multilevel k-way method
as explained in the `Metis manual <https://github.com/KarypisLab/METIS/tree/master/manual>`_.

For a proper building, the Metis software package must be installed first on your machine.

.. code-block:: bash

   sudo zypper install -y metis-devel

After Metis has been installed we continue with the build of SWAN. First, configure SWAN:

.. code-block:: bash

   make config fc=mpifort mpi=on metis=on

Next, build SWAN:

.. code-block:: bash

   make

And finally, install SWAN:

.. code-block:: bash

   make install

clean up
--------

To remove all files installed by ``make install``, type the following command

.. code-block:: bash

   make uninstall

If you want to remove the build directory and all files that have been created after running ``make`` or ``make build``, then run

.. code-block:: bash

   make clobber
