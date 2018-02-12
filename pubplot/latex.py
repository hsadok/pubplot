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
# latex.py

import os
from pylatex import Document, NoEscape, Command
import tempfile


def get_document_sizes(document_class):
    """Get useful document sizes given a LaTeX document class.

    Args:
        document_class: dict with ``documentclass`` and ``document_options``. It
            may optionally contain a list of LaTeX packages under ``packages``
            as well as any other argument acceptable by ``pylatex.document``.

    Examples:
        You may use one of the available document_classes.
         >>> from pprint import pprint
         >>> from pubplot.document_classes import ieee_infocom
         >>> sizes_dict = get_document_sizes(ieee_infocom)
         >>> pprint(sizes_dict)
         {'Huge': 24.0,
          'LARGE': 17.0,
          'Large': 14.0,
          'columnwidth': 252.0,
          'footnotesize': 8.0,
          'huge': 20.0,
          'large': 12.0,
          'normalsize': 10.0,
          'scriptsize': 7.0,
          'small': 9.0,
          'textwidth': 516.0,
          'tiny': 5.0}

         Or provide your own, using a dict
         >>> document_class = {
         ...    'documentclass': 'IEEEtran',
         ...    'document_options': ['10pt', 'conference', 'letterpaper']
         ... }
         >>> sizes_dict = get_document_sizes(document_class)
         >>> pprint(sizes_dict)
         {'Huge': 24.0,
          'LARGE': 17.0,
          'Large': 14.0,
          'columnwidth': 252.0,
          'footnotesize': 8.0,
          'huge': 20.0,
          'large': 12.0,
          'normalsize': 10.0,
          'scriptsize': 7.0,
          'small': 9.0,
          'textwidth': 516.0,
          'tiny': 5.0}

    Returns:
        A dictionary containing sizes
        - columnwidth
        - textwidth
        - tiny
        - scriptsize
        - footnotesize
        - small
        - normalsize
        - large
        - Large
        - LARGE
        - huge
        - Huge
    """
    sizes_file = next(tempfile._get_candidate_names()) + '.txt'
    size_command = r"""
    \newwrite\sizesfile
    
    \makeatletter
    \newcommand\getsizes{%
        \openout\sizesfile=""" + sizes_file + r"""

        \write\sizesfile{columnwidth=\the\columnwidth}%

        \write\sizesfile{textwidth=\the\textwidth}%

        \newlength{\textsizetiny}
        \tiny a \setlength{\textsizetiny}{\f@size pt}
        \write\sizesfile{tiny=\the\textsizetiny}%

        \newlength{\textsizescript}
        \scriptsize a \setlength{\textsizescript}{\f@size pt}
        \write\sizesfile{scriptsize=\the\textsizescript}%

        \newlength{\textsizefoot}
        \footnotesize a \setlength{\textsizefoot}{\f@size pt}
        \write\sizesfile{footnotesize=\the\textsizefoot}%

        \newlength{\textsizesmall}
        \small a \setlength{\textsizesmall}{\f@size pt}
        \write\sizesfile{small=\the\textsizesmall}%

        \newlength{\textsizenormal}
        \normalsize a \setlength{\textsizenormal}{\f@size pt}
        \write\sizesfile{normalsize=\the\textsizenormal}%

        \newlength{\textsizelarge}
        \large a \setlength{\textsizelarge}{\f@size pt}
        \write\sizesfile{large=\the\textsizelarge}%

        \newlength{\textsizeLarge}
        \Large a \setlength{\textsizeLarge}{\f@size pt}
        \write\sizesfile{Large=\the\textsizeLarge}%

        \newlength{\textsizeLARGE}
        \LARGE a \setlength{\textsizeLARGE}{\f@size pt}
        \write\sizesfile{LARGE=\the\textsizeLARGE}%

        \newlength{\textsizehuge}
        \huge a \setlength{\textsizehuge}{\f@size pt}
        \write\sizesfile{huge=\the\textsizehuge}%

        \newlength{\textsizeHuge}
        \Huge a \setlength{\textsizeHuge}{\f@size pt}
        \write\sizesfile{Huge=\the\textsizeHuge}%

        \closeout\sizesfile
    }
    \makeatother
    """
    temp_doc_name = next(tempfile._get_candidate_names())
    
    if 'packages' in document_class:
        packages = document_class['packages']
        del document_class['packages']
    else:
        packages = []

    doc = Document(temp_doc_name, **document_class)
    doc.packages = packages
    doc.preamble.append(NoEscape(size_command))
    doc.append(Command('title', 'Title'))
    doc.append(Command('maketitle'))
    doc.append('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam c'
               'onsectetur volutpat tellus vel ultricies. Donec ullamcorper or'
               'ci quis ante volutpat efficitur. Aenean at rhoncus nibh. Morbi'
               ' vitae justo velit. Curabitur eget condimentum quam, nec accum'
               'san nulla. Nam tempor sem id tellus consectetur condimentum. N'
               'ullam id lacus purus. Nam nisi nisi, tempus ac ligula luctus, '
               'mollis volutpat odio. Mauris euismod mi nec rutrum tempor.\n'
               * 20)
    doc.append(NoEscape(r'\getsizes'))
    doc.generate_pdf(temp_doc_name)
    os.remove(temp_doc_name + '.pdf')

    with open(sizes_file, 'r') as f:
        lines = f.read().splitlines()

    sizes_dict = {}
    for l in lines:
        variable, value = l.split('=')
        sizes_dict[variable] = float(value[0:-2])

    os.remove(sizes_file)

    return sizes_dict
