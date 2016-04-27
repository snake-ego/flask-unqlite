#!/usr/bin/env python
# -*- coding: utf8 -*-
from os import path as op
from .storage import KVStorage

__all__ = ['UnqliteKV']
__version__ = '0.5.1'


class UnqliteKV(object):
    """docstring for Unqlite"""

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app, **kwargs):
        kvs = app.config.get('UNQLITE_STORAGE_FILE', None)
        if kvs is None:
            raise AttributeError("You must set 'UNQLITE_STORAGE_FILE' in app configuration")
        if not op.exists(op.dirname(kvs)):
            raise ValueError("Coudn't find directory: '{}'".format(op.dirname(kvs)))

        app.extensions['kvstorage'] = KVStorage(kvs)
