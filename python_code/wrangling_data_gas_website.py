# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 08:56:25 2020

@author: lyubo
"""



import requests
import pandas as pd
from datetime import datetime




def monthlyprice():
    
    # monthly price
    dls = "https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDm.xls"
    resp = requests.get(dls)
    
    output = open('monthlyprice.xls', 'wb')
    output.write(resp.content)
    output.close()
    
    
    
    data = pd.read_excel (r'monthlyprice.xls',sheet_name='Data 1')
    data.head()
    
    
    # delet first rows of data 
    data = data.iloc[2:]
    
    print(data.columns)
    #rename columns 
    data.columns = ['Date', 'Price']
    
    # make column Date in datetime format
    data['Date'] = pd.to_datetime(data['Date'])
    data.head()
    
    data.to_csv(r'monthlyprice_1.csv')#, index = None, header=True)    
    
    return data


if __name__ == '__main__':
    monthlyprice() # execute function