=====================
 Tweets Tutorial App
=====================

This project contains the example application for the Tutorial_ held
at the Europython 2014 in Berlin.


Development Setup
=================

To get a development environment this project uses `buildout
<https://pypi.python.org/pypi/zc.buildout/2.2.1>`_


Prerequesites:
--------------

- A Java 7 runtime environment

- Python 3 installed.

Setup:
------

Run `bootstrap.py`::

    python bootstrap.py

And afterwards run buildout::

    ./bin/buildout -N


Starting
========

First start the Crate Datastore::

 ./bin/crate

Initialize the database schema::

 ./parts/crate/bin/crash < src/ep2014tutorial/schema.sql

Then start the application::

 ./bin/app

Using
=====

Go to http://localhost:4200/_plugin/crate-admin/#/tutorial and start
the tweet import to add data.

See the latest tweets at http://localhost:8080/latest

The admin interface of the data store is avalable under
http://localhost:4200 and the app gets exposed unter
http://localhost:8080

Running Tests
=============

The tests are run using the `zope.testrunner
<https://pypi.python.org/pypi/zope.testrunner/4.4.1>`_::

    ./bin/test

.. _Tutorial: https://ep2014.europython.eu/en/accounts/profile/1592/
