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
# barplot.py

from pubplot import Document
from pubplot.document_classes import acm_sigconf


def single_plot():
    style = Document(acm_sigconf)
    fig, ax = style.subfigures()
    ax.bar(range(11), range(11))
    fig.save('single_barplot')


def fill_subplot_axes(axes, label=False):
    for ax in axes:
        ax.bar(range(11), [-i for i in range(11)])
        if label:
            ax.set_xlabel('lalala')
            ax.set_ylabel('lalala')


def subplots(nrows, ncols, label=False):
    style = Document(acm_sigconf)

    fig, ax = style.subfigures(nrows, ncols, width=style.textwidth)
    fill_subplot_axes(ax, label=label)
    fig.save('subbarplots1')

    fig, ax = style.subfigures(nrows, ncols)
    fill_subplot_axes(ax, label=label)
    fig.save('subbarplots2')


def main():
    single_plot()
    subplots(2, 3, label=True)

if __name__ == '__main__':
    main()
