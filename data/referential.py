# -*- coding: utf-8 -*-

"""Create a referential database for the technical values."""

from __future__ import division, print_function, absolute_import

import sqlite3

#####################################################################
# SQL STATEMENTS
#####################################################################

with open('./view_bulk_material.sql', 'r') as query_file:
    READ_QUERY = query_file.read()

with open('./create_bulk_material.sql', 'r') as query_file:
    CREATE_QUERY = query_file.read() 

with open('./insert_bulk_material.sql', 'r') as query_file:
    INSERT_QUERY = query_file.read()

#####################################################################
# READ PRE-EXISTING DB
#####################################################################

with sqlite3.connect('./_referential.sqlite3') as old_db:
    cursor = old_db.cursor()
    product_catalog = [
        product for product in cursor.execute(READ_QUERY)]

#####################################################################
# CREATE & FILL NEW DB
#####################################################################

with sqlite3.connect('./referential.sqlite3') as new_db:
    cursor = new_db.cursor()
    cursor.execute(CREATE_QUERY)
    for product in product_catalog:
        cursor.execute(INSERT_QUERY, product[:15])
