# coding=utf-8
# ISC License
# Copyright (c) 2017, Hugo Sadok
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# document.py

from math import sqrt

import matplotlib as mpl
from matplotlib.figure import Figure

from pubplot.axes import PubAxes
from pubplot.figure import PubFigure
from pubplot.helpers import RCParams
from pubplot.latex import get_document_sizes
from pubplot.styles import dichromatic

inches_per_pt = 1.0 / 72.27
golden_ratio = (1.0 + sqrt(5.0)) / 2.0


class Document(object):
    """Document class used to create plots using the same style.

    The Document class serves as a Figure factory. Figures follow the same
    style and are compatible with a given LaTeX document class. By default it
    uses the dichromatic style from ``pubplot.styles``.

    Args:
        document_class: dict with ``documentclass`` and ``document_options``. It
            may optionally contain a list of LaTeX packages under ``packages``
            as well as any other argument acceptable by ``pylatex.document``.
        style: dict following matplotlib rcParams convention.

    Attributes:
        style: dict following matplotlib rcParams convention.
        columnwidth: equivalent size as in the LaTeX document class.
        textwidth: equivalent size as in the LaTeX document class.
        tiny: equivalent size as in the LaTeX document class.
        scriptsize: equivalent size as in the LaTeX document class.
        footnotesize: equivalent size as in the LaTeX document class.
        small: equivalent size as in the LaTeX document class.
        normalsize: equivalent size as in the LaTeX document class.
        large: equivalent size as in the LaTeX document class.
        Large: equivalent size as in the LaTeX document class.
        LARGE: equivalent size as in the LaTeX document class.
        huge: equivalent size as in the LaTeX document class.
        Huge: equivalent size as in the LaTeX document class.

    Examples:
        You may use one of the available document_classes.
        >>> from pubplot.document_classes import ieee_infocom
        >>> doc = Document(ieee_infocom)

        Or provide your own, using a dict
        >>> document_class = {
        ...    'documentclass': 'IEEEtran',
        ...    'document_options': ['10pt', 'conference', 'letterpaper']
        ... }
        >>> doc = Document(document_class)

        Similarly, a style can be chosen from one of the available
        >>> from pubplot.styles import monochromatic
        >>> doc = Document(ieee_infocom, style=monochromatic())

        or personalized to your specific needs.
        >>> style_axis_below = {
        ...     'axes.grid': True,
        ...     'axes.axisbelow': False,
        ...     ':bar:axes.grid.axis': 'y'
        ... }
        >>> doc = Document(ieee_infocom, style=style_axis_below)

        Any rcParam can be used to define the style. But it also supports
        plot-specific styles. In the example above the option
        ``':bar:axes.grid.axis': 'y'`` applies only to bar plots. You may
        prepend ``:<plot_style>:`` to any option in order to apply it only to
        the specific plot type (e.g., bar).

        Once you have a document, you can obtain any LaTeX font size related to
        the ``document_class`` you specified, e.g.,
        >>> doc.normalsize
        10.0

    """

    def __init__(self, document_class, style=None):
        sizes = get_document_sizes(document_class)
        self.__dict__.update(sizes)

        # check https://matplotlib.org/users/customizing.html for some options
        self.style = {
            'pgf.texsystem': 'pdflatex',
            'text.usetex': True,

            # fonts (empty lists inherit from document)
            'font.family': 'serif',
            'font.serif': [],
            'font.sans-serif': [],
            'font.monospace': [],

            # sizes
            'font.size': self.small,
            'axes.labelsize': self.small,
            'legend.fontsize': self.footnotesize,
            'xtick.labelsize': self.small,
            'ytick.labelsize': self.small,

            "pgf.preamble": [
                r"\usepackage[utf8x]{inputenc}",
                r"\usepackage[T1]{fontenc}",
            ]
        }
        if style is not None:
            self.style.update(style)

    def update_style(self, new_style):
        """Updates the current document style.

        Used to change the current style. It is notably useful to change sizes,
        since the document sizes can only be retrieved after the class was
        initialized.

        Examples:
            An example, updating sizes
            >>> from pubplot.document_classes import ieee_infocom
            >>> doc = Document(ieee_infocom)
            >>>
            >>> update_sizes = {
            ...     'font.size': doc.footnotesize,
            ...     'axes.labelsize': doc.footnotesize,
            ...     'legend.fontsize': doc.scriptsize,
            ...     'xtick.labelsize': doc.footnotesize,
            ...     'ytick.labelsize': doc.footnotesize
            ... }
            >>> doc.update_style(update_sizes)

        Args:
            new_style: a dict with rcParams. If the option is not specified in
            the new dict it remains with the old value.
        """
        self.style.update(new_style)

    def figure(self, width=None, height=None, scale=1, xscale=1, yscale=1):
        """Creates a new figure with a single plot.

        Args:
            width: figure width in pt, defaults to columnwidth.
            height: figure height in pt and, by default, it is adjusted
                    automatically based on the width.
            scale: overall figure scale, adjusts both width and height.
            xscale: multiply width by xscale, leaving height intact.
            yscale: multiply height by yscale, leaving width intact.

        Returns:
            fig, axes: a Figure and a single axes.
        """
        fig, axes = self.subfigures(1, 1, width=width, height=height,
                                    scale=scale, xscale=xscale, yscale=yscale)
        return fig, axes[0]

    def subfigures(self, nrows, ncols, width=None, height=None, scale=1,
                   xscale=1, yscale=1):
        """Creates a new figure with multiple plots.

        Args:
            nrows: number of plot rows.
            ncols: number of column rows.
            width: figure width in pt, defaults to columnwidth.
            height: figure height in pt and, by default, it is adjusted
                    automatically based on nrows, ncols and width.
            scale: overall figure scale, adjusts both width and height.
            xscale: multiply width by xscale, leaving height intact.
            yscale: multiply height by yscale, leaving width intact.

        Returns:
            fig, axes: a Figure and a list of axes.
        """
        if width is None:
            width = self.columnwidth

        if height is None:
            height = width / golden_ratio * nrows / ncols

        width = width * inches_per_pt * xscale * scale
        height = height * inches_per_pt * yscale * scale
        figsize = [width, height]

        plain_rc_params = RCParams(self.style).get_rc_to_function('')
        with mpl.rc_context(rc=plain_rc_params):
            fig = Figure(figsize=figsize, frameon=False, tight_layout=True)
            fig = PubFigure(fig, self.style)

            axes = []
            # range is bad in py2.7 however we expect this to be short
            for i in range(1, nrows*ncols+1):
                def lazy_ax(nrows=nrows, ncols=ncols, i=i):
                    return fig.add_subplot(nrows, ncols, i)
                ax = PubAxes(lazy_ax, self.style)
                axes.append(ax)

        return fig, axes
