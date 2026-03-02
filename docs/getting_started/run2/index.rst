from Docker image
=================

The user can either choose between running SWAN directly using docker or the docker in interactive mode (option ``-it``).

To run SWAN directly, copy and paste the following command, replace the required run parameters, and hit Enter::

   docker run --rm -v .:/home/swan delftwaves/swan swanrun -input <SWAN-command-file-without-extension> -mpi <nprocs>

To run the SWAN container interactively, enter::

   docker run --rm -v .:/home/swan -it delftwaves/swan bash

Once the interactive bash shell is started in the container, the user can access the commands available from Linux Ubuntu (e.g., ``ls``, ``find``,
``which``) and SWAN (e.g., ``swanrun``, ``swan.exe``).

.. note::

   - The option ``-v .:/home/swan`` ensures that the SWAN output files and the PRINT file created in the directory ``/home/swan`` of the
     docker container will store in your local current directory.
   - The option ``--rm`` removes the exited container from your machine after terminating SWAN. (Check by invoking the command ``docker ps -a``.)
   - For a complete overview of the command ``docker run``, please refer to this `page <https://docs.docker.com/reference/cli/docker/container/run/>`_.
