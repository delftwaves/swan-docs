install SWAN on SUSE Linux
==========================

.. _prerequisiteslsi:

prerequisites
-------------

The following packages must be installed first:

- gcc
- cmake
- ninja
- git
- perl
- intel-fortran-essentials

These packages can be installed using the package manager ``zypper``.

Open a command line terminal and run the following commands:

.. code-block:: bash

   sudo zypper update -y

followed by

.. code-block:: bash

   sudo zypper install -y gcc cmake ninja git

The package ``perl`` is installed by default.

The final step is to install the Intel Fortran Essentials package which also includes the MPI libraries.
First, add the Intel oneAPI repository public key with the following command:

.. code-block:: bash

   sudo zypper addrepo https://yum.repos.intel.com/oneapi oneAPI

By adding this new repository, ``zypper`` automatically imports the public repo key. For some cases ``rpm`` might require explicit key import by:

.. code-block:: bash

   rpm --import https://yum.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB

Finally, install the package with the following command:

.. code-block:: bash

   sudo zypper install -y intel-fortran-essentials

.. important::

   If the above installation method does not work or fails, there is the option to use the offline installer.
   This installer can be downloaded by entering the following command:

   .. code-block:: bash

      wget https://registrationcenter-download.intel.com/akdlm/IRC_NAS/ce0f9b00-4780-483f-bc09-96d6fb4467ca/intel-fortran-essentials-2025.3.1.26_offline.sh

   Then run the installation script as follows:

   .. code-block:: bash

      sudo sh ./intel-fortran-essentials-2025.3.1.26_offline.sh -a --silent --cli --eula accept

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

.. _bmpisi:

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
For this, an MPI implementation is still required, click :ref:`here <bmpisi>` for details.

The actual mesh partitioning implemented in SWAN is the multilevel k-way method
as explained in the `Metis manual <https://github.com/KarypisLab/METIS/tree/master/manual>`_.

For a proper building, the Metis software package must be installed first on your machine.

.. code-block:: bash

   sudo zypper install -y metis-devel

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
