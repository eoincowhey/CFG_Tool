# Power Swing Blocking Test Tool V1.00
# Developed by Eoin Cowhey
# Copyright Eoin Cowhey 2022

import pandas as pd
import numpy as np
import math

Name_version = "PSB Shishe V1.00"

Header = Name_version + ", 1997"
Output_Types = "6, 6A, 0D"

# Input information
Source_1_Freq = 50
Source_2_Freq = 49.5
V_Nom = 57.74
V_Fault = 30
Z_Finish = 20
Z_Start = 55
Source_1_Voltage_Phi = 0
Source_2_Voltage_Phi = 0
Source_1_Current_Phi = 0
Source_2_Current_Phi = 180

# Instrument transformers
VT_Primary = 220
VT_Secondary = 100
CT_Primary = 2500
CT_Secondary = 1
CT_Star_Point = "Busbar"

VTP = format(VT_Primary * 1000,'.2E')
VTS = format(VT_Secondary,'.2E')
CTP = format(CT_Primary,'.2E')
CTS = format(CT_Secondary,'.2E')


# Calc values
T_swing = 1/(Source_1_Freq-Source_2_Freq)
Source_V1 = V_Fault+(V_Nom-V_Fault)/2
Source_V2 = (V_Nom-V_Fault)/2
Source_I1 = ((V_Fault/Z_Finish)-(((V_Fault/Z_Finish)-(V_Nom/Z_Start))/2))
Source_I2 = (((V_Fault/Z_Finish)-(V_Nom/Z_Start))/2)
Z_rate = ((Z_Start-Z_Finish)/T_swing)/2
I_minimum = Source_I1-Source_I2

# Fault record process data
Recording_bits = 12
Recording_decimal = (2**Recording_bits)-1
Sample_rate = 2400  # e.g. 10 kHz
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


Sample_No = list_range(0, No_of_samples, 1)
Time_Stamp = list_range(Sample_t_res, (No_of_samples * Sample_t_res), Sample_t_res)


Calcs = pd.DataFrame(Time_Stamp, columns = ['Time Stamp'])


# Power Swing Impedance Calculations

# R Phase
Calcs['V1_R'] = Source_V1 * np.sin((2 * math.pi * Source_1_Freq * Calcs['Time Stamp']) + math.radians(Source_1_Voltage_Phi))
Calcs['V2_R'] = Source_V2 * np.sin((2 * math.pi * Source_2_Freq * Calcs['Time Stamp']) + math.radians(Source_2_Voltage_Phi))
Calcs['V1_R + V2_R'] = Calcs['V1_R'] + Calcs['V2_R']
Calcs['I1_R'] = Source_I1 * np.sin((2 * math.pi * Source_1_Freq * Calcs['Time Stamp']) + math.radians(Source_1_Current_Phi))
Calcs['I2_R'] = Source_I2 * np.sin((2 * math.pi * Source_2_Freq * Calcs['Time Stamp']) + math.radians(Source_2_Current_Phi))
Calcs['I1_R + I2_R'] = Calcs['I1_R'] + Calcs['I2_R']
Calcs['Z_R'] = Calcs['V1_R + V2_R'] / Calcs['I1_R + I2_R']

# S Phase
Calcs['V1_S'] = Source_V1 * np.sin((2 * math.pi * Source_1_Freq * Calcs['Time Stamp']) + math.radians(Source_1_Voltage_Phi) + math.radians(240))
Calcs['V2_S'] = Source_V2 * np.sin((2 * math.pi * Source_2_Freq * Calcs['Time Stamp']) + math.radians(Source_2_Voltage_Phi) + math.radians(240))
Calcs['V1_S + V2_S'] = Calcs['V1_S'] + Calcs['V2_S']
Calcs['I1_S'] = Source_I1 * np.sin((2 * math.pi * Source_1_Freq * Calcs['Time Stamp']) + math.radians(Source_1_Current_Phi) + math.radians(240))
Calcs['I2_S'] = Source_I2 * np.sin((2 * math.pi * Source_2_Freq * Calcs['Time Stamp']) + math.radians(Source_2_Current_Phi) + math.radians(240))
Calcs['I1_S + I2_S'] = Calcs['I1_S'] + Calcs['I2_S']
Calcs['Z_S'] = Calcs['V1_S + V2_S'] / Calcs['I1_S + I2_S']

# T Phase
Calcs['V1_T'] = Source_V1 * np.sin((2 * math.pi * Source_1_Freq * Calcs['Time Stamp']) + math.radians(Source_1_Voltage_Phi) + math.radians(120))
Calcs['V2_T'] = Source_V2 * np.sin((2 * math.pi * Source_2_Freq * Calcs['Time Stamp']) + math.radians(Source_2_Voltage_Phi) + math.radians(120))
Calcs['V1_T + V2_T'] = Calcs['V1_T'] + Calcs['V2_T']
Calcs['I1_T'] = Source_I1 * np.sin((2 * math.pi * Source_1_Freq * Calcs['Time Stamp']) + math.radians(Source_1_Current_Phi) + math.radians(120))
Calcs['I2_T'] = Source_I2 * np.sin((2 * math.pi * Source_2_Freq * Calcs['Time Stamp']) + math.radians(Source_2_Current_Phi) + math.radians(120))
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

Calcs['VR_dat'] = (((Calcs['V1_R + V2_R'] - VR_Min)/VR_Range) * Recording_decimal).astype('int')
Calcs['VS_dat'] = (((Calcs['V1_S + V2_S'] - VS_Min)/VS_Range) * Recording_decimal).astype('int')
Calcs['VT_dat'] = (((Calcs['V1_T + V2_T'] - VT_Min)/VT_Range) * Recording_decimal).astype('int')
Calcs['IR_dat'] = (((Calcs['I1_R + I2_R'] - IR_Min)/IR_Range) * Recording_decimal).astype('int')
Calcs['IS_dat'] = (((Calcs['I1_S + I2_S'] - IS_Min)/IS_Range) * Recording_decimal).astype('int')
Calcs['IT_dat'] = (((Calcs['I1_T + I2_T'] - IT_Min)/IT_Range) * Recording_decimal).astype('int')



Dat_File = pd.DataFrame(Time_Stamp, columns = ['Time Stamp'])
Dat_File = Dat_File.merge(Calcs, on='Time Stamp', how='left')

Dat_File = Dat_File.drop(['V1_R', 'V2_R', 'V1_R + V2_R','I1_R', 'I2_R', 'I1_R + I2_R', 'Z_R'], axis = 'columns')
Dat_File = Dat_File.drop(['V1_S', 'V2_S', 'V1_S + V2_S','I1_S', 'I2_S', 'I1_S + I2_S', 'Z_S'], axis = 'columns')
Dat_File = Dat_File.drop(['V1_T', 'V2_T', 'V1_T + V2_T','I1_T', 'I2_T', 'I1_T + I2_T', 'Z_T'], axis = 'columns')
Dat_File['Time Stamp'] = (Dat_File['Time Stamp']*1000000).astype(int)

print(Dat_File)


# CFG File

Output_1 = ['1',',','VL1',',', '1',',', 'V',',', VR_Multiplier,',', VR_Min,',', '0.00E+00',',', '0',',', Recording_decimal,',', VTP,',', VTS,',', 's']
Output_2 = ['2',',','VL2',',', '2',',', 'V',',', VS_Multiplier,',', VS_Min,',', '0.00E+00',',', '0',',', Recording_decimal,',', VTP,',', VTS,',', 's']
Output_3 = ['3',',', 'VL3',',', '3',',', 'V',',', VT_Multiplier,',', VT_Min,',', '0.00E+00',',', '0',',', Recording_decimal,',', VTP,',', VTS,',', 's']
Output_4 = ['4',',', 'IL1',',', '4',',', 'A',',', IR_Multiplier,',', IR_Min,',', '0.00E+00',',', '0',',', Recording_decimal,',', CTP,',', CTS,',', 's']
Output_5 = ['5',',', 'IL2',',', '5',',', 'A',',', IS_Multiplier,',', IS_Min,',', '0.00E+00',',', '0',',', Recording_decimal,',', CTP,',', CTS,',', 's']
Output_6 = ['6',',', 'IL3',',', '6',',', 'A',',', IT_Multiplier,',', IT_Min,',', '0.00E+00',',', '0',',', Recording_decimal,',', CTP,',', CTS,',', 's']

Outputs = pd.DataFrame([Output_1, Output_2, Output_3, Output_4, Output_5, Output_6])


System_Frequency = "50.00"
Next = "1"
Sampling_Rate = str(Sample_rate) + ", " + str(int(No_of_samples))
Trigger_Time = "23/01/2022,04:24:06.978389"
Stop_Time = "23/01/2022,04:24:07.078389"
Main_Format = "ASCII"
Final = "1.0"


# Output Files

#with open('CFG.txt') as t:
#    contents = t.read()

CFG_filepath = "C:/Users/eoinc/OneDrive/Desktop/Test123.CFG"

Dat_filepath = "C:/Users/eoinc/OneDrive/Desktop/Table123.DAT"



# Export Files

Output_s = Outputs.to_string(header=False, index=False)
Output_x = Header + "\n" + Output_Types + "\n" + Output_s + "\n" + System_Frequency + "\n" + Next + "\n" \
           + Sampling_Rate + "\n" + Trigger_Time + "\n" + Stop_Time + "\n" + Main_Format + "\n" + Final

print(Output_x)

with open(CFG_filepath, "w") as f:   # Opens file and casts as f
    f.write(Output_x)# + f.name)       # Writing
    # File closed automatically

# Dat_File.to_csv(filepath2, index=False, header=False)

Dat_File = Dat_File.to_csv(header=False, index=True, sep=',')


with open(Dat_filepath, "w") as g:   # Opens file and casts as f
    g.write(Dat_File)



print(Dat_File)





