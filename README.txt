This is a series of script that allow to visualize and modify graphs obtain through umbrella sampling calculations from AMBER (https://ambermd.org/index.php) and WHAM (http://membrane.urmc.rochester.edu/?page_id=126) software. The required libraries are: subprocess, PIL, math, pandas, matplotlib and itertools.  

File path should be specififed if the file is not in the same directory as the scripts and file name should be specified without .csv or .png extensions. 

The visualization_function.py script perform basic transformation of the files, shows preliminary picture to the user, asks if user want to delete some columns that stand out and informs if the spread of the lines below x<2 is high (which is imoportant from chemical point of view). 

The merge.py script merges created files according to the input provided by the user, asks how many columns and what the name should be. 

Each script can be run separately, however the main.py script combines these two scripts together to provide smooth performance and workload. 
