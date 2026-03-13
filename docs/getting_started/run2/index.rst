.. _docrun:

from Docker image
=================

The user can either choose between running SWAN directly using docker or the docker in interactive mode.
It is beneficial to download the `SWAN docker image <https://hub.docker.com/r/delftwaves/swan>`_ first::

   docker pull delftwaves/swan && docker tag delftwaves/swan <image-id>

with ``image-id`` a suitable image identifier.

To run SWAN directly, copy and paste the following command, replace the required run parameters, and hit Enter::

   docker run --rm -v .:/home/swan <image-id> swanrun -input <SWAN-command-file-without-extension> -mpi <nprocs>

or without flag ``--rm``::

   docker run -v .:/home/swan <image-id> swanrun -input <SWAN-command-file-without-extension> -mpi <nprocs>

.. note::

   - The directive ``-v .:/home/swan`` ensures that the SWAN output files and the PRINT file created in the directory ``/home/swan`` of the
     docker container will store in your local current directory.
   - The flag ``--rm`` removes the exited container from your machine after terminating SWAN.
   - The container can also be removed by running ``docker rm --force <container-id>``. Check the container identifier by invoking
     the command ``docker ps -a`` (displayed in the final column).
   - If there are stopped containers left, remove them by entering ``docker container prune -f``.

To run the SWAN container interactively, add the flag ``-it``::

   docker run -v .:/home/swan -it <image-id> bash

Once the interactive bash shell is started in the container, the user can access the commands available from Linux Ubuntu (e.g., ``ls``, ``find``,
``which``) and SWAN (e.g., ``swanrun``, ``swan.exe``).

.. _indoc:

You can also treat the container as a light-weight virtual machine (VM) for running, testing or developing applications. Insert the following
command in terminal::

   docker run --name <container-id> -it <image-id> bash

where ``container-id`` is the identifier you specify for easy reuse of this container.

The base image of this container is Ubuntu 24.04. Additionally, the GNU Fortran compiler and the MPI libraries are already installed.
Thus, to rebuild SWAN, consult this :ref:`page <instlswn>`.

.. tip::

   Update the package list for possible upgrades and in case you want to install new apps.
   For example, you may want to install the ``vi`` editor::

      apt-get update && apt-get install vim

You can stop and exit the running container by typing the ``exit`` command or press ctrl+D.

Unless you remove your container, it will remain alive and your created data, new software, etc. within the container will be saved even if you
exit the container.

To restart the container and then run a bash session inside the container, enter::

   docker start <container-id> && docker exec -it <container-id> bash

or::

   docker start <container-id> && docker attach <container-id>

.. caution::

   Do not remove the container (e.g., ``docker rm``), otherwise data will be lost.
