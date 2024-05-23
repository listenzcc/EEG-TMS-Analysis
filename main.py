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

import seaborn as sns
import matplotlib.pyplot as plt

from util.read_files import read_files
from IPython.display import display


# %% ---- 2024-05-23 ------------------------
# Function and class


# %% ---- 2024-05-23 ------------------------
# Play ground

files = read_files()
display(files)

# %%
path = files.loc[4, 'path']

selected = files[files['stem'].map(lambda s: s.startswith('jichangkai'))]
path = selected.iloc[0]['path']
display(path)

epochs = mne.io.read_epochs_eeglab(path)
display(epochs)

# The shape of epochs_data is (n_epochs, channels, n_times)
# The shape of times is (n_times,)
epochs_data = epochs.get_data()
times = epochs.times
ch_names = epochs.info['ch_names']
display(epochs_data.shape, times.shape)

# %%
selected_times_map = [-0.01 < t < 0.01 for t in times]
selected_times = np.array(times[selected_times_map])
mat = epochs_data[:, 0, selected_times_map].squeeze()
display(mat.shape, selected_times.shape)

m = 100*1e-6
fig, ax = plt.subplots(1, 1)
sns.heatmap(mat, cmap='RdBu', vmax=m, vmin=-m, ax=ax)
ax.set_xticks(
    range(len(selected_times))[::10],
    selected_times[::10], rotation=45)
i = int(np.argwhere(selected_times == 0).squeeze())
ax.axvline(x=i, color='green', linewidth=2)
ax.text(x=i, y=0, s='x=0', ha='right', va='top', color='green')
ax.set_title(path.name)
fig.tight_layout()
plt.show()

# %% ---- 2024-05-23 ------------------------
# Pending


# %% ---- 2024-05-23 ------------------------
# Pending
