import pandas as pd
import numpy as np
import os as os

print("works")

broken = []
healthy = []

pth1 = 'dataset/BrokenTooth'
pth2 = 'dataset/Healthy'

for file in os.listdir(pth1):
    broken.append(os.path.join(pth1, file))
broken.sort()

for file in os.listdir(pth2):
    healthy.append(os.path.join(pth2, file))
healthy.sort()

i = 0
for file in os.listdir(pth1):
    broken[i] = pd.read_csv(os.path.join(pth1, file))
    i += 1

j = 0
for file in os.listdir(pth2):
    healthy[j] = pd.read_csv(os.path.join(pth2, file))
    j += 1