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
# helpers.py

import matplotlib as mpl


class RCParamWrapper(object):
    """Matplotlib object wrapper for nonglobal RCParams.

    This wraps Matplotlib objects which allows us set RCparams per object.
    Optionally can use a function that returns an object so that the object is
    lazy initialized

    Attributes:
        obj: A matplotlib object or a function that returns such object
        rc: Matplotlib RCparams
    """
    def __init__(self, obj, rc):
        if callable(obj):  # lazy initialization
            self.lazy_obj = obj
            self.obj = None
        else:
            self.obj = obj
            self.lazy_obj = None
        self.rc = RCParams(rc)

    def __getattr__(self, item):
        if self.obj is None:
            with mpl.rc_context(rc=self.rc.get_rc_to_function(item)):
                self.obj = self.lazy_obj()

        attr = getattr(self.obj, item)

        if not callable(attr):
            return attr

        # the following function wraps whatever method is being called in an
        # rc_context, this enforces the rcparams while being transparent to the
        # user

        def method(*args, **kwargs):
            with mpl.rc_context(rc=self.rc.get_rc_to_function(item)):
                return attr(*args, **kwargs)

        return method


def dict_select(my_dict, term, expect=True):
    return {k: v for k, v in my_dict.items() if expect == k.startswith(term)}


class RCParams(object):
    """Handle plot-specific rcParams

    Stores rcParams, optionally filtering plot-specific options.

    Args:
        rc_dict: rcParams style dict. With plot-specific options prepended with
                 the plot type.

    Attributes:
        rc_dict: rcParams style dict. With plot-specific options prepended with
                 the plot type.

    """

    def __init__(self, rc_dict):
        if isinstance(rc_dict, RCParams):
            self.rc_dict = rc_dict.rc_dict
        else:
            self.rc_dict = rc_dict

    def get_rc_to_function(self, func):
        plain_rc = dict_select(self.rc_dict, ':', expect=False)
        func_rc = dict_select(self.rc_dict, ':{}:'.format(func))
        func_opt_len = len(func)+2
        func_rc = {k[func_opt_len:]: v for k, v in func_rc.items()}
        plain_rc.update(func_rc)
        return plain_rc
