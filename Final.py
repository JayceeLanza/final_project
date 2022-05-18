import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import pandas as pd
import seaborn as sns
import scipy as syp
import pingouin as pg
from statsmodels.stats.multicomp import pairwise_tukeyhsd

def shapiro_func(list_df,x):
    Norm=[]
    for df in list_df:
        norms = (syp.stats.shapiro(df[x]))
        Norm.append(norms)
    return(Norm)


def histograms(list_df, x):
    for df in list_df:
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(1,1,1)
        hists = ax1.hist(df['SporophytesperFemale'])
    return(hists);