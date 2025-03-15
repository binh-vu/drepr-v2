.. include:: glossary.rst

Getting Started
===============

Installation
------------

|drepr| is distributed on `PyPI <https://pypi.org/project/drepr-v2/>`_ so you can install it with pip as shown below.

.. code:: bash

    pip install drepr-v2


Concepts
--------

There are five steps in D-REPR to model a dataset:

1. Define resources: A resource can be a physical file in CSV or JSON format. A dataset may have multiple resources, such as one main CSV file and a data-definition dictionary in a JSON file.
2. Define attributes: Each attribute denotes values that belong to a group. For example, in a relational table, each column is an attribute.
3. Define transformations (preprocessing): Custom Python functions to update resources (e.g., normalize values).
4. Define alignments between attributes: A method to get the value of an attribute from the value of a corresponding attribute. The common methods are accessing by index and by value. For example, in a relational table of products, given a product ID, we can retrieve the corresponding product name in the same row (by index). This step essentially defines the layout of the dataset.
5. Define a semantic model: Assign each attribute a type and define relationships between attributes.

Transformation
~~~~~~~~~~~~~~

A preprocessing function may produce a new attribute or modify an existing attribute. When it produces a new attribute, we can optionally choose the resource ID or let the system generate the ID automatically.

