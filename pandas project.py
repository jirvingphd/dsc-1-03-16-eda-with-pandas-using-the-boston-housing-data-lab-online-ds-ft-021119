# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:38:42 2019

@author: james
"""

#import pandas as pd
#df=pd.read_csv('train.csv')
#
#df.head()

import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

df = pd.read_csv('turnstile_180901.txt')
print(len(df))
df.head()


cleaned = col_name.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
def clean(col_name):
   cleaned = [col_name.lower() for col_name in df.columns]
#     cleaned = col_name.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
   return cleaned