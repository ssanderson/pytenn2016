Unspeakably Evil Hacks in Service of Marginally Improved Syntax
---------------------------------------------------------------

Delivered at 2:00 PM on Sat Feb 6 2016.

Running the Slides
~~~~~~~~~~~~~~~~~~

To run the slides, check out the repo and run:

    $ pip install virtualenv virtualenvwrapper   # Skip if you already have these.
    $ git submodule init && gitsubmodule update  # Clone vendored forks of pyxl3 and RISE.
    $ mkvirtualenv -p $(which python3) pytenn2016
    $ source run.sh  # It's important that you source here rather than just invoking ./run.sh!

If you want to install the (somewhat more complex) compiled dependencies for
slides referencing numba and Cython, you should run:

    $ pip install -e .[extra]

before sourcing `run.sh`.  This command may fail depending on whether you have
the requisite non-Python binary dependencies (e.g. LLVM or ATLAS/BLAS)
installed.  The correct way to acquire binary dependencies varies from platform
to platform.  Consult the docs for `numba` for instructions on installation for
your platform of choice.

This should start install all the necessary dependencies into a Python 3
virtualenv named `pytenn2016` and start a Jupyter Notebook server with the
LiveReveal extension installed and running.
