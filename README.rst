This is a Python package for notebook, an addon for `Websauna framework <https://websauna.org>`_.

Prerequisites
=============

* PostgreSQL

* Redis

Installation
============

Local development mode
-----------------------

Activate the virtual environment of your Websauna application.

Then::

    cd notebook  # This is the folder with setup.py file
    pip install -e .

Running the development website
===============================

Local development machine
-------------------------

Example (OSX / Homebrew)::

    psql create notebook_dev
    ws-sync-db development.ini
    pserve -c development.ini --reload

Running the test suite
======================

First create test database::

    # Create database used for unit testing
    psql create notebook_test

Install test and dev dependencies (run in the folder with ``setup.py``)::

    pip install -e ".[dev,test]"

Run test suite using py.test running::

    py.test websauna/notebook/tests --ini test.ini

More information
================

Please see https://websauna.org/