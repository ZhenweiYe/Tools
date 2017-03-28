#!/usr/bin/env python
# -*- coding=utf8 -*-


import datetime as dt


def conv_long_to_dtm(dt_l):
    '''
    convert long to datetime
    >>> conv_long_to_dtm(1486456336)
    Outputs:
    2017-02-07 16:32:16

    '''
    return dt.datetime.fromtimestamp(dt_l)


def main():
    print(conv_long_to_dtm(1486456336))


if __name__ == "__main__":
    main()
