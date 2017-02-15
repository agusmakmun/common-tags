common-tags |pypi version|
------------------------------

.. |pypi version|
   image:: https://img.shields.io/pypi/v/common-tags.svg?style=flat-square
   :target: https://pypi.python.org/pypi/common-tags

.. image:: https://img.shields.io/badge/license-GNUGPLv3-blue.svg?style=flat-square
   :target: https://raw.githubusercontent.com/agusmakmun/common-tags/master/LICENSE

.. image:: https://img.shields.io/pypi/pyversions/common-tags.svg?style=flat-square
   :target: https://pypi.python.org/pypi/common-tags

.. image:: https://img.shields.io/badge/Django-1.8,%201.9,%201.10-green.svg?style=flat-square
  :target: https://www.djangoproject.com

Common templatetags provide for Django.


Installation
------------------------------

Common Tags is available directly from `PyPI`_:

1. Installing the package.

::

    $ pip install common-tags


2. Don't forget to add ``'common'`` to your ``'INSTALLED_APPS'`` setting `(without migrations)`.

::

    # settings.py
    INSTALLED_APPS = [
        ....
        'common',
    ]


Usage in template
------------------------------

::

    {% load common_tags %}

For complete usage, see `common/templatetags/common_tags.py`_


Contributing
------------------------------
Feel free to `open a bug`_ or `contribute to code`_ !



.. _PyPI: https://pypi.python.org/pypi/django-contact-widget
.. _common/templatetags/common_tags.py: https://github.com/agusmakmun/common-tags/blob/master/common/templatetags/common_tags.py
.. _open a bug: https://github.com/agusmakmun/common-tags/issues
.. _contribute to code: https://github.com/agusmakmun/common-tags/pulls
