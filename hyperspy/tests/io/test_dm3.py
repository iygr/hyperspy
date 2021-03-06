# -*- coding: utf-8 -*-
# Copyright 2007-2011 The Hyperspy developers
#
# This file is part of  Hyperspy.
#
#  Hyperspy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
#  Hyperspy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with  Hyperspy.  If not, see <http://www.gnu.org/licenses/>.


import os

import numpy as np
from generate_dm_testing_files import data_types

from nose.tools import assert_true
from hyperspy.io import load

my_path = os.path.dirname(__file__)

# When running the loading test the data of the files that passes it are 
# stored in the following dict. 
# TODO: fixtures should be used instead...
data_dict = {   'dm3_1D_data' : {},
                'dm3_2D_data' : {},
                'dm3_3D_data' : {},}

def test_loading():
    dims = range(1,4)
    for dim in dims:
        subfolder = 'dm3_%iD_data' % dim
        for key in data_types.iterkeys():
            fname = "test-%s.dm3" % key
            filename = os.path.join(my_path, subfolder, fname)
            yield check_load, filename, subfolder, key

def test_dtypes():
    subfolder = 'dm3_1D_data'
    for key,data in data_dict[subfolder].iteritems():
        yield check_dtype, data.dtype, np.dtype(data_types[key]), key

## TODO: the RGB data generated is not correct        
def test_content():
    for subfolder in data_dict:
        if subfolder == 'dm3_1D_data':
            dat = np.arange(1,3)
        elif subfolder == 'dm3_2D_data':
            dat = np.arange(1,5).reshape(2,2)
        elif subfolder == 'dm3_3D_data':
            dat = np.arange(1,9).reshape(2,2,2)
        for key,data in data_dict[subfolder].iteritems():
            dat = dat.astype(data_types[key])
            yield check_content, data, dat, subfolder, key

def check_load(filename, subfolder, key):
    try:
        s = load(filename)
        ok = True
        # Store the data for the next tests
        data_dict[subfolder][key] = s.data
    except:
        ok = False
    assert_true(ok == True, msg = 'loading %s\\test-%i' % (subfolder, key))
    
def check_dtype(d1, d2, i):
    assert_true(d1 == d2, msg = 'test_dtype-%i' % i)

def check_content(dat1, dat2, subfolder, key):   
    assert_true(np.all(dat1 == dat2) == True, msg = 'content %s type % i' % 
    (subfolder, key))
