# Import packages
import pandas as pd 
import numpy as np 
from parse import preprocess

df = preprocess("rawfile_blood.csv")

# Data Dictionary:
# frail -> 0
# frail_mci -> 1
# mci -> 2
# prefrail_mci -> 3
# prefrail -> 4
# robust -> 5

frail = 0
frail_mci = 0
mci = 0
prefrail_mci = 0
prefrail = 0
robust = 0

for i in range(0, len(df)):
	if df.at[i, 'condition'] == 'frail':
		frail += 1
		df.at[i, 'condition'] = 0
	elif df.at[i, 'condition'] == 'frail_mci':
		frail_mci += 1
		df.at[i, 'condition'] = 1
	elif df.at[i, 'condition'] == 'mci':
		mci += 1
		df.at[i, 'condition'] = 2
	elif df.at[i, 'condition'] == 'prefrail_mci':
		prefrail_mci += 1
		df.at[i, 'condition'] = 3
	elif df.at[i, 'condition'] == 'prefrail':
		prefrail += 1
		df.at[i, 'condition'] = 4
	elif df.at[i, 'condition'] == 'robust':
		robust += 1
		df.at[i, 'condition'] = 5

print("\n####################################################################")
print("Labels with frequencies:")
print("Frail:", frail)
print("Frail + MCI:", frail_mci)
print("MCI:", mci)
print("Prefrail + MCI:", prefrail_mci)
print("Prefrail:", prefrail)
print("Robust:", robust)

# Specify features and labels
y = df['condition'].astype('int')
x = df.drop(['mtag', 'condition'], axis=1)