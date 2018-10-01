# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import

def display_value_in_label(value_range, label_text):
    if value_range and value_range:
        if value_range[0] == value_range[1]:
            return label_text.format(value_range[0])
        else:
            return label_text.format(
                '[{} ; {}]'.format(value_range[0], value_range[1]))
    else:
        return label_text
