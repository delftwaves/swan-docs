pre-compiled binary packages
============================

A pre-compiled binary distribution allows quick installation without requiring compilation.
The SWAN 41.51 binaries are available for the following OS/ARCH:

- `Windows 11 (AMD64) <https://swanmodel.sourceforge.io/download/zip/SWAN-41.51-Windows.exe>`_
- `Linux Ubuntu 24.04 LTS (AMD64) <https://swanmodel.sourceforge.io/download/zip/SWAN-41.51-Linux.tar.gz>`_
- `macOS Monterey 12.7.6 (AMD64) <https://swanmodel.sourceforge.io/download/zip/SWAN-41.51-macOS.tar.gz>`_
- `macOS Sequoia 15.7.3 (ARM64) <https://swanmodel.sourceforge.io/download/zip/SWAN-41.51-macOS-Silicon.tar.gz>`_

.. attention::

   - The above executables have been built using GNU fortran.
   - These binaries are 64-bit only and, additionally, cannot be executed on multiple cores or threads.
   - Be aware that you may run into compatibility issues when another OS version (e.g., Windows 7, 32-bit Windows 10) or
     distro (e.g., Linux Mint, Rocky Linux) is installed on your machine, or another CPU architecture (e.g., i386/i686, x86_64, AMD64, ARMv7, ARM64).
     If this is the case, then :ref:`Docker <docker>` might be a good alternative for you.
   - The tarball files can be extracted in any folder (``tar xzf SWAN-41.51-<OS>.tar.gz`` with ``OS = Linux`` or ``macOS``)
     and has no further installation steps.
     However, do not forget to permanently add the ``/bin`` folder in your installed folder in your ``$PATH`` variable. Open a command line terminal and enter::

        echo export PATH=$PATH:/your-SWAN-folder/bin >> ~/.bash_profile

   - The macOS executables require the GCC (GNU Compiler Collection) package. Open a terminal (Applications > Utilities and search for the Terminal app),
     copy and paste the following command, and hit Enter::

        brew install gcc

