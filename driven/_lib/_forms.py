# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import

import dash_html_components as html

#####################################################################
# LABELS
#####################################################################
def display_value_in_label(value_range, label_text, precision=0):
    float_format = '{{:.{}f}}'.format(precision)
    single_value_format = float_format
    range_value_format = '[{} ; {}]'.format(float_format, float_format)

    if value_range:

        if value_range[0] == value_range[1]:
            return label_text.format(
                single_value_format.format(value_range[0]))
        else:
            return label_text.format(
                range_value_format.format(value_range[0], value_range[1]))
    else:
        return label_text

#####################################################################
# MARKS
#####################################################################

def style_mark(
        value,
        order=0,
        unit='',
        color='#f50'):
    """
    """
    return dict(
        label='100 m',
        style={'color': '#f50'})

#####################################################################
# WRAP DCC ELEMENTS
#####################################################################
def wrap_dcc_element(
    ):
    return
