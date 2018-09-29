import pandas as pd 
import numpy as np 
import csv
with open('hmda_lar.csv', 'r') as data:
    csv_reader = csv.reader(data)

    for line in data:
        print(line)
