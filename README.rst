######################
django-iban-field
######################

Django iban field with validators and optional postgresql in base constraint checking. This is
expected to work with django 1.8 and later.

Installation
=============

Install ``django-iban-field`` like you would install any other pypi package::

    pip install django-iban-field


Configuration and usage
========================

* add ``django_iban`` to the list of ``INSTALLED_APPS`` in your ``settings.py``
* use in ``models.py``::

    from django_iban.fields import IBANField

    ...

    class MyModel(models.Model):
        iban = IBANField(enforce_database_constraint=True, unique=True)

The ``enable_databse_constraint`` option will add a function named is_valid_iban to your database and
use it the enforce the database type checking. This option will have an effect only if you are using
the postgreql backend and have the ``plpython`` extension enabled on your database.

Inspiration
===========

This module take it's inspiration and some of the ideas from the [django-localflvor](http://django-localflavor.readthedocs.org/en/latest/)
IBanField and the specification from [toms-cafe](http://toms-cafe.de/iban/iban.py)

Example
=======

You can find a running example of this field in this [django application](https://github.com/Chedi/test_app)
