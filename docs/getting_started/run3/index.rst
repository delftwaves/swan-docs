use with Apptainer or Singularity
=================================

The `SWAN docker image <https://hub.docker.com/r/delftwaves/swan>`_ can be used with `Apptainer <https://apptainer.org>`_ and
`Singularity <https://sylabs.io/singularity/>`_.
These container platforms are especially useful for running SWAN on HPC clusters, either locally or in the cloud
(e.g., `Microsoft Azure <https://azure.microsoft.com/en-us>`_ and `Amazon Web Services <https://aws.amazon.com/>`_).

First, pull the docker image in the following way::

   apptainer pull docker://delftwaves/swan:latest

This pull creates a singularity image named ``swan_latest.sif``, which can then be run with standard Apptainer commands. For example::

   apptainer run --bind .:/home/swan swan_latest.sif swanrun -input <SWAN-command-file-without-extension> -mpi <nprocs> > swanout &

where ``<SWAN-command-file-without-extension>`` is the name of your command file without extension and ``<nprocs>`` indicates
how many processors need to be launched for a parallel MPI run.

To interactively execute commands within the SWAN container, enter::

   apptainer shell swan_latest.sif

Consult this `page <https://apptainer.org/docs/user/main/quick_start.html#overview-of-the-apptainer-interface>`_ to explore the possibilities with Apptainer.

.. note::

   Apptainer is compatible with Singularity, implying that you may use the command ``singularity`` instead of ``apptainer``.
