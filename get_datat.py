#!/usr/bin/env python3
split = 20* "#####"
print(split)
print('Generating data for the test')
import numpy as np 
import pandas as pd 
import os 
print(split)
print('Creating directory for the dataasets')
data = 'Data'
small_file  = f'{data}/data_small.csv'
medium_file = f'{data}/data_medium.csv'
large_file  = f'{data}/data_large.csv'
url = 'https://data.wprdc.org/datastore/dump/2c13021f-74a9-4289-a1e5-fe0472c89881?bom=True'
print(split)
print(f'Creating directory {data} for the dataasets')
try: 
    os.mkdir(data)
except Exception as E:
    print(str(E))
    pass
print(split)
print(f'Downloading original dataset.\n url = {url}')
df = pd.read_csv(url, low_memory = False)
print(split)
print('Generating dataframes with different sizes')
dfs = df.head(22000)
dfm = df.head(220000)
dfl = pd.concat([dfm, dfm], axis = 0)
print(f'Dataframes shapes:\n\t Original: \t {df.shape} \n\t Small: \t {dfs.shape} \n\t Medium: \t {dfm.shape} \n\t Large: \t {dfl.shape}')
print(split)
print(f'Saving files to {data}')
dfs.to_csv(small_file, index = False)
dfm.to_csv(medium_file, index = False)
dfl.to_csv(large_file, index = False)
print('Calculating files size in MB')
sm_size = np.round(os.stat(small_file).st_size / (1024 * 1024), 2)
md_size = np.round(os.stat(medium_file).st_size / (1024 * 1024), 2)
lg_size = np.round(os.stat(large_file).st_size / (1024 * 1024), 2)
print(f'Small (22K records, {sm_size} MB), medium (220K records, {md_size} MB) and large (440K records, {lg_size} MB) datasets created from {url} in {data} folder. \nTry running the Pandas Alternative Notebook(s) now')
print(split)
