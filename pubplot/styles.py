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
# styles.py

import matplotlib as mpl
import numpy as np
from matplotlib import cycler


def dichromatic(color1='r', color2='k'):
    """Dichromatic style.

    Classic style using only two colors. It includes a background grid.

    Args:
        color1: primary color, defaults to red.
        color2: secondary color, defaults to black.

    Returns:
        dict: rcParams dict with the appropriate style
    """
    return {
        # line styles
        'axes.prop_cycle': cycler('color', [color1] * 4 + [color2] * 4) +
                           cycler('linestyle', ['-', '--', ':', '-.'] * 2),

        # grid
        'grid.color': '0.3',
        'grid.linestyle': ':',
        'grid.linewidth': 0.5,
        'axes.grid': True,
        'axes.axisbelow': True,
        ':bar:axes.grid.axis': 'y',

        # patch edges
        'patch.edgecolor': 'black',
        'patch.force_edgecolor': True,
        'patch.linewidth': 0.5,

        # font
        'font.family': 'sans-serif'
    }


def monochromatic(color='k'):
    """Monochromatic style.

    Equivalent to Dichromatic using the same color for both arguments.

    Args:
        color: the single color, defaults to black.

    Returns:
        dict: rcParams dict with the appropriate style
    """
    return dichromatic(color, color)


def qualitative(markers=True):
    cmap = mpl.cm.get_cmap('Set2')
    bins = np.linspace(0, 1, 8)
    palette = list(map(tuple, cmap(bins)[:, :3]))

    prop_cycle = cycler('color', palette)

    if markers:
        prop_cycle += cycler('marker', ['.', '^', 'x', 'v', 'D', '*', '>', '+'])

    return {
        # line styles
        'axes.prop_cycle': prop_cycle,

        # grid
        'grid.color': '0.3',
        'grid.linestyle': ':',
        'grid.linewidth': 0.5,
        'axes.grid': True,
        'axes.axisbelow': True,
        ':bar:axes.grid.axis': 'y',

        # patch edges
        'patch.edgecolor': 'black',
        'patch.force_edgecolor': True,
        'patch.linewidth': 0.5,

        # font
        'font.family': 'sans-serif'
    }
    
def mpl_default():
    return {}
