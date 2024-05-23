"""
File: main.py
Author: Chuncheng Zhang
Date: 2024-05-23
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Amazing things

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-05-23 ------------------------
# Requirements and constants
import mne
import numpy as np
import pandas as pd
import plotly.express as px

from util.read_files import read_files
from IPython.display import display


# %% ---- 2024-05-23 ------------------------
# Function and class
files = read_files()
display(files)

# %%
# %%
path = files.loc[4, 'path']

selected = files[files['stem'].map(lambda s: s.startswith('jichangkai'))]
path = selected.iloc[0]['path']
print(path)

epochs = mne.io.read_epochs_eeglab(path)
epochs

# %% ---- 2024-05-23 ------------------------
# Play ground
evoked = epochs.average()
# evoked.plot()
# fig = epochs[0].plot()

# %%
data = evoked.data
times = evoked.times
ch_names = evoked.info['ch_names']
print(data.shape, times.shape)

x_array = []
y_array = []
ch_array = []
for ch, d in zip(ch_names, data):
    x_array.append(times)
    y_array.append(d)
    ch_array.append([ch] * len(d))

x_array = np.concatenate(x_array)
y_array = np.concatenate(y_array)
ch_array = np.concatenate(ch_array)
print(x_array, y_array, ch_array)
df = pd.DataFrame()
df['x'] = x_array
df['y'] = y_array
df['ch'] = ch_array

display(df)

px.line(df, x='x', y='y', color='ch', title=path.name)


# %% ---- 2024-05-23 ------------------------
# Pending


# %% ---- 2024-05-23 ------------------------
# Pending
