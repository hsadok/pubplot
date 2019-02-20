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
from pylatex import Document, NoEscape, Command, Package
import tempfile
import subprocess
import glob

LATEX_BUILT_IN_SIZES = ['tiny', 'scriptsize', 'footnotesize', 'small',
                        'normalsize', 'large', 'Large', 'LARGE', 'huge', 'Huge']
LOG_PATTERN = '<<<>>>'

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
          'caption': 8.0,
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
          'caption': 8.0,
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
        - caption
    """

    def log_with_name(name, value):
        return '\\wlog{{{}{}={}}}'.format(LOG_PATTERN, name, value)

    def log_text_size(text_size_name):
        return '\\{} a {} \n\n'.format(text_size_name,
            log_with_name(text_size_name, r'\f@size pt'))

    get_sizes_command = r"""
    \makeatletter
    \newcommand\getsizes{%
        """ + log_with_name('columnwidth', r'\the\columnwidth') + r"""
        """ + log_with_name('textwidth', r'\the\textwidth') + r"""

        \begin{figure}
            \centering
            \fbox{
                \begin{minipage}[c][0.1\textheight][c]{\columnwidth}
                \centering{Dummy Image}
                \end{minipage}
            }
            \caption{a """ + log_with_name('caption', r'\f@size pt') + r""" }
        \end{figure}

    """
    for size in LATEX_BUILT_IN_SIZES:
        get_sizes_command += log_text_size(size)

    get_sizes_command += '}'

    temp_doc_name = next(tempfile._get_candidate_names())

    document_kwargs = document_class.copy()
    packages = document_kwargs.pop('packages', [])

    doc = Document(temp_doc_name, **document_kwargs)
    doc.packages = packages
    doc.preamble.append(NoEscape(get_sizes_command))
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
    
    try:
        doc.generate_pdf(temp_doc_name, clean=False)
    except subprocess.CalledProcessError:
        pass

    with open(temp_doc_name + '.log', 'r') as f:
        lines = f.read().splitlines()

    sizes_dict = {}
    for l in lines:
        if l.startswith(LOG_PATTERN):
            variable, value = l.split('=')
            variable = variable[len(LOG_PATTERN):]
            sizes_dict[variable] = float(value[0:-2])

    list(map(os.remove, glob.glob(temp_doc_name + '.*')))

    return sizes_dict
