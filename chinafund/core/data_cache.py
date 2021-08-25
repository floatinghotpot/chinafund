# -*- coding: utf-8; py-indent-offset:4 -*-

import os
import time
import datetime as dt
import pandas as pd

from ..utils import get_file_modify_time, datetime_today, symbol_normalize, symbol_market, dict_from_df

from ..data_source import *

def get_cached_download_df(csv_file, download_func, param = None, check_date = None):
    if type(param) == str:
        csv_file = csv_file.replace('{param}', param)

    # like ^GSPC.csv, will cause trouble when manually delete
    csv_file = csv_file.replace('^','_').replace('$','_')

    need_update = False
    if os.path.isfile(csv_file):
        if check_date is not None:
            modified_time = get_file_modify_time(csv_file)
            need_update = modified_time < check_date
        else:
            need_update = False
    else:
        need_update = True

    if need_update:
        for i in range(3):
            try:
                df = download_func(param)
            except (ValueError, IndexError) as err:
                _DOWNLOAD_RETRY_DELAY = 300
                print('downloading failed, try again after {} min'.format(_DOWNLOAD_RETRY_DELAY // 60))
                time.sleep(_DOWNLOAD_RETRY_DELAY)
                df = None

            if df is not None:
                df.to_csv(csv_file, index= bool(df.index.name))
                return df

        if df is None:
            print('downloading failed after 3 tries, loading cached data')

    df = pd.read_csv(csv_file, dtype=str)
    return df

def get_cn_fund_list():
    return get_cached_download_df('cache/cn_fund_list.csv', download_cn_fund_list, check_date= datetime_today())
