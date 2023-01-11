************
Introduction
************

**daul** is a collection of utilities for dealing with pandas' DataFrames, numpy arrays, and files. 

One of the purpose of **daul** is to allow constructive updates of :class:`pandas.DataFrame` using utilities in :mod:`daul.pandas_utils` to encourage programming in functional style. As use of some of these functions is rather frequent, they are also incorporated in abbreviated form in the :mod:`daul.shortcuts` module. 

Example
*******

.. include:: code/introduction.py
   :start-after: <intro:1>
   :end-before: </intro:1>


However, **daul** also contains utilities that can be of general use, e.g., for dealing with nested DataFrames (:ref:`Inner frames`), transformations of DataFrames (:ref:`Transformations`), and many others.

The :mod:`daul.numpy_utils` and :mod:`daul.file_utils` are modules with less functions, they, nevertheless, contain some potentially useful utilities. 	

