#!/usr/bin/env python
# -*- coding=utf8 -*-


import datetime as dt
import scipy.stats
import numpy as np


def conv_long_to_dtm(dt_l):
    '''
    Convert long to datetime
    >>> conv_long_to_dtm(1486456336)
    2017-02-07 16:32:16
    '''
    return dt.datetime.fromtimestamp(dt_l)
    
    
def trim(docstring):
    if not docstring:
        return ''
    # Convert tabs to spaces (following the normal Python rules)
    # and split into a list of lines:
    lines = docstring.expandtabs().splitlines()
    # Determine minimum indentation (first line doesn't count):
    indent = sys.maxint
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))
    # Remove indentation (first line is special):
    trimmed = [lines[0].strip()]
    if indent < sys.maxint:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())
    # Strip off trailing and leading blank lines:
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)
    # Return a single string:
    return '\n'.join(trimmed)
    
#caclulate mode for the series which include nan.
def mode(series):
    try:
        return scipy.stats.mode(series.dropna())[0][0]
    except IndexError:
        # (array([], dtype=...), array([], dtype=float64))
        return np.nan
                                    
def main():
    print(conv_long_to_dtm(1486456336))


if __name__ == "__main__":
    main()
