import pandas as pd
import matplotlib.pyplot as plt
import itertools
import us_vis

#if input("Do you want to modify pictures? y/n ") == "y":
#input as a command line prompt - no inside names as easy to confuse and not so easily applicable
    #filename=input("Enter name of input file: ")
    #data=pd.read_csv(filename+".csv", na_values="inf")

data=pd.read_csv("test.csv", na_values="inf")
data2, work_columns2=us_vis.vis.col_names(data)
data3=us_vis.vis.sub_min(data2, work_columns2)
ax = us_vis.vis.vis_fun(data3,work_columns2,"naming")
us_vis.vis.vis_save(data3,work_columns2,"naming")
odd_out1=us_vis.vis.odd_col(data3,work_columns2)
columns = "1 2 3"
work_columns3=us_vis.vis.del_col(work_columns2, columns)
us_vis.vis.vis_save(data3,work_columns3,"delere")
us_vis.vis.spread(data3, odd_out1)
