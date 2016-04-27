#!/usr/bin/env python
# -*- coding: utf8 -*-
from os import path as op
from unqlite import UnQLite
from functools import wraps


def kv_storage(fn):
    @wraps(fn)
    def decorated(inst, *args, **kwargs):
        try:
            inst._kvs.open()
            return fn(inst, *args, **kwargs)
        finally:
            inst._kvs.close()
    return decorated


class KVStorage(object):
    """docstring for KVStorage"""
    _kvs = None

    def __init__(self, kvs_file):
        if not op.exists(kvs_file):
            open(kvs_file, 'a').close()

        super(KVStorage, self).__setattr__('_kvs', UnQLite(kvs_file))

    @kv_storage
    def __getattr__(self, key):
        try:
            return self._kvs[key]
        except KeyError:
            raise AttributeError("type object '{}' has no attribute '{}'".format(self.__class__.__name__, key))

    @kv_storage
    def __setattr__(self, key, value):
        self._kvs[key] = value

    @kv_storage
    def __delattr__(self, key):
        del self._kvs[key]
