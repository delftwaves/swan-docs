DelftBlue (for TU Delft employees only)
=======================================

prerequisites
-------------

Click `here <https://doc.dhpc.tudelft.nl/delftblue/crash-course/>`_ for background information, how the cluster works, and instructions to access the cluster.
Staff, postdocs, and PhD students have access granted, so no action is needed. MSc students need to request access.

After login, load the following modules:

.. code-block:: bash

   module load 2025
   module load cmake
   module load ninja
   module load intel/oneapi-all
   module load metis

.. tip::

   It is useful to place these modules in the ``~/.bashrc`` file so that they are automatically loaded as soon as you log in again.

   .. code-block:: bash

      echo "# load required modules" >> ~/.bashrc
      echo module load 2025 >> ~/.bashrc
      echo module load cmake >> ~/.bashrc
      echo module load ninja >> ~/.bashrc
      echo module load intel/oneapi-all >> ~/.bashrc
      echo module load metis >> ~/.bashrc

installation SWAN
------------------

1. download SWAN

.. code-block:: bash

   git clone https://gitlab.tudelft.nl/citg/wavemodels/swan.git && cd swan

2. configure SWAN

.. code-block:: bash

   make config fc=mpiifort mpi=on metis=on

3. build SWAN

.. code-block:: bash

   make

4. install SWAN

.. code-block:: bash

   make install

SWAN is installed at folder ``$HOME/wavemodels/swan`` by default.
To run SWAN, you need to make sure that the ``/bin`` folder in this directory is added to your system's ``PATH``:

.. code-block:: bash

   echo export PATH=$PATH:$HOME/wavemodels/swan/bin >> ~/.bash_profile
   source ~/.bash_profile
