# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import

from decorator import decorator

@decorator
def memoize(func, *args, **kwargs):
    if not hasattr(func, 'cache'):
        func.cache = {}

    key = str(args) + str(kwargs)
    if key not in func.cache:
        func.cache[key] = func(*args, **kwargs)
    
    return func.cache[key]