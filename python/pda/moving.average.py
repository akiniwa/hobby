#! coding: utf-8

import matplotlib.pyplot as plt
import statsmodels.api as sm


def rolling_window():
    """rolling_window
    http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.rolling.html
    """
    dl = sm.datasets.sunspots.load_pandas()
    df = dl.data
    year_range = df['YEAR'].values
    plt.plot(year_range, df['SUNACTIVITY'].values, label='original')
    plt.plot(year_range, df['SUNACTIVITY'].rolling(
        window=11, center=False).mean(), label='sma 11')
    plt.plot(year_range, df['SUNACTIVITY'].rolling(
        window=22, center=False).mean(), label='sma 22')
    plt.legend()
    plt.show()


def rolling_window_type():
    """rolling_window_type"""
    # The recognized window types are:
    win_types = [
        'boxcar',
        'triang',
        'blackman',
        'hamming',
        'bartlett',
        # 'parzen',
        # 'bohman',
        # 'blackmanharris',
        # 'nuttall',
        # 'barthann',
        # 'kaiser',
        # 'gaussian',
        # 'general_gaussian',
        # 'slepian',
    ]

    dl = sm.datasets.sunspots.load_pandas()
    df = dl.data
    year_range = df['YEAR'].values
    plt.plot(year_range, df['SUNACTIVITY'].values, label='original')
    for win_type in win_types:
        plt.plot(year_range, df['SUNACTIVITY'].rolling(
            window=11, win_type=win_type).mean(), label=win_type)
    plt.legend()
    plt.show()

rolling_window_type()
