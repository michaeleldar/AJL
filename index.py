import sys
sys.stderr = 0

in_file = sys.argv[1]
out_file = sys.argv[2]

in_file_a = open(in_file, "r")
out_file_a = open(out_file, "w")

out_file_a.write("#include <iostream>\n")
out_file_a.write("using namespace std;\n")
out_file_a.write("int main()\n")
out_file_a.write("{\n")

in_file_b = in_file_a.read().split("\n")
for line in in_file_b:
    try:
        line_b = line.split()
        if line_b[0] == "write":
            out_file_a.write("cout << \"")
            out_file_a.write(line_b[1])
            out_file_a.write("\";\n")
    except:
        continue
out_file_a.write("}\n")