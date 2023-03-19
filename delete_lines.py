import sys

if len(sys.argv) != 3:
    print("Usage: python3 program.py input.xyz output.xyz")
    sys.exit(1)

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

# Open the input file
with open(input_file_name, 'r') as input_file:
    # Read all the lines from the input file
    lines = input_file.readlines()

# Open the output file
with open(output_file_name, 'w') as output_file:
    # Write every 40th line to the output file
    for i in range(0, len(lines), 40):
        output_file.write(lines[i])
