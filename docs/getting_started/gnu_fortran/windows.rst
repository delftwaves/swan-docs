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
   - The ``ninja`` version should be at least 1.10.
   - The ``perl`` version is 5 or higher.

In addition to these packages, Git must also be installed. For the installation, please refer to the official `Git for Windows website <https://gitforwindows.org>`_.

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

To run SWAN, you need to make sure that the ``\bin`` folder in this directory is added to your system's ``PATH``. Open command prompt and type

.. code-block:: text

   setx path "%path%;%LocalAppData%\Programs\wavemodels\swan\bin"

.. warning::

   To check the new value of ``%path%`` by echoing, first close the command prompt terminal and then open again.

options for configuring SWAN
----------------------------

If desired, the build can be configured by passing the option ``prefix=<folder>`` to ``gmake config``.
For example, the following command

.. code-block:: text

   gmake config prefix=C:\Program Files\swan

will configure SWAN to be installed at ``C:\Program Files\swan``.

.. note::

   Unfortunately, there is no simple way to build SWAN with MPI support using gfortran.
   One consideration is to build using :ref:`Intel Fortran + MPI <intelwin>`.
   Another option is to build within the :ref:`Docker container <indoc>`.

clean up
--------

To remove all files installed by ``gmake install``, type the following command

.. code-block:: text

   gmake uninstall

If you want to remove the build directory and all files that have been created after running ``gmake`` or ``gmake build``, then run

.. code-block:: text

   gmake clobber
