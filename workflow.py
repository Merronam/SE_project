import pandas as pd
import us_vis
import glob

while True:
    if input("Do you want to visualize all pictures w/o 
            modifying? y/n ") == "y":
        list=glob.glob("*.csv")
        for i in list:
            data=pd.read_csv(i, na_values = "inf")
            data2, work_columns2 = us_vis.vis.col_names(data)
            data3 = us_vis.vis.sub_min(data2, work_columns2)
            us_vis.vis.vis_save(data3, work_columns2, i.replace(".csv", ""))
    else:
        break

while True:
    if input("Do you want to modify pictures? y/n ") == "y":
        filename = input("Enter name of input file: ")
        if input("Does your data have column names? y/n ") == "y":
            data=pd.read_csv(filename+".csv", na_values="inf", skiprows = [0])
        else:
            data = pd.read_csv(filename+".csv", na_values="inf")
        data2, work_columns2 = us_vis.vis.col_names(data)
        data3 = us_vis.vis.sub_min(data2, work_columns2)
        us_vis.vis.vis_show(data3, work_columns2, "test")
        odd_out1 = us_vis.vis.odd_col(data3, work_columns2)
        if input('Do you want to delete columns? y/n ') == 'y':
            columns=input(f"Which columns do you want to delete (Type number 
                    1 to {len(work_columns2)} separated by space) ")
            work_columns2 = us_vis.vis.del_col(work_columns2, columns)
        us_vis.vis.vis_save(data3, work_columns2, filename)
        us_vis.vis.spread(data3, odd_out1)
    else: 
        break

while True:
    if input("Do you want to merge files? y/n ") == "y":
        pics = input("The names of the pictures without file extension 
                (or hit double enter to finish) ")
        columns = int(input("How many pictures should there be horizontally? "))
        name = input("Insert name of the output file: ")
        pics = us_vis.vis.split_strings(pics)
        pics = us_vis.merge.list_pics(pics)
        us_vis.merge.merge_pics(pics, columns, name)
    else:
        break
