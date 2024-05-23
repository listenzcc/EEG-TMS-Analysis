"""
File: read_files.py
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
import pandas as pd

from pathlib import Path
from . import logger, data_folder


# %% ---- 2024-05-23 ------------------------
# Function and class

def read_files():
    files = [
        dict(ext=path.suffix, name=path.name, stem=path.stem, path=path)
        for path in data_folder.iterdir()
        if path.suffix == '.set'
    ]
    return pd.DataFrame(files)


# %% ---- 2024-05-23 ------------------------
# Play ground


# %% ---- 2024-05-23 ------------------------
# Pending


# %% ---- 2024-05-23 ------------------------
# Pending
