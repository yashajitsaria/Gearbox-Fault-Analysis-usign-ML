import pandas as pd
import numpy as np
import math
import os as os

#creating empty list for broken tooth and healthy gearbox datasets
broken = []
healthy = []

#defining the path where the datasets are stored
pth1 = 'dataset/BrokenTooth'
pth2 = 'dataset/Healthy'

#reading the dataset as the list items using the OS library to access the files and read_csv function from pandas to read the daatasets 
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
    