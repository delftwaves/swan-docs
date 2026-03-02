Windows
=======

prerequisites
-------------

The following packages must be installed first:

- gfortran
- gmake
- cmake
- ninja
- perl

These packages are all included in the `Strawberry Perl <https://strawberryperl.com>`_ package.

After installing the latest release of Strawberry Perl, check whether the required packages were successfully installed on your computer,
by opening a command prompt (press Windows key + R, type ``cmd``, and hit Enter) and running the following commands::

   gfortran --version

   cmake --version

   ninja --version

   perl --version

If each of the above package reports a version number, then the installation was successful.

.. important::

   - The version number of ``CMake`` must be at least 3.20 or newer.
   - The ``perl`` version is 5 or higher.

installation SWAN
-----------------

Once the prerequisites are taken care of, installing SWAN on your machine is a four-step process.

1. download SWAN

   Open a command prompt, copy the command below, right-click in the prompt window to paste and press Enter.

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

To run SWAN, you need to make sure that this directory is added to your system's ``PATH``. Open command prompt and type

.. code-block:: text

   setx path "%path%;%LocalAppData%\Programs\wavemodels\swan"

.. warning::

   To check the new value of ``%path%`` by echoing, first close the command prompt terminal and then open again.

options for configuring SWAN
----------------------------

If desired, the build can be configured by passing one or more options below to ``gmake config``.

    ===================  ====================================================================================
    ``fc=<compiler>``    the Fortran90 compiler to use [default is determined by ``CMake``]
    ``mpi=on``           enable build of SWAN with MPI [``off`` by default]
    ``prefix=<folder>``  set the installation folder [``%LocalAppData%\Programs\wavemodels\swan`` by default]
    ===================  ====================================================================================

For example, the following command

.. code-block:: text

   gmake config prefix=C:\Program Files\swan

will configure SWAN to be installed at ``C:\Program Files\swan``.

clean up
--------

To remove all files installed by ``gmake install``, type the following command

.. code-block:: text

   gmake uninstall

If you want to remove the build directory and all files that have been created after running ``gmake`` or ``gmake build``, then run

.. code-block:: text

   gmake clobber
