#!/usr/bin/env python
# -*- coding=utf8 -*-

import datetime as dt
import scipy.stats
import numpy as np
import sys


class TimeProcess():
    @classmethod
    def conv_long_to_dtm(cls, dt_l):
        '''
        Convert long to datetime
        >>> conv_long_to_dtm(1486456336)
        2017-02-07 16:32:16
        '''
        return dt.datetime.fromtimestamp(dt_l)
        
    @classmethod
    def conv_dtm_to_long(cls, dtm):
        '''
        Convert datetime to long
        >>> conv_dtm_to_long(datetime.datetime(2017, 3, 31, 17, 13, 11))
        1490951591.0
        '''
        return dtm.timestamp()
    
    @classmethod
	def check_range(cls, df, col_ref_dtm, col_proc_dtm, time_range):
        '''
        def check_range(cls, df, col_ref_dtm, col_proc_dtm, time_range)
        Add columns for time ranges, indicating if processed datetime is
        within specified time range of reference datetime.
        
        df - data to be processed
        col_ref_dtm - column name of reference datetime
        col_proc_dtm - column name to be processed datetime
        time_range: list of time range, for example ['p3m', '5w', '7d']; added columns would be ['is_3m', 'is_5w', 'is_7d'].
        '''
        pass
        
class Stats():
    @classmethod
    def mode(cls, series):
        '''
        caclulate mode for the series which include nan.
        '''
        try:
            return scipy.stats.mode(series.dropna())[0][0]
        except IndexError:
            # (array([], dtype=...), array([], dtype=float64))
            return np.nan
            
    @classmethod
    def calc_nna_stats(cls, df, by, col, suf=None):
        '''
        Calculate Not NA statistics of specified column,
        that is, count, max, median, mean, min, mode of Not NaN records.
        Add suffix to new columns name if specified.
        
        Example:
        >>> BasicStats.calc_nna_stats(data, by='person_id', col='trade_money', suf='p3m').head(5)
        
                trade_money_nnacnt_p3m     trade_money_cnt_p3m     trade_money_nnarto_p3m     trade_money_max_p3m     trade_money_mean_p3m     trade_money_median_p3m     trade_money_min_p3m     trade_money_std_p3m
        person_id
        13821     120.0     120.0     1.0     8300.00     -0.000500     -50.000     -3500.00     1109.643982
        14118     179.0     179.0     1.0     9600.00     0.011173     -20.000     -5000.00     960.992158
        14142     112.0     112.0     1.0     3000.00     -0.048393     -17.000     -3000.00     702.466085
        14148     150.0     150.0     1.0     4000.00     -9.323800     -135.000     -3000.00     760.773323
        14156     607.0     607.0     1.0     33000.00     -5.831779     -100.000     -23449.00     2748.952585
        '''
        if suf is None:
            return df.groupby(by).agg({col: {'{}_nnacnt'.format(col): pd.Series.count,
                                             '{}_cnt'.format(col): len,
                                             '{}_nnarto'.format(col): cls.calc_nna_ratio,
                                             '{}_max'.format(col): cls.np_nanmax_series,
                                             '{}_mean'.format(col): np.nanmean,
                                             '{}_median'.format(col): np.nanmedian,
                                             '{}_min'.format(col): cls.np_nanmin_series,
                                             '{}_std'.format(col): cls.np.nanstd}})[col]
        else:
            return df.groupby(by).agg({col: {'{}_nnacnt_{}'.format(col, suf): pd.Series.count,
                                             '{}_cnt_{}'.format(col, suf): len,
                                             '{}_nnarto_{}'.format(col, suf): cls.calc_nna_ratio,
                                             '{}_max_{}'.format(col, suf): cls.np_nanmax_series,
                                             '{}_mean_{}'.format(col, suf): np.nanmean,
                                             '{}_median_{}'.format(col, suf): np.nanmedian,
                                             '{}_min_{}'.format(col, suf): cls.np_nanmin_series,
                                             '{}_std_{}'.format(col, suf): cls.np.nanstd}})[col]
                                             
    @classmethod
    def np_nanmax_series(cls, series):
        '''
        Numpy nanmax for pandas series,
        for bug (https://github.com/pandas-dev/pandas/issues/12383) in numpy.
        '''
        try:
            return np.nanmax(series).iloc[0]
        except ValueError:
            return np.nan
            
    @classmethod
    def np_nanmin_series(cls, series):
        '''
         Numpy nanmin for pandas series,
         for bug (https://github.com/pandas-dev/pandas/issues/12383) in numpy.
        '''
        try:
            return np.nanmin(series).iloc[0]
        except ValueError:
            return np.nan
            
    @classmethod
    def calc_nna_ratio(cls, series):
        '''
        Calculate Not NaN ratio for a series
        '''
        return series.count() / series.shape[0]
        
        
def trim(docstring):
    if not docstring:
        return ''
    # Convert tabs to spaces (following the normal Python rules)
    # and split into a list of lines:
    lines = docstring.expandtabs().splitlines()
    # Determine minimum indentation (first line doesn't count):
    indent = sys.maxsize
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))
    # Remove indentation (first line is special):
    trimmed = [lines[0].strip()]
    if indent < sys.maxsize:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())
    # Strip off trailing and leading blank lines:
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)
    # Return a single string:
    return '\n'.join(trimmed)
    
    
def qcutils():
    print('you are using qcutils')
    
    
def main():
    print(conv_long_to_dtm(1486456336))
    
    
if __name__ == "__main__":
    main()
