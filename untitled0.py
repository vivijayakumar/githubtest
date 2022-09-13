# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 08:52:10 2022

@author: vivijayakumar
"""

import pandas as pd
xls_aws = pd.ExcelFile(r'C:\Users\vivijayakumar\OneDrive - Deloitte (O365D)\Documents\AWS_Instance_Tracker.xlsx')

RAW = pd.read_excel(xls_aws, 'RAW')
RAW.columns.values
len(RAW)    


print(RAW.groupby('Instance State').groups)

ter = RAW.groupby('Instance State').get_group('terminated')
ru = RAW.groupby('Instance State').get_group('running')
stp = RAW.groupby('Instance State').get_group('stopped')
##Replace prod to production
RAW.replace(to_replace=r'^prod.$', value='Production', regex=True)

ter.count()
ru.count()
stp.count()

###############
averages = {}

# Split the data into different regions
for environment in RAW['environment']:
    tempdf1 = RAW[RAW['environment'] == environment]

    # Apply an aggregation function
    average = tempdf1['application'].count()

    # Combine the data into a DataFrame
    averages[environment] = [average]

aggregate_df = pd.DataFrame.from_dict(averages, orient='index', columns=['Total count'])
print(aggregate_df)

aggregate_df1 = aggregate_df.replace(to_replace=r'^prod.$', value='Pra', regex=True)




###Dashboard
#conda install hvplot panel pandas jupyterlab
from bokeh.sampledata.autompg import autompg_clean as df
import hvplot.pandas
import panel as pn
import holoviews as hv
hv.extension('bokeh')
pn.extension('tabulator')
PALETTE = ["#ff6f69", "#ffcc5c", "#88d8b0", ]

import sklearn
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer

import matplotlib.pyplot as plt


with plt.style.context(("seaborn","ggplot")):
    avg_radius_per_tumor_typ = aggregate_df

    plt.figure(figsize=(10,5))
    plt.bar(avg_radius_per_tumor_typ.index,
            avg_radius_per_tumor_typ["Total count"],
            color="tab:blue",
            width=1)
    plt.ylabel("Total count", rotation=0, fontsize=8)
    plt.title("Average mean radius per tumor type")

