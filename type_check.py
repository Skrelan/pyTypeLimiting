"""
Yes, Python 2.7 does have the isinstance() method, but that doesn't wrap
 raising an error nor does it take more than one instance at a time.

 This package aims to help with that.
"""


def __worker(t, arg):
    if type(arg) != t:
        raise TypeError("Expected type {} given {} : {}".format(
            t, arg, type(arg)))


def type_int(*args):
    for arg in args:
        __worker(int, arg)


def type_float(*args):
    for arg in args:
        __worker(float, arg)


def type_long(*args):
    for arg in args:
        __worker(long, arg)


def type_complex(*args):
    for arg in args:
        __worker(complex, arg)


def type_bool(*args):
    for arg in args:
        __worker(bool, arg)


def type_chr(*args):
    for arg in args:
        __worker(chr, arg)


def type_str(*args):
    for arg in args:
        __worker(str, arg)


def type_list(*args):
    for arg in args:
        __worker(list, arg)


def type_tuple(*args):
    for arg in args:
        __worker(tuple, arg)


def type_class(t, *args):
    for arg in args:
        if arg.__class__ != t:
            raise TypeError("Expected type {} given {} : {}".format(
                t, arg, type(arg)))
