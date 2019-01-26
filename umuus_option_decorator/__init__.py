#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Jun Makii <junmakii@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""Utilities, tools, and scripts for Python.

umuus-option-decorator
======================

Installation
------------

    $ pip install git+https://github.com/junmakii/umuus-option-decorator.git

Example
-------

    $ umuus_option_decorator

    >>> import umuus_option_decorator

    >>> @umuus_option_decorator.decorator() 
    ... def f(x, options): print(x, options)

    >>> f(1)
    1 {'x': 1}

    >>> f(x=1)
    1 {'x': 1}

    >>> f(options=dict(x=1))
    1 {'x': 1}

    >>> f(options={'x': 1})
    1 {'x': 1}

Authors
-------

- Jun Makii <junmakii@gmail.com>

License
-------

GPLv3 <https://www.gnu.org/licenses/>

"""
import sys
import functools
import addict
import toolz
import inspect
__version__ = '0.1'
__url__ = 'https://github.com/junmakii/umuus-option-decorator'
__author__ = 'Jun Makii'
__author_email__ = 'junmakii@gmail.com'
__author_username__ = 'junmakii'
__keywords__ = []
__license__ = 'GPLv3'
__scripts__ = []
__install_requires__ = [
    'toolz>=0.9.0',
    'addict>=2.2.0',
]
__dependency_links__ = []
__classifiers__ = []
__entry_points__ = {}
__project_urls__ = {}
__setup_requires__ = []
__test_suite__ = ''
__tests_require__ = []
__extras_require__ = {}
__package_data__ = {}
__python_requires__ = ''
__include_package_data__ = True
__zip_safe__ = True
__static_files__ = {}
__extra_options__ = {}
__download_url__ = ''
__all__ = []


@toolz.curry
def decorator(fn, **default_kw):
    spec = inspect.getfullargspec(fn)

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            _args = dict(zip(spec.args[:len(args)], args))
            _options = functools.reduce(lambda a, b: (a.update(b), a)[-1], (
                default_kw,
                _args,
                kwargs,
                kwargs.get('options', {}),
            ), addict.Dict())
            return fn(
                *args, **{
                    key: value
                    for key, value in (
                        [] + list(dict(options=_options).items()) +
                        list(_options.items()) + list(_args.items()))
                    if key in spec.args and key not in spec.args[:len(args)]
                    or spec.varkw
                })
        except Exception as err:
            raise err

    return wrapper


if __name__ == '__main__':
    sys.exit(main(sys.argv))
