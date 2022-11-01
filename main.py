# Power Swing Blocking Test Tool V1.00
#
# Developed by Eoin Cowhey
# Copyright Eoin Cowhey 2022

import pandas as pd

Name_version = "PSB Shishe V1.00"

Header = Name_version + ", '1997'"
Output_Types = "'6', '6A', '0D'"

#OP_No = ['1', '2', '3', '4', '5', '6']
#OP_Name = ['VL1', 'VL2', 'VL3', 'VL4', 'VL5', 'VL6']
#OP_Units = ['V', 'V', 'V', 'A', 'A', 'A']
#OP_Mult = ['0.029303126', '0.029303126', '0.029303126', '0.001465144', '0.001465144', '0.001465144']
#OP_Min = ['-59.99814949', '-59.99814949', '-59.99814949', '-2.99988224', '-2.99988224', '-2.99988224']
#OP_Skew = ['0', '0', '0', '0', '0', '0']
#OP_Bits = ['4095', '4095', '4095', '4095', '4095', '4095']
#OP_Prim = ['2.20E+05', '2.20E+05', '2.20E+05', '2.50E+03', '2.50E+03', '2.50E+03']
#OP_Sec = ['1.00E+02', '1.00E+02', '1.00E+02', '1.00E+00', '1.00E+00', '1.00E+00']
#OP_Rec = ['s', 's', 's', 's', 's', 's']

#Outputs = pd.DataFrame([OP_No, OP_Name, OP_Units, OP_Mult, OP_Min, OP_Skew, OP_Bits, OP_Prim, OP_Sec, OP_Rec])
#print(Outputs)

Output_1 = ['1', 'VL1', '5', 'A', '0.029303126', '-59.99814949', '0.00E+00', '0', '4095', '2.20E+05', '1.00E+02', 's']
Output_2 = ['2', 'VL2', '6', 'A', '0.029303126', '-59.99814949', '0.00E+00', '0', '4095', '2.20E+05', '1.00E+02', 's']
Output_3 = ['3', 'VL3', '7', 'A', '0.029303126', '-59.99814949', '0.00E+00', '0', '4095', '2.20E+05', '1.00E+02', 's']
Output_4 = ['4', 'IL1', '162', 'A', '0.001465144', '-2.99988224', '0.00E+00', '0', '4095', '2.50E+03', '1.00E+00', 's']
Output_5 = ['5', 'IL2', '163', 'A', '0.001465144', '-2.99988224', '0.00E+00', '0', '4095', '2.50E+03', '1.00E+00', 's']
Output_6 = ['6', 'IL3', '164', 'A', '0.001465144', '-2.99988224', '0.00E+00', '0', '4095', '2.50E+03', '1.00E+00', 's']

Outputs = pd.DataFrame([Output_1, Output_2, Output_3, Output_4, Output_5, Output_6])
print(Outputs)

System_Frequency = "50.00"
Next = "1"
Sampling_Rate = "'1000', '2000'"
Trigger_Time = "'04/08/2022', '21:56:50'"
Stop_Time = "'04/08/2022', '21:56:52'"
Main_Format = "ASCII"
Final = "1.0"

#Outputs = Output_1# + "\n" + Output_2 + "\n" + Output_3 + "\n" + Output_4 +"\n" + Output_5 +"\n" + Output_6


#Total = Header #+ "\n" + Output_Types + "\n" + Outputs + "\n" + System_Frequecy + "\n" + Sampling_Rate + "\n" + Trigger_Time + "\n" + Stop_Time + "\n" + Main_Format + "\n" + Final


with open('CFG.txt') as t:
    contents = t.read()


filepath = "C:/Users/eoinc/OneDrive/Desktop/Test121.txt"

filepath2 = "C:/Users/eoinc/OneDrive/Desktop/Table121.txt"



# last item
#print(string1)

def index_ESB(n):
   return [i for i in range(1,n+1)]
n = 1000
#print(index_ESB(n))

Times_t = pd.Series(index_ESB(n))/1000

print(Times_t)



#f = open("C:\Users\eoinc\OneDrive\Desktop\Test121.cfg", "w")   # 'r' for reading and 'w' for writing
#f.write("Eoin C V1.1" + f.name)    # Write inside file
#f.close()

Output_s = Outputs.to_string(header=False, index=False)
Output_x = Header + "\n" + Output_Types + "\n" + Output_s + "\n" + System_Frequency + "\n" + Next + "\n" + Sampling_Rate + "\n" + Trigger_Time + "\n" + Stop_Time + "\n" + Main_Format + "\n" + Final

print(Output_x)

with open(filepath, "w") as f:   # Opens file and casts as f
    f.write(Output_x)# + f.name)       # Writing
    # File closed automatically

#Times_t.to_csv(filepath2, index=False, header=False)

Times_tee = Times_t.to_string(header=False, index=False)

with open(filepath2, "w") as g:   # Opens file and casts as f
    g.write(Times_tee)

#Pandas List
#people_list = ['Jon','Mark','Maria','Jill','Jack']
#my_series = pd.Series(people_list)
#print(my_series)





