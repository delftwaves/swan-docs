install SWAN on RPM-based Linux distributions
=============================================

.. _prerequisiteslir:

prerequisites
-------------

The following packages must be installed first:

- gcc
- cmake
- ninja
- git
- perl
- intel-fortran-essentials

These packages can be installed using the default package manager ``dnf``.

First, update the system

.. code-block:: bash

   sudo dnf -y update

Next, run the following command to install GCC (GNU Compiler Collection) on the system

.. code-block:: bash

   sudo dnf -y install gcc

To install ``cmake``, enter

.. code-block:: bash

   sudo dnf -y install cmake

Finally, install ``ninja`` by running the following command

.. code-block:: bash

   sudo dnf -y install ninja-build

.. warning::

   On AlmaLinux OS 9 and Rocky Linux 9, this command must be preceded by the two commands below:

   .. code-block:: bash

      sudo dnf -y install dnf-plugins-core
      sudo dnf config-manager --set-enabled crb

   Note that both AlmaLinux 8 and Rocky 8 install an older version of Ninja, namely 1.8.2, while ``CMake`` requires 1.10+ in order to build fortran. So if possible, please upgrade to
   a higher OS version.

On Oracle Linux 9 ``ninja`` should be installed as follows:

.. code-block:: bash

   sudo dnf --enablerepo=ol9_codeready_builder install ninja-build

Install both ``git`` and ``perl`` in the following way:

.. code-block:: bash

   sudo dnf -y install git

The final step is to install the Intel Fortran Essentials package which also includes the MPI libraries. First, create the repository file in the ``/temp`` folder:

.. code-block:: text

   tee > /tmp/oneAPI.repo << EOF
   [oneAPI]
   name=Intel(R) oneAPI repository
   baseurl=https://yum.repos.intel.com/oneapi
   enabled=1
   gpgcheck=1
   repo_gpgcheck=1
   gpgkey=https://yum.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB
   EOF

Next, move this repo file ``oneAPI.repo`` to the yum configuration folder ``/etc/yum.repos.d``:

.. code-block:: bash

   sudo mv /tmp/oneAPI.repo /etc/yum.repos.d

Finally, install the package with the following command:

.. code-block:: bash

   sudo dnf -y install intel-fortran-essentials

Let your OS system know where to find the compilers and libraries:

.. code-block:: bash

   echo export INTF=/opt/intel/oneapi >> ~/.bashrc
   echo "source \$INTF/setvars.sh > /dev/null 2>&1" >> ~/.bashrc
   source ~/.bashrc

verify installations
~~~~~~~~~~~~~~~~~~~~

Verify the required installations by checking their versions, as follows

.. code-block:: bash

   ifx --version

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
    ``prefix=<folder>``  set the installation folder [``$HOME/wavemodels/swan by`` default]
    ===================  ==================================================================

For example, the following command

.. code-block:: bash

   make config fc=ifx prefix=/usr/local/swan

will configure SWAN to be built using ``ifx`` and then install it at ``/usr/local/swan``.

.. _bmpiri:

building with MPI support
-------------------------

The SWAN source code also supports memory-distributed parallelism for high performance computing applications.
A message passing approach is employed based on the Message Passing Interface (MPI) standard that enables communication between independent processors.

The Intel Fortran Essentials package also contains the Intel MPI Library.
This can be checked with the following command:

.. code-block:: bash

   mpirun --version

We proceed to build SWAN. First, we configure SWAN to be built with support for MPI, as follows

.. code-block:: bash

   make config fc=mpiifx mpi=on

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
For this, an MPI implementation is still required, click :ref:`here <bmpiri>` for details.

The actual mesh partitioning implemented in SWAN is the multilevel k-way method
as explained in the `Metis manual <https://github.com/KarypisLab/METIS/tree/master/manual>`_.

For a proper building, the Metis software package must be installed first on your machine.

On a RPM-based Linux (e.g., Fedora):

.. code-block:: bash

   sudo dnf -y install metis-devel

or, if that does not work (e.g., on Rocky Linux 8), enable the development repository:

.. code-block:: bash

   sudo dnf -y --enablerepo=devel install metis-devel

However, on AlmaLinux 9+ and Rocky 9+ the development packages are moved to the CRB (CodeReady Builder) repo.
In this case, run the following commands:

.. code-block:: bash

   sudo dnf config-manager --set-enabled crb
   sudo dnf makecache
   sudo dnf -y install epel-release
   sudo dnf -y install metis-devel

On Oracle Linux 9 Metis should be installed as follows:

.. code-block:: bash

   sudo dnf -y install epel-release metis-devel

After Metis has been installed we continue with the build of SWAN. First, configure SWAN:

.. code-block:: bash

   make config fc=mpiifx mpi=on metis=on

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
