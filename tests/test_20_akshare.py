# -*- coding: utf-8; py-indent-offset:4 -*-

from chinafund.data_source import *
from chinafund.core.data_cache import *

def test_akshare():
    df = get_cn_fund_list()
    print(df)

if __name__ == "__main__":
    df = test_akshare()
