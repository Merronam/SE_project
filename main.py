#importing library that allows to run scripts through other python script and force them to wait and execute in order
import subprocess

#Visualizing plots according to user specifications
proc1 = subprocess.Popen(['python', 'visualization_function.py'])
proc1.wait()

#Merging plots according to user specifications
proc2 = subprocess.Popen(['python', 'merge.py'])
proc2.wait()
