# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import

from decorator import decorator

@decorator
def memoize(func, *args, **kwargs):
    if not hasattr(func, '__cache__'):
        func.__cache__ = {}

    key = str(args) + str(kwargs)
    if key not in func.__cache__:
        func.__cache__[key] = func(*args, **kwargs)
    
    return func.__cache__[key]