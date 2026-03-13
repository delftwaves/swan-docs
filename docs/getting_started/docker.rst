.. _docker:

docker container
================

A docker container bundles an application (here SWAN) with all its dependencies, including libraries, configuration files, and a lightweight OS kernel (usually Linux Ubuntu) into a single package, and can be used to run the application directly on any OS platform. To run the container, one needs to
install the `Docker Engine <https://docs.docker.com/engine/install/>`_ in their machine. This engine is available for Windows, Linux, and macOS via
`Docker Desktop <https://www.docker.com/products/docker-desktop/>`_.

After installing Docker Desktop, you can test SWAN and check if it runs properly.
Open a terminal, copy and paste the following command into the terminal and press Enter:

.. code-block:: bash

   docker run delftwaves/swan

This ``docker run`` command first pulls the image ``delftwaves/swan`` from the `Docker Hub <https://hub.docker.com>`_, which might take a few moments.
Next, it creates a new container based on this image and then the SWAN executable within this container will be run.
If the installation was successful, you should see a message saying that SWAN ran successfully.

To run your own SWAN application, download the official `SWAN docker image <https://hub.docker.com/r/delftwaves/swan>`_ from the Docker Hub repository.
Like the SWAN source code, this image is distributed under `GNU GPL v3 license <https://gitlab.tudelft.nl/citg/wavemodels/swan/-/blob/main/LICENSE>`_.

Consult this :ref:`page <docrun>` for the various run instructions.
