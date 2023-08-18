input_file_path = "/Users/linaliu/code/Lina-Liuna.github.io/Grade1.html"  # Replace with your input file's path
output_file_path = "/Users/linaliu/code/Lina-Liuna.github.io/Grade1.html"  # Replace with the desired output file's path
start_line = 9
end_line = 71

with open(input_file_path, 'r') as input_file:
    lines = input_file.readlines()

indented_lines = []
for index, line in enumerate(lines):
    if start_line <= index + 1 <= end_line:
        indented_lines.append('    ' + line)  # Adding 4 spaces before lines 10 to 100
    else:
        indented_lines.append(line)

with open(output_file_path, 'w') as output_file:
    output_file.writelines(indented_lines)
