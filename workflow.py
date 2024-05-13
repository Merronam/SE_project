import pandas as pd
import matplotlib.pyplot as plt
import itertools
import us_vis

while True:
    if input("Do you want to modify pictures? y/n ") == "y":
        filename=input("Enter name of input file: ")
        data=pd.read_csv("test.csv", na_values="inf")
        data2, work_columns2=us_vis.vis.col_names(data)
        data3=us_vis.vis.sub_min(data2, work_columns2)
        odd_out1=us_vis.vis.odd_col(data3,work_columns2)
        columns = "1 2 3"
        work_columns3=us_vis.vis.del_col(work_columns2, columns)
        us_vis.vis.vis_save(data3,work_columns3,"filename")
        us_vis.vis.spread(data3, odd_out1)
    else: 
        break
