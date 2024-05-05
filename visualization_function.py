#importing basic libraries
import pandas as pd
import matplotlib.pyplot as plt
import itertools

while True:
    if input("Do you want to modify pictures? y/n ") == "y":
#input as a command line prompt - no inside names as easy to confuse and not so easily applicable
        filename=input("Enter name of input file: ")
#filename="test_test_columns"

#read data, assume that 'inf' are NaN; since column names may differ between runs (sometimes its "US10, US20..." and sometimes its "US1, US2...") the column names for further visualisation are gives by the loop below for consistency
        data=pd.read_csv(filename+".csv", na_values="inf")
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

#Primar transformation of a data - looking for minimum and shifting the data up/down
#Get a minimum value in each "US" column and then substract it from all rows - shifting all columns 
#find minimum
        for i in work_columns:
            new_col=[]
            for j in data[i]:
                k=j-data[(data["Coord"]>=2.0)][i].min()
                new_col.append(k)
            data[i]=new_col


#plot rough figure - adjust so the xaxis is in y=0 - colours based on answers from: https://stackoverflow.com/questions/8931268/using-colormaps-to-set-color-of-line-in-matplotlib
        Ncolors = 10
        colormap = plt.cm.Set3 #choosing colormaps
        mapcolors = [colormap(int(x*colormap.N/Ncolors)) for x in range(Ncolors)]
        l_styles = ['-'] #if in the future I want to change linestyle
        m_styles = [''] #if in the future I want to add marker
        fig,ax = plt.subplots(gridspec_kw=dict(right=0.85))
        for i,(marker,linestyle,color) in zip(work_columns,itertools.product(m_styles,l_styles, mapcolors)):
            ax.plot(data["Coord"],data[i], color=color, linestyle=linestyle,marker=marker,label=i)
        plt.xlim(1.4,3.5)
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.spines['bottom'].set_position('zero')
        plt.title("Pre-delete plot")
        fig.legend(loc="right", ncol=1,prop={'size': 8})
        plt.show()
        plt.savefig("graph.png")

#Odd graphs out - if one specific line stands out too much from the rest that is the sign that this one run should be recalculated. The code below informs user about  that
        odd_out=[]
        for i in work_columns:
            odd=[]
            for j in range(1,len(data[(data["Coord"]>=2.5)][i])):
                if data[(data["Coord"]>=2.0)].loc[j+14,i] > data[(data["Coord"]>=2.0)].loc[j+14-1,i]:
                    odd.append("1")
            if len(odd)>10:
                odd_out.append(i)
                print(f"You might need to recalculate {i}")

        if input('Do you want to delete columns? y/n ') == 'y':
            columns=input(f"Which columns do you want to delete (Type number 1 to {len(work_columns)} separated by space) ")
            delete_columns=columns.split(" ")
            delete_columns=["US"+str(eval(i)*10) for i in delete_columns]
            work_columns=[i for i in work_columns if i not in delete_columns]
            del_col=[]
            for i in delete_columns: 
                loc=data.columns.get_loc(i)
                loc_list=[loc-1,loc]
                del_col.extend(loc_list)
            data.drop(data.columns[del_col], axis=1, inplace=True)

# If the spread of the graphs, after deleting outstanding lines, in x<=2 is bigger than 20 kcal/mol - print a warning 
        min=data[(data["Coord"]<=2.0)].loc[5,"US10"].min()
        max=data[(data["Coord"]<=2.0)].loc[5,"US10"].max()
        for i in [i for i in list(data.columns.values) if i not in odd_out]:
            new_min=data[(data["Coord"]<=2.0)].loc[5,i].min()
            new_max=data[(data["Coord"]<=2.0)].loc[5,i].max()
            if new_min<min:
                min=new_min
            if new_max>max:
                max=new_max
            diff=max-min
        if diff > 20:
            print("The spread is high")

#plot final figure 
        Ncolors = len(work_columns)
        colormap = plt.cm.Set3 #choosing colormaps
        mapcolors = [colormap(int(x*colormap.N/Ncolors)) for x in range(Ncolors)]
        l_styles = ['-'] #if in the future I want to change linestyle
        m_styles = [''] #if in the future I want to add marker
        fig1,ax = plt.subplots(gridspec_kw=dict(right=0.85))
        for i,(marker,linestyle,color) in zip(work_columns,itertools.product(m_styles,l_styles, mapcolors)):
            ax.plot(data["Coord"],data[i], color=color, linestyle=linestyle,marker=marker,label=i)
        plt.xlim(1.4,3.5)
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.spines['bottom'].set_position('zero')
        fig1.legend(loc="right", ncol=1,prop={'size': 8})
        title=input("What is the title of the plot? ")
        plt.title(title)
        fig1.savefig(filename+".png")
        plt.show()
        
    else:
        break
