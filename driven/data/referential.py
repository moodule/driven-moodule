# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import

import sqlite3

from driven._lib import *

#####################################################################
# PRODUCT DATA
#####################################################################
@memoize
def bulk_material_data():
    with sqlite3.connect('./driven/data/referential.sqlite3') as ref_db:
        cursor = ref_db.cursor()
        product_catalog = {
            product[0]: product[1:]
            for product in cursor.execute(
                """select id, name, average_density, surcharge_angle
                from bulk_material
                order by name
                limit 10;""")}

    return product_catalog