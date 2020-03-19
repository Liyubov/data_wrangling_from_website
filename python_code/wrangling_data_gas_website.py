# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 08:56:25 2020

@author: lyubo
"""



import requests
import pandas as pd
from datetime import datetime




def gas_price(dls, savecsv):
    
    # monthly or daily price extraction    
    
    resp = requests.get(dls)
    
    output = open('price.xls', 'wb')
    output.write(resp.content)
    output.close()
        
    
    data = pd.read_excel (r'price.xls',sheet_name='Data 1')
    data.head()
    
    
    # delet first rows of data 
    data = data.iloc[2:]
    
    print(data.columns)
    #rename columns 
    data.columns = ['Date', 'Price']
    
    # make column Date in datetime format
    data['Date'] = pd.to_datetime(data['Date'])
    data.head()
    
    data.to_csv(savecsv)#, index = None, header=True)    
    
    return data

# for creating datapackage.json
# we use datapackage from https://pypi.org/project/datapackage/



if __name__ == '__main__':
    dls_day = "https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDm.xls"
    dls_mon = "https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDd.xls"

    save_day = "dailyprice.csv"
    save_mon = "monthlyprice.csv"
    
    gas_price(dls_day, save_day) # execute function for daily price
    gas_price(dls_mon, save_mon) # execute function for daily price
    