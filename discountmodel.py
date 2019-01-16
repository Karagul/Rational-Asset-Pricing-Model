import numpy
import numpy as np
import pandas
from xml.dom import minidom
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize
from statsmodels.formula.api  import ols
import statsmodels.formula.api as smf

def iterator(x):
    df = x
    rlist = []
    for i in range(15,len(df)):
        frame = df[:i]
        price = price0(frame)
        rlist.append(price)
    return rlist
        
        
def price0(X):
    dataframe = X
    time = dataframe[dataframe.columns[1]]
    expp = (dataframe[dataframe.columns[-1]])

    ## fitting model every iteration 
    results = smf.ols('I(np.log(expp)) ~ time + I(time**2)', data=dataframe).fit()

    values = []
    rrate = []
    for i in range(200):
        rrate.append(np.sum((results.params[1]+2*(i+time.iloc[-1])*results.params[2])*np.exp((results.params[0] + (i+time.iloc[-1])*results.params[1]+ ((i+time.iloc[-1])**2)*results.params[2] ))))
        values.append(np.exp(np.sum(results.params[0] + (i+(time.iloc[-1]))*results.params[1] + ((i+time.iloc[-1])**2)*results.params[2] )))

    def sumdiv():
        lisrate = []
        newrate = 1
        for i, val in enumerate(rrate):
            newrate = newrate*(1 + abs(val))
            lisrate.append(newrate)

        sum1 = 0
        for i, val in enumerate(values):
            value = val / lisrate[i]
            sum1=sum1+value
        return sum1
    price = sumdiv()
    return price