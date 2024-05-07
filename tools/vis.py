import pandas as pd
import matplotlib.pyplot as plt
import itertools

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

def sub_min(data, work_columns):
    for i in work_columns:
        new_col=[]
        for j in data[i]:
            k=j-data[(data["Coord"]>=2.0)][i].min()
            new_col.append(k)
        data[i]=new_col
    return data

def vis_fun(data, work_columns):
    Ncolors = len(work_columns)
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
    plt.savefig("graph.png")
    return ax

