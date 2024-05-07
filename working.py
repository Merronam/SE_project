import pandas as pd
import matplotlib.pyplot as plt
import itertools
import tools.vis

#if input("Do you want to modify pictures? y/n ") == "y":
#input as a command line prompt - no inside names as easy to confuse and not so easily applicable
    #filename=input("Enter name of input file: ")
    #data=pd.read_csv(filename+".csv", na_values="inf")

data=pd.read_csv("test.csv", na_values="inf")
data2, work_columns2=tools.vis.col_names(data)
data3=tools.vis.sub_min(data2, work_columns2)
ax = tools.vis.vis_fun(data3,work_columns2)
tools.vis.odd_col(data3,work_columns2)
