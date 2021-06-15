def RobustFrailMCIpreprocess(csvfile):

    # Import necessary libraries
    import pandas as pd
    import os
    import sys

    # Load CSV File
    df = pd.read_csv(csvfile)

    # df = df[df.condition != 'frail']
    # df = df.reset_index(drop=True)

    print(df['condition'].value_counts())

    print("\n####################################################################")
    print("Number of Rows of Dataframe:")
    print(len(df))
    print("Number of Columns of Dataframe:")
    print(len(df.columns))

    # If there are too many #NULL!s in a column, remove the column
    THRESHOLD = 0.1095

    print("\n####################################################################")
    print("Threshold for number of NULLs in a column:", THRESHOLD)
    name_of_column = []

    print("Number of Columns before Parsing for Too Many NULLs in a column:")
    print(len(df.columns))

    for i in range(0, len(df.columns)):
        count = 0
        for j in range(0, len(df)):
            # if (df.iat[j,i] == '#NULL!'):
            if ((df.iat[j,i] == '#NULL!') or (df.iat[j,i] == 'NIL')):
                count += 1
                if (count >= (len(df) * THRESHOLD)):
                    name_of_column.append(df.columns[i])
                    break

    df = df.drop(name_of_column, axis=1)

    print("Number of Columns after Parsing for Too Many NULLs in a column:")
    print(len(df.columns))

    print("\nColumns Removed:")
    for items in name_of_column:
        print(items)

    # # Drop B1_b4, B2_c3, B4_b2
    df = df.drop(['B1_b4', 'B2_c3', 'B4_b2'], axis=1)

    # df.to_csv("rawfile_blood_parsed.csv", index=False)
    
    print("\n####################################################################")
    print("Number of Columns after dropping B1_b4, B2_c3, B4_b2 for inconsistent data types:")
    print(len(df.columns))

    # If there are #NULL!s in any data for any rows/columns, remove the whole row
    list_of_removables = []

    print("\n####################################################################")
    print("Number of Rows before Parsing NULLs in data:")
    print(len(df))

    for i in range(0, len(df)):
        for j in range(0, len(df.columns)):
            if df.iat[i,j] == '#NULL!':
                list_of_removables.append(i)

    list_of_removables = list(dict.fromkeys(list_of_removables))

    df = df.drop(list_of_removables)

    print("Number of Rows after Parsing NULLs in data:")
    print(len(df))

    df.to_csv("rawfile_robust_frailmci_parsed.csv", index=False)

    # For column 'B1_a1', data dictionary indicates ranges should be around 4.50 - 6.50 for normal
    # Dataset has cells that indicate exponent values(e12).
    # Action: Divide values exceeding 10 by 10e12
    df = pd.read_csv("rawfile_robust_frailmci_parsed.csv")

    df['B1_a1'] = df['B1_a1'].astype(float)

    for i in range(0, len(df)):
        temp = df.at[i,'B1_a1']
        if (temp > 10):
            df.at[i,'B1_a1'] = temp / 1000000000000.0

    # For column 'B1_b', data dictionary indicates ranges should be around 4.0 - 11.0
    # Action: Divide values exceeding 100 by 10e9
    df['B1_b'] = df['B1_b'].astype(float)

    for i in range(0, len(df)):
        temp = df.at[i, 'B1_b']
        if (temp > 100):
            df.at[i,'B1_b'] = temp / 1000000000.0
    
    # Repeat for other columns
    df['B1_b1'] = df['B1_b1'].astype(float)

    for i in range(0, len(df)):
        temp = df.at[i, 'B1_b1']
        if (temp > 100):
            df.at[i,'B1_b1'] = temp / 1000000000.0

    df['B1_b2'] = df['B1_b2'].astype(float)

    for i in range(0, len(df)):
        temp = df.at[i, 'B1_b2']
        if (temp > 100):
            df.at[i,'B1_b2'] = temp / 1000000000.0
    
    df['B1_b3'] = df['B1_b3'].astype(float)

    for i in range(0, len(df)):
        temp = df.at[i, 'B1_b3']
        if (temp > 100):
            df.at[i,'B1_b3'] = temp / 1000000000.0

    #NOTE: B1_b4 unsure

    df['B1_c'] = df['B1_c'].astype(float)

    for i in range(0, len(df)):
        temp = df.at[i, 'B1_c']
        if (temp > 100):
            df.at[i,'B1_c'] = temp / 1000000000.0

    # Just want to parse the <0.1 for B3

    for i in range(0, len(df)):
        temp = df.at[i, 'B3']
        temp = temp.replace(' ', '')
        if ((temp == '<0.1') or (temp == '<.1')):
            df.at[i,'B3'] = 0.05

    df['B3'] = df['B3'].astype(float)

    df.to_csv("rawfile_robust_frailmci_parsed.csv", index=False)
    
    return df