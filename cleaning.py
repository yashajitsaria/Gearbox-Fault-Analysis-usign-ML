from matplotlib.pyplot import axis
import pandas as pd
import numpy as np
import math
import matplotlib as plt
import os as os

# Creating empty list for broken tooth and healthy gearbox datasets
broken = []
healthy = []

# Defining the path where the datasets are stored
pth1 = 'dataset/BrokenTooth'
pth2 = 'dataset/Healthy'

# Reading the dataset as the list items using the OS library to access the files and read_csv function from pandas to read the daatasets 
i = 0
for file in os.listdir(pth1):
    broken.append(pd.read_csv(os.path.join(pth1, file)))
    #print(broken[i].head())
    i += 1
    
j = 0
for file in os.listdir(pth2):
    healthy.append(pd.read_csv(os.path.join(pth2, file)))
    #print(healthy[j].head())
    j += 1

# Adding load and broken/healthy information to the dataset
for i in range(0, 10):
    load = 10*i
    # failure = 1, refers the gearbox is faulty while failure = 0, refers to healthy gearbox
    broken[i]['load'] = load
    broken[i]['failure'] = 1
    healthy[i]['load'] = load
    healthy[i]['failure'] = 0

# Aggregating dataset for broken and healthy
healthy_agg = healthy[0]
broken_agg = broken[0]
for i in range(1,10):
    healthy_agg = healthy_agg.append(healthy[i], ignore_index=True)
    broken_agg = broken_agg.append(broken[i], ignore_index=True)

# Agregrating total dataset
healthy_broken_agg = pd.concat([healthy_agg, broken_agg], axis=0, ignore_index=True)

