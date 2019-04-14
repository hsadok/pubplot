=======
pubplot
=======

.. image:: https://img.shields.io/pypi/v/pubplot.svg
    :target: https://pypi.python.org/pypi/pubplot
    :alt: PyPI version

.. image:: https://travis-ci.com/hsadok/pubplot.svg?token=WbvxSoxYCEXuq2yHcffB&branch=master
    :target: https://travis-ci.com/hsadok/pubplot
    :alt: Build Status

.. image:: https://readthedocs.org/projects/pubplot/badge/?version=latest
    :target: https://pubplot.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. content-start

**pubplot** allows you to create publication quality plots that fit elegantly
in your LaTeX document.

Main Features
-------------
- **Make plots that match the LaTeX style you are using.** Automatically adjust
  plot sizes to fit in a column (or in a page) of the document. Detect text
  sizes in the LaTeX document and ensures that texts inside plots use the same
  size as captions or other predefined text size (*e.g.*, ``\footnotesize``).
- **Document-level styles.** Apply styles to a document -- instead of a global
  configuration. This allows you to use multiple documents with different
  styles at the same time. Moreover, you can easily reuse your style across
  different documents.

Usage
-----
Start creating a document matching your LaTeX documentclass:

>>> from pubplot import Document
>>> from pubplot.document_classes import acm_sigconf
>>> doc = Document(acm_sigconf)

Now you can use your newly created ``doc`` to make plots that fit well in an
`ACM conference paper <http://www.acm.org/publications/proceedings-template>`_.

>>> fig, ax = doc.subfigures()
>>> ax.plot(range(11), range(11))
>>> fig.save('plot_name')

This will create two files ``plot_name.pdf`` and ``plot_name.pgf``.

To include the generated pgf plot in your LaTeX document, make sure to include
the folowing line your document preamble:

.. code:: latex

    \usepackage{pgf}

Then, include the image using the following line (usually inside a figure environment):

.. code:: latex

    \input{plot_name.pgf}

.. image:: https://raw.githubusercontent.com/hsadok/pubplot/master/docs/images/example1-short.png
    :align: center
    :alt: plot in a LaTeX document

If you are familiar with matplotlib you will have no problem using pubplot. In 
the example above, ``fig`` should support all methods from matplotlib's Figure
class. The same is true for ``ax``, which works like ``Axes``.

For further help, check the examples_ and `the rest of the documentation`_.

.. _examples: https://github.com/hsadok/pubplot/tree/master/examples
.. _`the rest of the documentation`: http://pubplot.readthedocs.org/en/latest/

Installing
----------

Ubuntu/Debian
.............

Make sure you have an updated LaTeX installation::

    sudo apt update
    sudo apt install texlive-base texlive-latex-recommended texlive-fonts-recommended texlive-publishers texlive-latex-extra

Now install ``pubplot`` using ``pip``::

    pip install pubplot

macOS
.....

You need a basic LaTeX installation. An easy way of getting LaTeX on a mac is
through `homebrew cask <https://caskroom.github.io>`_ (although any other form
of getting mactex should be fine)::

    brew cask install mactex

Now install ``pubplot`` using ``pip``::

    pip install pubplot

**Optional but recommended.** Matplotlib works better if you install some
dependencies, if you use `homebrew <https://brew.sh>`_ that can be accomplished
with::

    brew install libpng freetype pkg-config fontconfig

