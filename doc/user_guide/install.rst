Installing Hyperspy
===================

For the easiest way to install Hyperspy in Windows :ref:`read this <quick-windows-install>`.

For the easiest way to install Hyperspy in MacOs :ref:`read this <quick-mac-install>`.

The easiest way to install Hyperspy in Ubuntu Linux is by downloading and installing the deb file from the  `Download section <http://hyperspy.org/download.html>`_.

For installing in any other platform you can :ref:`install-with-python-installers` or :ref:`install-source`. 

.. _quick-windows-install:

Quick instructions to install Hyperspy in Windows
-------------------------------------------------

#. Download and install `EPD. <http://www.enthought.com/products/epd.php>`_ EPD is reccomended for the best performance (it is compiled using Intel MKL libraries) and the easiest intallation (all the required libraries are incluided). The academic license is free and it can be obtained `here. <http://www.enthought.com/products/edudownload.php>`_
#. (Maybe) Restart the computer
#. Download and install Hyperspy from the `Download section <http://hyperspy.org/download.html>`_

For more options and details read the rest of the documentation.

.. _quick-mac-install:


Quick instructions to install Hyperspy in MacOs
-------------------------------------------------

#. Download and install `EPD. <http://www.enthought.com/products/epd.php>`_ EPD is reccomended for the best performance (it is compiled using Intel MKL libraries) and the easiest intallation (all the required libraries are incluided). The academic license is free and it can be obtained `here. <http://www.enthought.com/products/edudownload.php>`_
#. (Maybe) Restart the computer
#. Open a terminal and type: `easy_install hyperspy`

For more options and details read the rest of the documentation.


.. _install-with-python-installers:

Install using Python installers
-------------------------------

Since version 4.1 Hyperspy is listed in the `Python Package Index <http://pypi.python.org/pypi>`_. Therefore, it can be automatically downloaded and installed using `distribute <http://pypi.python.org/pypi/distribute>`_ or (our favourite) `pip <http://pypi.python.org/pypi/pip>`_. Depending on your Python distribution, you might need to install at least one of these packages manually.

Install using `pip`:

.. code-block:: bash

    $ pip install hyperspy

Install using `distribute` or `setuptools`:

.. code-block:: bash

    $ easy_install hyperspy

In any case, you must be sure to have all the dependencies installed, see :ref:`install-dependencies`


.. _install-binary:
 
Install from a binary
---------------------

We provide  binary distributions for Ubuntu Linux and Windows (`see the Downloads section of the website <http://hyperspy.org/download.html>`_). In Ubuntu the dependencies are installed automatically. In Windows it is necessary to previously install the required libraries, see :ref:`install-dependencies`. To install easily in other platforms see :ref:`install-with-python-installers`
    

.. _install-source:

Install from source
-------------------

.. _install-released-source:

Released version
^^^^^^^^^^^^^^^^

To install from source grab a tar.gz release and in Linux/Mac (requires to :ref:`install-dependencies` manually):

.. code-block:: bash

    $ tar -xzf hyperspy.tar.gz
    $ cd hyperspy
    $ python setup.py install
    
You can also use a Python installer, e.g.

.. code-block:: bash

    $ pip install hyperspy.tar.gz

.. _install-dev:

Development version
^^^^^^^^^^^^^^^^^^^


To get the development version from our git repository you need to install `git <http://git-scm.com//>`_. Then just do:

.. code-block:: bash

    $ git clone https://github.com/hyperspy/hyperspy.git

To install Hyperspy you could proceed like in :ref:`iinstall-released-source`. However, if you are installing from the development version most likely you will prefer to install Hyperspy using  `pip <http://www.pip-installer.org>`_ development mode: 


.. code-block:: bash

    $ cd hyperspy
    $ pip install -e ./
    
In any case, you must be sure to have all the dependencies installed, see :ref:`install-dependencies`
 
.. _create-debian-binary: 
    
Creating Debian/Ubuntu binaries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can create binaries for Debian/Ubuntu from the source by running the `release_debian` script

.. code-block:: bash

    $ ./release_debian
    
.. Warning::

    For this to work, the following packages must be installed in your system python-stdeb, debhelper, dpkg-dev and python-argparser are required.
    

.. _install-dependencies:

Installing the required libraries
---------------------------------

.. Warning::

    Read at least up to the second paragraph of this instruction before taking any action
    
    
Before installing Hyperspy Python and the following libraries be installed in the system: numpy, scipy, matplotlib, ipython, traits and traitsui. For full functionality it is reccomended to also install h5py, mdp and scikit-learn. In Windows Hyperspy uses the Ipython's QtConsole nd therefore Qt and PyQt or PySide are also required.

In Windows and Mac the easiest way to install these packages is by installing the `enthought python distribution. <http://www.enthought.com/products/epd.php>`_ (EPD) that from version 0.7.1 comes with all the required libraries included by default. Academics can get it free `here <http://www.enthought.com/products/edudownload.php>`_ .

If you use an Ubuntu binary to install Hyperspy all the dependencies should install automatically.















