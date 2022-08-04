# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.

import pandas as pd

with open('CFG.txt') as t:
    contents = t.read()

plick = "Eoin Cowhey V1.1.1."

filepath = "C:/Users/eoinc/OneDrive/Desktop/Test121.cfg"


Total = contents + plick

#f = open("C:\Users\eoinc\OneDrive\Desktop\Test121.cfg", "w")   # 'r' for reading and 'w' for writing
#f.write("Eoin C V1.1" + f.name)    # Write inside file
#f.close()

with open(filepath, "w") as f:   # Opens file and casts as f
    f.write(Total)# + f.name)       # Writing
    # File closed automatically


#print(Total)



