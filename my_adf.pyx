import cython
import numpy as np
from statsmodels.tsa.stattools import adfuller

cpdef tuple adf_test(arr):
    """
    进行ADF检验并输出结果。

    参数:
    timeseries (array_like): 要进行ADF检验的时间序列数据。

    返回:
    tuple
    """
    result = adfuller(arr, autolag='AIC')

    # print(f'ADF Statistic: {result[0]}')
    # print(f'p-value: {result[1]}')
    # print(f'Lags Used: {result[2]}')
    # print(f'Number of Observations Used: {result[3]}')

    my_result = (result[0], result[1], result[2], result[3])

    return my_result