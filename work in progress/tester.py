from parse import preprocess
import pandas as pd

# Pre-parse the dataset
data = preprocess("rawfile_blood.csv")

# Grouping Pre-frail, Frail, and Robust

# Grouping:
# Frail, Frail_MCI, --> Frail
# Prefrail_MCI, Prefrail --> Prefrail
# MCI, Robust --> Robust

for i in range(0, len(data)):
    if data.at[i, 'condition'] == 'frail':
        data.at[i, 'condition'] = 'frail'
    elif data.at[i, 'condition'] == 'frail_mci':
        data.at[i, 'condition'] = 'frail'
    elif data.at[i, 'condition'] == 'mci':
        data.at[i, 'condition'] = 'robust'
    elif data.at[i, 'condition'] == 'prefrail_mci':
        data.at[i, 'condition'] = 'prefrail'
    elif data.at[i, 'condition'] == 'prefrail':
        data.at[i, 'condition'] = 'prefrail'
    elif data.at[i, 'condition'] == 'robust':
        data.at[i, 'condition'] = 'robust'
        
c = data['condition'].value_counts()
condition = c.index

print(c)

data.to_csv("Frailty_rawfile_blood_parsed.csv", index=False)