## Plotting from a text file
# Example of a comand line
# python3 POF_graphing -f file_1.txt  -x I_laser -y I_opc 
import matplotlib.pyplot as plt
import numpy as np
import argparse
#t = 10 #time of LED, 

#colors = ['red','red','red','black', 'black', 'black']

#colors = ['red', 'blue', 'green', 'orange','purple', 'black']

# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-f","--f", help = "Input File name")
parser.add_argument("-x", '--x', help = "x axis")
parser.add_argument("-y", '--y', help = "y axis")
args = vars(parser.parse_args())

plt.figure()
x = args['x']
y = args['y']
file_name = args['f']
info=np.loadtxt(file_name, comments='#', delimiter=',', skiprows=4)
laser_temp = info[:,0]
opc_temp = info[:,1]
I_laser = info[:,2]
V_laser = info[:,3]
V_opc = info[:,4]
I_opc = info[:,5]
p_opc = info[:,6]
#t = info[]
    
    
for i in x:

    if x == 'p_opc':
        x_var = p_opc
        title_x = "OPC Power"
        axis_x = "OPC Power (W)"
    elif x == 'laser_temp':
        x_var = laser_temp
        title_x = "Laser Temperture"
        axis_x = "Laser Temp (C)"
    elif x == 'opc_temp':
        x_var =  opc_temp
        title_x = "OPC Temperture"
        axis_x = "OPC Temp (C)"
    elif x == 'I_laser':
        x_var =   I_laser 
        title_x =  "Laser Current"
        axis_x = "Laser Current (A)"
    elif x == 'V_laser':
        x_var = V_laser
        title_x = "Laser Voltage"
        axis_x = "Laser Voltage (V)"
    elif x == 'V_opc':
        x_var = V_opc
        title_x = "OPC Voltage"
        axis_x = "OPC Voltage (V)"
    elif x == 'I_opc':
        x_var = I_opc
        title_x = "OPC Current"
        axis_x = "OPC Current (A)"
    else :
        print("invalid input for x axis")
        
    if y == 'p_opc':
        y_var = p_opc
        title_y = "OPC Power"
        axis_y = "OPC Power (W)"
    elif y == 'laser_temp':
        y_var = laser_temp
        title_y = "Laser Temperture"
        axis_y = "Laser Temp (C)"
    elif y == 'opc_temp':
        y_var =  opc_temp
        title_y = "OPC Temperture"
        axis_y = "OPC Temp (C)"
    elif y == 'I_laser':
        y_var =   I_laser  
        title_y =  "Laser Current"
        axis_y = "Laser Current (A)"
    elif y == 'V_laser':
        y_var = V_laser
        title_y = "Laser Voltage"
        axis_y = "Laser Voltage (V)"
    elif y == 'V_opc':
        y_var = V_opc
        title_y = "OPC Voltage"
        axis_y = "OPC Voltage (V)"
    elif y == 'I_opc':
        y_var = I_opc
        title_y = "OPC Current"
        axis_y = "OPC Current (A)"
    else :
        print("invalid input for y axis")
        
plt.plot(x_var,y_var)
title = title_x + " vs " + title_y
plt.title(title)
plt.xlabel(axis_x)
plt.ylabel(axis_y)
plt.show()

#plt.title("Photocurrent vs time")
#plt.legend(sys.argv[1:])
#plt.yscale("log")

plt.show()
