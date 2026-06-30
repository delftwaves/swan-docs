.. _intelwin:

Windows
=======

prerequisites
-------------

The following packages must be installed first:

- gmake
- cmake
- ninja
- perl

These packages are all included in the `Strawberry Perl <https://strawberryperl.com>`_ package.

After installing the latest release of Strawberry Perl, check whether the required packages were successfully installed on your computer,
by opening a Windows command prompt (press Windows key + R, type ``cmd``, and hit Enter) and running the following commands::

   gmake --version

   cmake --version

   ninja --version

   perl --version

If each of the above package reports a version number, then the installation was successful.

.. important::

   - The version number of ``CMake`` must be at least 3.20 or newer.
   - The ``ninja`` version should be at least 1.10.
   - The ``perl`` version is 5 or higher.

In addition to these packages, ``git`` and ``curl`` must also be installed. For the installation, please refer to the official `Git for Windows website <https://gitforwindows.org>`_.

The final step is to install the Intel Fortran Compiler. The installation method here is the
offline installer. This installer can be downloaded by entering the following command in a Windows command prompt:

.. code-block:: text

   curl https://registrationcenter-download.intel.com/akdlm/IRC_NAS/9af38d13-867b-45af-a950-0b42d9bac1ae/intel-fortran-compiler-2026.0.0.566_offline.exe --output ifc2026_offline.exe

For a proper installation the Build Tools for Visual Studio is required. Download this VS Build Tools installer:

.. code-block:: text

   curl -SL https://aka.ms/vs/stable/vs_buildtools.exe --output vs_buildtools.exe

Run the VS Build Tools installer and ensure you have selected the **Desktop development with C++** workload:

.. code-block:: text

   vs_buildtools.exe

This might take a while. After completing installation of VS Build Tools, set the following environment variable permanently:

.. code-block:: text

   setx VS2026INSTALLDIR "C:\Program Files (x86)\Microsoft Visual Studio\18\BuildTools" /m

.. warning::

   Depending on the installed version (here: Build Tools for Visual Studio 2026, v18), the path above may be different. Check where the BuildTools folder is located and adjust the path if necessary.

Next, run the Intel Fortran Compiler installer:

.. code-block:: text

   ifc2026_offline.exe

Follow the instruction steps to complete the successful installation. This might take a while.

.. note::

   This installs version 2026.0.0 of Intel Fortran Compiler and is not necessarily the latest version.
   Check this `page <https://www.intel.com/content/www/us/en/developer/tools/oneapi/fortran-compiler-download.html?operatingsystem=windows&distribution-windows=offline>`_
   to get the latest version.

Finally, we check whether the installation was successful.

.. _ioap:

With the next two steps, an **Intel oneAPI terminal** will be started, after which the necessary environment variables will be set.

- Click on the *Start* button to open the Start menu.
- Type ``intel oneapi`` in the search box at the top and click on the app.

Type ``ifx --version`` to verify Intel Fortran Compiler was installed.

installation SWAN
-----------------

Once the prerequisites are taken care of, installing SWAN on your machine is a four-step process.

1. download SWAN

   Open an :ref:`Intel oneAPI command prompt <ioap>`, navigate to your Downloads folder, copy the command below, right-click in the prompt window to paste and press Enter.

   .. code-block:: text

      git clone https://gitlab.tudelft.nl/citg/wavemodels/swan.git && cd swan

2. configure SWAN

   .. code-block:: text

      gmake config

3. build SWAN

   .. code-block:: text

      gmake

4. install SWAN

   .. code-block:: text

      gmake install

SWAN is installed at folder ``%LocalAppData%\Programs\wavemodels\swan`` by default. The current value of ``%LocalAppData%`` can be checked by typing

.. code-block:: text

   echo %LocalAppData%

To run SWAN, you need to make sure that the ``\bin`` folder in this directory is added to your system's ``PATH``. Open command prompt and type

.. code-block:: text

   setx path "%path%;%LocalAppData%\Programs\wavemodels\swan\bin"

.. warning::

   To check the new value of ``%path%`` by echoing, first close the command prompt terminal and then open again.

options for configuring SWAN
----------------------------

If desired, the build can be configured by passing one or more options below to ``gmake config``.

    ===================  ====================================================================================
    ``fc=<compiler>``    the Fortran90 compiler to use [default is determined by ``CMake``]
    ``mpi=on``           enable build of SWAN with MPI [``off`` by default]
    ``metis=on``         enable build of SWAN with Metis [``off`` by default]
    ``prefix=<folder>``  set the installation folder [``%LocalAppData%\Programs\wavemodels\swan`` by default]
    ===================  ====================================================================================

For example, the following command

.. code-block:: text

   gmake config prefix=C:\Program Files\swan

will configure SWAN to be installed at ``C:\Program Files\swan``.

.. _bmpiwi:

building with MPI support
-------------------------

The SWAN source code also supports memory-distributed parallelism for high performance computing applications.
A message passing approach is employed based on the Message Passing Interface (MPI) standard that enables communication between independent processors.

First, download the offline installer of `Intel MPI Library <https://www.intel.com/content/www/us/en/developer/tools/oneapi/mpi-library-download.html?operatingsystem=windows&distribution-windows=offline>`_:

.. code-block:: text

   curl https://registrationcenter-download.intel.com/akdlm/IRC_NAS/8fd05348-8fd1-40e4-ba04-35bdb2ae9252/intel-mpi-2021.18.0.742_offline.exe --output impi2021_offline.exe

Next, run the install script:

.. code-block:: text

   impi2021_offline.exe

and follow the instruction steps to complete the installation.

Finally, let us check the installation of Intel MPI Library with the following command inserted in the :ref:`Intel oneAPI command prompt <ioap>`:

.. code-block:: text

   mpiexec --version

If successful, then we proceed to build SWAN. First, we configure SWAN to be built with support for MPI, as follows

.. code-block:: text

   gmake config fc=mpiifx.bat mpi=on

The actual building is done by typing

.. code-block:: text

   gmake

Finally, to install SWAN, run the following command

.. code-block:: text

   gmake install

SWAN is now ready for high performance computing.

building with Metis support
---------------------------

SWAN can be compiled with support for Metis to partition an unstructured mesh so that simulations can be carried out on distributed-memory machines.
For this, an MPI implementation is still required, click :ref:`here <bmpiwi>` for details.

The actual mesh partitioning implemented in SWAN is the multilevel k-way method
as explained in the `Metis manual <https://github.com/KarypisLab/METIS/tree/master/manual>`_.

For a proper building, the Metis software package must be installed first on your Windows machine.

First, open an :ref:`Intel oneAPI command prompt <ioap>` and then navigate to your SWAN source directory.
Next, copy the command below, right-click in the prompt window to paste and press Enter.

.. code-block:: text

   git clone https://github.com/scivision/METIS.git && cd METIS

Next, build the Metis libraries in the following way:

.. code-block:: text

   cmake --workflow --preset default

After Metis has been build we continue with the build of SWAN. At the top of SWAN source directory configure SWAN:

.. code-block:: text

   gmake config fc=mpiifx.bat mpi=on metis=on

Next, build SWAN:

.. code-block:: text

   gmake

And finally, install SWAN:

.. code-block:: text

   gmake install

clean up
--------

To remove all files installed by ``gmake install``, type the following command

.. code-block:: text

   gmake uninstall

If you want to remove the build directory and all files that have been created after running ``gmake`` or ``gmake build``, then run

.. code-block:: text

   gmake clobber
