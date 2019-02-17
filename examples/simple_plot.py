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
# simple_plot.py

from pubplot import Document
from pubplot.document_classes import ieee_infocom
from pubplot.styles import monochromatic


def single_plot():
    doc = Document(ieee_infocom)
    fig, ax = doc.subfigures()
    ax.plot(range(11), range(11))
    fig.save('single_plot')


def fill_subplot_axes(axes, label=False):
    for i, ax in enumerate(axes):
        if i % 3:
            for j in range(1,5):
                ax.plot(range(11), [j*i for i in range(11)])
        else:
            ax.bar(range(11), [i for i in range(11)])
        if label:
            ax.set_xlabel('lorem')
            ax.set_ylabel('ipsum')


def subplots(nrows, ncols, label=False):
    doc = Document(ieee_infocom, monochromatic())

    fig, ax = doc.subfigures(nrows, ncols, width=doc.textwidth)
    fill_subplot_axes(ax, label=label)
    fig.save('subplots1')

    fig, ax = doc.subfigures(nrows, ncols)
    fill_subplot_axes(ax, label=label)
    fig.save('subplots2')


def main():
    single_plot()
    # subplots(2, 3, label=True)
    subplots(1, 3, label=True)

if __name__ == '__main__':
    main()
