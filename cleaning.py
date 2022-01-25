#import pandas as pd
#import numpy as np
import os as os

print("works")

b30 = []
blist = []
h30 = []
hlist = []

pth1 = 'dataset/BrokenTooth'
pth2 = 'dataset/Healthy'

for file in os.listdir(pth1):
    blist.append(os.path.join(pth1, file))
blist.sort()
print(blist)

for file in os.listdir(pth2):
    hlist.append(os.path.join(pth2, file))
hlist.sort()
print(hlist)
