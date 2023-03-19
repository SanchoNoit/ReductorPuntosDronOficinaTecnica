import sys

# Importando paquetes de interfaz gráfica

import easygui
from Tkinter import Tk # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

#################################################################################

if len(sys.argv) != 3:
    print("Usage: python3 program.py input.xyz output.xyz")
    sys.exit(1)

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

input_file_name = askopenfilename()

output_file_name = easygui.enterbox("Nombre del archivo resultante: ")

# Open the input file
with open(input_file_name, 'r') as input_file:
    # Read all the lines from the input file
    lines = input_file.readlines()

# Open the output file
with open(output_file_name, 'w') as output_file:
    # Write every 40th line to the output file
    for i in range(0, len(lines), 40):
        output_file.write(lines[i])
