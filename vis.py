#importing basic libraries
import pandas as pd
import matplotlib.pyplot as plt
import itertools

if input("Do you want to modify pictures? y/n ") == "y":
#input as a command line prompt - no inside names as easy to confuse and not so easily applicable
    filename=input("Enter name of input file: ")
    data=pd.read_csv(filename+".csv", na_values="inf")

def col_names(data):
    column_names=[]
    work_columns=[]
    j=10
    for i in range(1,(data.shape[1]+1)):
        if i == 1:
            column_names.append("Coord")
        elif (i%2)==0:
            column_names.append("US"+str(j))
            work_columns.append("US"+str(j))
            j+=10
        elif (i%2)==1:
            column_names.append("")
    data.columns=column_names
    return data, work_columns

data2, work_columns2=col_names(data)

def sub_min(data, work_columns):
    for i in work_columns:
        new_col=[]
        for j in data[i]:
            k=j-data[(data["Coord"]>=2.0)][i].min()
            new_col.append(k)
        data[i]=new_col
    return data

data3=sub_min(data2, work_columns2)
