# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.

import pandas as pd


with open('CFG.txt') as t:
    contents = t.read()

plick = "Eoin Cowhey V1.1.1."

filepath = "C:/Users/eoinc/OneDrive/Desktop/Test121.txt"

filepath2 = "C:/Users/eoinc/OneDrive/Desktop/Table121.txt"

# Negative indexing in lists
my_list = ['p', 'r', 'o', 'b', 'e']

string1="".join(map(str,my_list))

# last item
#print(string1)

def index_ESB(n):
   return [i for i in range(1,n+1)]
n = 1000
#print(index_ESB(n))

Times_t = pd.Series(index_ESB(n))/1000

print(Times_t)

Total = contents + plick + "\n" "EOIN C" #+ Times_t

#f = open("C:\Users\eoinc\OneDrive\Desktop\Test121.cfg", "w")   # 'r' for reading and 'w' for writing
#f.write("Eoin C V1.1" + f.name)    # Write inside file
#f.close()

with open(filepath, "w") as f:   # Opens file and casts as f
    f.write(Total)# + f.name)       # Writing
    # File closed automatically

#Times_t.to_csv(filepath2, index=False, header=False)

Times_tee = Times_t.to_string(header=False, index=False)

with open(filepath2, "w") as g:   # Opens file and casts as f
    g.write(Times_tee)

#Pandas List
#people_list = ['Jon','Mark','Maria','Jill','Jack']
#my_series = pd.Series(people_list)
#print(my_series)





