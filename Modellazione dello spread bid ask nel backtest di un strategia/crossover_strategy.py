# Import necessary modules
import os
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# stocks_data_filename = 'equity_trade_and_quotes_1min.csv'
stocks_data_filename = 'equity_trade_and_quotes.csv'
df = pd.read_csv(stocks_data_filename, parse_dates=True, index_col=0)
df.index.name = 'Date_'
df = df.between_time('9:40', '15:50')