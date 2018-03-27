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
# document_classes.py

from pylatex import Package, NoEscape

ieee_infocom = {
    'documentclass': 'IEEEtran',
    'document_options': ['10pt', 'conference', 'letterpaper']
}

ieee_conf = {
    'documentclass': 'IEEEtran',
    'document_options': ['conference']
}

ieee_conf_compsoc = {
    'documentclass': 'IEEEtran',
    'document_options': ['conference', 'compsoc']
}

ieee_jrnl = {
    'documentclass': 'IEEEtran',
    'document_options': ['journal']
}

ieee_jrnl_compsoc = {
    'documentclass': 'IEEEtran',
    'document_options': ['10pt', 'journal', 'compsoc']
}

ieee_jrnl_comsoc = {
    'documentclass': 'IEEEtran',
    'document_options': ['journal', 'comsoc']
}

ieee_jrnl_transmag = {
    'documentclass': 'IEEEtran',
    'document_options': ['journal', 'transmag']
}

acm_sigconf = {
    'documentclass': 'acmart',
    'document_options': 'sigconf'
}

usenix = {
    'documentclass': 'article',
    'document_options': ['letterpaper','twocolumn','10pt'],
    'packages': [Package(NoEscape('usenix'))],
}

sbc = {
    'documentclass': 'article',
    'document_options': ['12pt'],
    'packages': [Package(NoEscape('sbc-template'))],
    'data': [NoEscape(r'\address{a}')]
}
