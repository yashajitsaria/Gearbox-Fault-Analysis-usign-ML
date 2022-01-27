import pandas as pd
import numpy as np
import math
import os as os

broken = []
healthy = []

pth1 = 'dataset/BrokenTooth'
pth2 = 'dataset/Healthy'

i = 0
for file in os.listdir(pth1):
    broken.append(pd.read_csv(os.path.join(pth1, file)))
    print(broken[i].head())
    i += 1

j = 0
for file in os.listdir(pth2):
    healthy.append(pd.read_csv(os.path.join(pth2, file)))
    print(healthy[j].head())
    j += 1

def stdev_features(df, grouped, load, outcome):
    #### Create empty dataframe with columns a1,a2,a3,a4
    df_result = pd.DataFrame( [ np.zeros(len(df.columns)-2) ],columns= df.columns[:-2])

    #### Aggregate in groups of nrows computing the standard deviation
    # Remove load & failure columns, keeping only a1,a2,a3,a4
    stdev_lenght=len(df.columns)-2
    
    #### Compute number of rows of the aggregated dataframe
    nrows_raw = len(df.index)
    nrows = math.floor(nrows_raw / grouped)
    nrows_dropped = nrows_raw - nrows*grouped
    print("nrows_raw=", nrows_raw, "   nrows=", nrows, "   Number of dropped rows of grouped= ", nrows_dropped/grouped*100,"%\n")
    
    # Iterate every 'grouped' rows and compute stdev per column
    for i in range(nrows):
        df_group = df.iloc[i*grouped:i*grouped+grouped,:]
        df_stdev = pd.DataFrame(df_group.std()).transpose()
        # Remove load & failure columns
        df_stdev=df_stdev.iloc[:,:stdev_lenght]
        # Add row of calculated stdev
        df_result = df_result.append(df_stdev, ignore_index=True)

        #print ("i*grouped TO i*grouped+grouped", i*grouped, i*grouped+grouped)
        #print ("row, df_stdev=\n", row, df_stdev.iloc[:,:])
        #print ("df_result=\n", df_result)
        #print("row", i, "\n", df_group)


    # Remove the first row (it was the seed of zeros for initializing df_result)
    #print(df_result)
    df_result = df_result.iloc[1:,:]
    # Add the column for 'load'
    df_result['load'] = load*np.ones((nrows,1))

    # Add the column for 'failure'
    failure = np.ones((nrows,1))
    df_result['failure'] = outcome
    print(df_result)
    
    return df_result

grouped = 100
broken_stdev = []
healthy_stdev = []

for i in range(len(broken)):
    load = 10*i
    broken[i]["load"] = load
    failure = 1
    broken[i]['failure'] = failure
    
    broken_stdev.append(stdev_features (df = broken[i], grouped = grouped, load = load, outcome = failure))

