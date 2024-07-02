#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 21:13:42 2019

@author: abhishekakshat
"""

# Data Pre-processing:

import pandas as pd
import glob

path = r'Data/downloaded' # use your path
all_files = glob.glob(path + "/*.tsv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None,sep='\t', encoding='latin-1', header=None, error_bad_lines=False)
    li.append(df)

data = pd.concat(li, axis=0, ignore_index=True)

data.columns=["ItemID","Sentiment","SentimentText","NaN"]
data.drop(['NaN'], axis=1, inplace=True)

data.to_csv('Combined-Twitter-Data.csv', sep='\t', encoding='utf-8', index=False)

