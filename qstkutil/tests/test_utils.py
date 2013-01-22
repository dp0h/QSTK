'''
(c) 2011, 2012 Georgia Tech Research Corporation
This source code is released under the New BSD license.  Please see
http://wiki.quantsoftware.org/index.php?title=QSTK_License
for license details.

Created on May 14, 2012

@author: John Cornwell
@contact:  John@lucenaresearch.com
@summary: 

'''

import unittest
from test import test_support

import datetime as dt
import qstkutil.qsdateutil as du

class TestDateUtils(unittest.TestCase):
    """
    Test case for qsdateutil
    """

    def test_NYSEdates(self):
        du.GTS_DATES = None # reset cache

        res = du.getNYSEdays(startday = dt.datetime(2013, 4, 26), endday = dt.datetime(2013, 5, 6))
	self.assertEquals(7, len(res))

    def test_LSEdates(self):
        du.GTS_DATES = None # reset cache

        res = du.getStockExchangeDays(stock_exchange = "LSE", startday = dt.datetime(2013, 4, 26), endday = dt.datetime(2013, 5, 6))
	self.assertEquals(6, len(res))

if __name__ == "__main__":
	test_support.run_unittest(TestDateUtils)
    
