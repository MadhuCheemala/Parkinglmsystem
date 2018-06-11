# -*- coding: utf-8 -*-
""" AMP AI exception and warning classes """
import sys
import traceback
import linecache


class DataPrepException(Exception):
    """ Handles data preparation exceptions """

    def __init__(self, arg):
        self.msg = arg


class DbconException(Exception):
    """ Handles data preparation exceptions """

    def __init__(self, arg):
        self.msg = arg

class PortsException(Exception):
    """ Handles data preparation exceptions """

    def __init__(self, arg):
        self.msg = arg

class NotebookPrepException(Exception):
    """ Handles data preparation exceptions """

    def __init__(self, arg):
        self.msg = arg


class LogerException(Exception):
    """ Handles data preparation exceptions """

    def __init__(self, arg):
        self.msg = arg

def format_exception():
    """ Formats the exception in a readable string """

    exc_type, exc_obj, tb_exp = sys.exc_info()
    f_frame = tb_exp.tb_frame
    lineno = tb_exp.tb_lineno
    filename = f_frame.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f_frame.f_globals)
    val = ' ({}, LINE {} "{}"): {}'.format(
        filename, lineno, line.strip(), exc_obj)
    return val # + '\n' + traceback.format_tb(tb_exp)
