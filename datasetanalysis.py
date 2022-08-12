# importing packages
import pandas as pd
import pandas_profiling as pp
import os

# forming dataframe and printing
data = pd.read_csv("Stockdata/HDFC.csv")
# print(data)
  
# forming ProfileReport and save
# as output.html file

profile = pp.ProfileReport(data)
profile.to_file("templates/dataanalysis.html")