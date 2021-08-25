# -*- coding: utf-8; py-indent-offset:4 -*-

import pandas as pd
import akshare as ak

def download_cn_fund_list(param= None, verbose= False):
    df = ak.fund_em_open_fund_daily()
    return df

def download_cn_fund_info(symbol, indicator):
    df = ak.fund_em_open_fund_info(symbol, indicator)
    return df

def download_cn_etf_fund_list(param= None, verbose= False):
    df = ak.fund_em_etf_fund_daily()
    return df

def download_cn_etf_fund_info(symbol):
    df = ak.fund_em_etf_fund_info(symbol)