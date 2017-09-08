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
# figure.py

import warnings

import matplotlib as mpl
from matplotlib.backends.backend_pgf import FigureCanvasPgf

from pubplot.helpers import RCParamWrapper


class PubFigure(RCParamWrapper):
    """Matplotlib Figure wrapper.

    This wraps Figure objects which allows us to do some nice stuff. Such as
    local rcParams and personalized save method.

    Args:
        fig: A matplotlib Figure object or function that returns such object.
        rc: Matplotlib RCparams.

    Attributes:
        fig: A matplotlib Figure object.
    """

    def __init__(self, fig, rc):
        super(PubFigure, self).__init__(fig, rc)
        self.fig = fig

    def save(self, name, pdf=True, pgf=True):
        """Save figure to pgf and pdf.

        By default it saves the figure in both pdf and pgf, but this behavior
        may be adapted using ``pdf`` and ``pgf`` keyword arguments.

        Args:
            name: file name without extension
            pdf: if True saves figure in pdf format
            pgf: if True saves figure in pgf format
        """
        with mpl.rc_context(rc=self.rc.get_rc_to_function('save')):
            canvas = FigureCanvasPgf(self.fig)
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                if pgf:
                    canvas.print_figure(name + '.pgf', bbox_inches='tight')
                if pdf:
                    canvas.print_figure(name + '.pdf', bbox_inches='tight')
