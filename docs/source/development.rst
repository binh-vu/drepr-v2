Development
===========

Install from PyPI
-------------------

.. code:: bash

    pip install drepr-v2

Install from Source
-------------------

.. code:: bash

    pip install .

Setup Documentation
-------------------

Follow these steps as they are designed for `Read the Docs <https://readthedocs.org/>`_.

1. Installing dependencies & copying required files

.. code:: bash

    pip install .
    pip install -r docs/requirements.txt
    cp CHANGELOG.md docs/source/changelog.md

2. Run ``sphinx-autobuild``

.. code:: bash

    sphinx-autobuild docs/source docs/build/html
