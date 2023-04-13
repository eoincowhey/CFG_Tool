# Power Swing Blocking Test Tool V1.00
# Developed by Eoin Cowhey
# Copyright Eoin Cowhey 2022/2023

import pandas as pd
import numpy as np
import math
import tkinter as tk
from tkinter import messagebox
#################GUI#######################

root = tk.Tk()
root.geometry("900x600")
root.title("Power Swing Blocking 2.0")

Version = tk.StringVar()
S1_Freq = tk.StringVar()
S2_Freq = tk.StringVar()
Nom_Voltage = tk.StringVar()
Fault_Voltage = tk.StringVar()
Imp_Start = tk.StringVar()
Imp_Finish = tk.StringVar()
S1_Volt_Phase_Angle = tk.StringVar()
S2_Volt_Phase_Angle = tk.StringVar()
S1_Current_Phase_Angle = tk.StringVar()
S2_Current_Phase_Angle = tk.StringVar()
Swing_Time = tk.StringVar()

#Default Values
Version.set("PSB Shishe V1.00")
S1_Freq.set("50")
S2_Freq.set("49.5")
Nom_Voltage.set("57.74")
Fault_Voltage.set("30")
Imp_Start.set("60")
Imp_Finish.set("22")
S1_Volt_Phase_Angle.set("0")
S2_Volt_Phase_Angle.set("0")
S1_Current_Phase_Angle.set("0")
S2_Current_Phase_Angle.set("180")
Swing_Time.set("2")

Label_Ver = tk.Label(root, font=('Arial',10), text='Program Version:')
Ver_entry = tk.Entry(root, font=('Arial',10), textvariable=Version)
Label_1 = tk.Label(root, font=('Arial',10), text='Source 1 Frequency:')
S1_entry = tk.Entry(root, font=('Arial',10), textvariable=S1_Freq)
Units_1 = tk.Label(root, font=('Arial',10), text='Hz')
Label_2 = tk.Label(root, font=('Arial',10), text='Source 2 Frequency:')
S2_entry = tk.Entry(root, font=('Arial',10), textvariable=S2_Freq)
Units_2 = tk.Label(root, font=('Arial',10), text='Hz')
Label_3 = tk.Label(root, font=('Arial',10), text='Healthy Voltage:')
S3_entry = tk.Entry(root, font=('Arial',10), textvariable=Nom_Voltage)
Units_3 = tk.Label(root, font=('Arial',10), text='V')
Label_4 = tk.Label(root, font=('Arial',10), text='Fault Voltage:')
S4_entry = tk.Entry(root, font=('Arial',10), textvariable=Fault_Voltage)
Units_4 = tk.Label(root, font=('Arial',10), text='V')
Label_5 = tk.Label(root, font=('Arial',10), text='Start Impedance:')
S5_entry = tk.Entry(root, font=('Arial',10), textvariable=Imp_Start)
Units_5 = tk.Label(root, font=('Arial',10), text='Ohms')
Label_6 = tk.Label(root, font=('Arial',10), text='Finish Impedance:')
S6_entry = tk.Entry(root, font=('Arial',10), textvariable=Imp_Finish)
Units_6 = tk.Label(root, font=('Arial',10), text='Ohms')
Label_7 = tk.Label(root, font=('Arial',10), text='Source 1 Voltage Phase Angle:')
S7_entry = tk.Entry(root, font=('Arial',10), textvariable=S1_Volt_Phase_Angle)
Units_7 = tk.Label(root, font=('Arial',10), text='deg')
Label_8 = tk.Label(root, font=('Arial',10), text='Source 2 Voltage Phase Angle:')
S8_entry = tk.Entry(root, font=('Arial',10), textvariable=S2_Volt_Phase_Angle)
Units_8 = tk.Label(root, font=('Arial',10), text='deg')
Label_9 = tk.Label(root, font=('Arial',10), text='Source 1 Current Phase Angle:')
S9_entry = tk.Entry(root, font=('Arial',10), textvariable=S1_Current_Phase_Angle)
Units_9 = tk.Label(root, font=('Arial',10), text='deg')
Label_10 = tk.Label(root, font=('Arial',10), text='Source 2 Current Phase Angle:')
S10_entry = tk.Entry(root, font=('Arial',10), textvariable=S2_Current_Phase_Angle)
Units_10 = tk.Label(root, font=('Arial',10), text='deg')
Label_11 = tk.Label(root, font=('Arial',10), text='Swing Time:')
S11_entry = tk.Entry(root, font=('Arial',10), textvariable=Swing_Time)
Units_11 = tk.Label(root, font=('Arial',10), text='sec')



#Positioning
Label_Ver.place(x=25, y=20)
Ver_entry.place(x=225, y=20)
Label_1.place(x=25, y=120)
S1_entry.place(x=225, y=120)
Units_1.place(x=375, y=120)
Label_2.place(x=450, y=120)
S2_entry.place(x=650, y=120)
Units_2.place(x=800, y=120)
Label_7.place(x=25, y=170)
S7_entry.place(x=225, y=170)
Units_7.place(x=375, y=170)
Label_8.place(x=450, y=170)
S8_entry.place(x=650, y=170)
Units_8.place(x=800, y=170)
Label_9.place(x=25, y=220)
S9_entry.place(x=225, y=220)
Units_9.place(x=375, y=220)
Label_10.place(x=450, y=220)
S10_entry.place(x=650, y=220)
Units_10.place(x=800, y=220)
Label_3.place(x=25, y=270)
S3_entry.place(x=200, y=270)
Units_3.place(x=350, y=270)
Label_4.place(x=25, y=320)
S4_entry.place(x=200, y=320)
Units_4.place(x=350, y=320)
Label_5.place(x=25, y=370)
S5_entry.place(x=200, y=370)
Units_5.place(x=350, y=370)
Label_6.place(x=25, y=420)
S6_entry.place(x=200, y=420)
Units_6.place(x=350, y=420)
Label_11.place(x=25, y=520)
S11_entry.place(x=200, y=520)
Units_11.place(x=350, y=520)


def myClick():

    def val_entry(inp):
        try:
            float(inp)
        except:
            return False
        return True

    Datacheck = val_entry(S1_Freq.get()) and val_entry(S2_Freq.get()) and val_entry(Swing_Time.get())
    Datacheck = Datacheck and val_entry(Nom_Voltage.get()) and val_entry(Fault_Voltage.get())
    Datacheck = Datacheck and val_entry(Imp_Start.get()) and val_entry(Imp_Finish.get())
    Datacheck = Datacheck and val_entry(S1_Volt_Phase_Angle.get()) and val_entry(S1_Current_Phase_Angle.get())
    Datacheck = Datacheck and val_entry(S2_Volt_Phase_Angle.get()) and val_entry(S2_Current_Phase_Angle.get())

    if Datacheck == False:
        messagebox.showwarning("Number Validation", "Enter number and can not be blank")


myButton = tk.Button(root, text="Validate Entry Information", command=myClick)
myButton.place(x=425, y=20)

root.mainloop()

##################GUI######################

Name_version = Version.get()#"PSB Shishe V1.00"

Header = Name_version + "," + "1997"
Output_Types = "6,6A,0D"

# Input information
Source_1_Freq = float(S1_Freq.get())
Source_2_Freq = float(S2_Freq.get())
V_Nom = float(Nom_Voltage.get())
V_Fault = float(Fault_Voltage.get())
Z_Finish = float(Imp_Finish.get())
Z_Start = float(Imp_Start.get())
Source_1_Voltage_Phi = float(S1_Volt_Phase_Angle.get())
Source_2_Voltage_Phi = float(S2_Volt_Phase_Angle.get())
Source_1_Current_Phi = float(S1_Current_Phase_Angle.get())
Source_2_Current_Phi = float(S2_Current_Phase_Angle.get())
T_swing = float(Swing_Time.get())

# Instrument Transformers
VT_Primary = 220
VT_Secondary = 100
CT_Primary = 2500
CT_Secondary = 1
CT_Star_Point = "Busbar"

VTP = format(VT_Primary * 1000, '.2E')
VTS = format(VT_Secondary, '.2E')
CTP = format(CT_Primary, '.2E')
CTS = format(CT_Secondary, '.2E')


# Calc values
T_for_1_swing = 1/(Source_1_Freq-Source_2_Freq)
Source_V1 = V_Fault+(V_Nom-V_Fault)/2
Source_V2 = (V_Nom-V_Fault)/2
Source_I1 = ((V_Fault/Z_Finish)-(((V_Fault/Z_Finish)-(V_Nom/Z_Start))/2))
Source_I2 = (((V_Fault/Z_Finish)-(V_Nom/Z_Start))/2)
Z_rate = ((Z_Start-Z_Finish)/T_swing)/2
I_minimum = Source_I1-Source_I2

if CT_Star_Point == "Busbar":
    Busbar_comp = 180
else:
    Busbar_comp = 0


# Fault record process data
Recording_bits = 12
Recording_decimal = (2**Recording_bits)-1
Sample_rate = 1000  # e.g. 10 kHz
No_of_samples = T_swing * Sample_rate
Sample_t_res = 1/Sample_rate


# Functions

# Function 1: used to generate lists for sample number and sample time stamp
# k = offset, samples = max value limit, delta = delta sample

def list_range(k, samples, delta):
    result = list()
    while k <= samples:
        result.append(k)
        k += delta
    return (result)


def Inst(Source, freq, df, phi, phase, starpoint):
    return(Source * np.sin((2 * math.pi * freq * df) + math.radians(phi) + math.radians(phase)
                           + math.radians(starpoint)))

def int_conv(df, Min, Range, Rec_dec):
    return((((df - Min)/Range) * Rec_dec).astype('int'))

def frame_op(No1, Name, No2, var, Mult, Min, Rec_dec, ITP, ITS):
    return([No1, ',', Name, ',', No2, ', ', ',', var, ',', Mult, ',', Min, ',', '0.00E+00', ',', '0', ',',
            Rec_dec, ',', ITP, ',', ITS, ',', 's'])



# Process Samples

Sample_No = list_range(0, No_of_samples, 1)
Time_Stamp = list_range(Sample_t_res, (No_of_samples * Sample_t_res), Sample_t_res)


Calcs = pd.DataFrame(Time_Stamp, columns = ['Time Stamp'])


# Functions 2

# Power Swing Impedance Calculations
# R Phase
Calcs['V1_R'] = Inst(Source_V1, Source_1_Freq, Calcs['Time Stamp'], Source_1_Voltage_Phi, 0, 0)
Calcs['V2_R'] = Inst(Source_V2, Source_2_Freq, Calcs['Time Stamp'], Source_2_Voltage_Phi, 0, 0)
Calcs['V1_R + V2_R'] = Calcs['V1_R'] + Calcs['V2_R']
Calcs['I1_R'] = Inst(Source_I1, Source_1_Freq, Calcs['Time Stamp'], Source_1_Current_Phi, 0, Busbar_comp)
Calcs['I2_R'] = Inst(Source_I2, Source_2_Freq, Calcs['Time Stamp'], Source_2_Current_Phi, 0, Busbar_comp)
Calcs['I1_R + I2_R'] = Calcs['I1_R'] + Calcs['I2_R']
Calcs['Z_R'] = Calcs['V1_R + V2_R'] / Calcs['I1_R + I2_R']

# S Phase
Calcs['V1_S'] = Inst(Source_V1, Source_1_Freq, Calcs['Time Stamp'], Source_1_Voltage_Phi, 240, 0)
Calcs['V2_S'] = Inst(Source_V2, Source_2_Freq, Calcs['Time Stamp'], Source_2_Voltage_Phi, 240, 0)
Calcs['V1_S + V2_S'] = Calcs['V1_S'] + Calcs['V2_S']
Calcs['I1_S'] = Inst(Source_I1, Source_1_Freq, Calcs['Time Stamp'], Source_1_Current_Phi, 240, Busbar_comp)
Calcs['I2_S'] = Inst(Source_I2, Source_2_Freq, Calcs['Time Stamp'], Source_2_Current_Phi, 240, Busbar_comp)
Calcs['I1_S + I2_S'] = Calcs['I1_S'] + Calcs['I2_S']
Calcs['Z_S'] = Calcs['V1_S + V2_S'] / Calcs['I1_S + I2_S']

# T Phase
Calcs['V1_T'] = Inst(Source_V1, Source_1_Freq, Calcs['Time Stamp'], Source_1_Voltage_Phi, 120, 0)
Calcs['V2_T'] = Inst(Source_V2, Source_2_Freq, Calcs['Time Stamp'], Source_2_Voltage_Phi, 120, 0)
Calcs['V1_T + V2_T'] = Calcs['V1_T'] + Calcs['V2_T']
Calcs['I1_T'] = Inst(Source_I1, Source_1_Freq, Calcs['Time Stamp'], Source_1_Current_Phi, 120, Busbar_comp)
Calcs['I2_T'] = Inst(Source_I2, Source_2_Freq, Calcs['Time Stamp'], Source_2_Current_Phi, 120, Busbar_comp)
Calcs['I1_T + I2_T'] = Calcs['I1_T'] + Calcs['I2_T']
Calcs['Z_T'] = Calcs['V1_T + V2_T'] / Calcs['I1_T + I2_T']



# Process Calculations

VR_Max = Calcs['V1_R + V2_R'].max()
VR_Min = Calcs['V1_R + V2_R'].min()
VR_Range = VR_Max - VR_Min
VR_Multiplier = VR_Range/Recording_decimal

VS_Max = Calcs['V1_S + V2_S'].max()
VS_Min = Calcs['V1_S + V2_S'].min()
VS_Range = VS_Max - VS_Min
VS_Multiplier = VS_Range/Recording_decimal

VT_Max = Calcs['V1_T + V2_T'].max()
VT_Min = Calcs['V1_T + V2_T'].min()
VT_Range = VT_Max - VT_Min
VT_Multiplier = VT_Range/Recording_decimal

IR_Max = Calcs['I1_R + I2_R'].max()
IR_Min = Calcs['I1_R + I2_R'].min()
IR_Range = IR_Max - IR_Min
IR_Multiplier = IR_Range/Recording_decimal

IS_Max = Calcs['I1_S + I2_S'].max()
IS_Min = Calcs['I1_S + I2_S'].min()
IS_Range = IS_Max - IS_Min
IS_Multiplier = IS_Range/Recording_decimal

IT_Max = Calcs['I1_T + I2_T'].max()
IT_Min = Calcs['I1_T + I2_T'].min()
IT_Range = IT_Max - IT_Min
IT_Multiplier = IT_Range/Recording_decimal


# Dat File

Calcs['VR_dat'] = int_conv(Calcs['V1_R + V2_R'], VR_Min, VR_Range, Recording_decimal)
Calcs['VS_dat'] = int_conv(Calcs['V1_S + V2_S'], VS_Min, VS_Range, Recording_decimal)
Calcs['VT_dat'] = int_conv(Calcs['V1_T + V2_T'], VT_Min, VT_Range, Recording_decimal)
Calcs['IR_dat'] = int_conv(Calcs['I1_R + I2_R'], VR_Min, VR_Range, Recording_decimal)
Calcs['IS_dat'] = int_conv(Calcs['I1_S + I2_S'], VS_Min, VS_Range, Recording_decimal)
Calcs['IT_dat'] = int_conv(Calcs['I1_T + I2_T'], VT_Min, VT_Range, Recording_decimal)


Dat_File = pd.DataFrame(Time_Stamp, columns = ['Time Stamp'])
Dat_File = Dat_File.merge(Calcs, on='Time Stamp', how='left')

Dat_File = Dat_File.drop(['V1_R', 'V2_R', 'V1_R + V2_R', 'I1_R', 'I2_R', 'I1_R + I2_R', 'Z_R'], axis = 'columns')
Dat_File = Dat_File.drop(['V1_S', 'V2_S', 'V1_S + V2_S', 'I1_S', 'I2_S', 'I1_S + I2_S', 'Z_S'], axis = 'columns')
Dat_File = Dat_File.drop(['V1_T', 'V2_T', 'V1_T + V2_T', 'I1_T', 'I2_T', 'I1_T + I2_T', 'Z_T'], axis = 'columns')
Dat_File['Time Stamp'] = (Dat_File['Time Stamp']*1000000).astype(int)


# CFG File

Output_1 = frame_op(1, 'VL1', 1, 'V', VR_Multiplier, VR_Min, Recording_decimal, VTP, VTS)
Output_2 = frame_op(2, 'VL2', 1, 'V', VS_Multiplier, VS_Min, Recording_decimal, VTP, VTS)
Output_3 = frame_op(3, 'VL3', 1, 'V', VT_Multiplier, VT_Min, Recording_decimal, VTP, VTS)
Output_4 = frame_op(4, 'IL1', 1, 'A', IR_Multiplier, IR_Min, Recording_decimal, CTP, CTS)
Output_5 = frame_op(5, 'IL2', 1, 'A', IS_Multiplier, IS_Min, Recording_decimal, CTP, CTS)
Output_6 = frame_op(6, 'IL3', 1, 'A', IT_Multiplier, IT_Min, Recording_decimal, CTP, CTS)

Outputs = pd.DataFrame([Output_1, Output_2, Output_3, Output_4, Output_5, Output_6])


System_Frequency = "50.00"
Next = "1"
Sampling_Rate = str(Sample_rate) + ", " + str(int(No_of_samples))
Trigger_Time = "23/01/2022,04:24:06.978389"
Stop_Time = "23/01/2022,04:24:07.078389"
Main_Format = "ASCII"
Final = "1.0"


# Output Files

CFG_filepath = "C:/Users/eoinc/OneDrive/Desktop/EC_Comtrade.cfg"

Dat_filepath = "C:/Users/eoinc/OneDrive/Desktop/EC_Comtrade.dat"


# Export Files

Output_s = Outputs.to_string(header=False, index=False)
Output_x = Header + "\n" + Output_Types + "\n" + Output_s + "\n" + System_Frequency + "\n" + Next + "\n" \
           + Sampling_Rate + "\n" + Trigger_Time + "\n" + Stop_Time + "\n" + Main_Format + "\n" + Final


with open(CFG_filepath, "w") as f:   # Opens file and casts as f
    f.write(Output_x) # Writing
    # File closed automatically


Dat_File = Dat_File.to_csv(header=False, index=True, sep=',')


with open(Dat_filepath, "w", newline = '') as g:   # Opens file and casts as f
    g.write(Dat_File)


print(Output_x)
#print(Dat_File)




