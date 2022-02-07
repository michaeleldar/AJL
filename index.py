import sys
sys.stderr = 0

in_file = sys.argv[1]
out_file = sys.argv[2]
ttype = "int "

in_file_a = open(in_file, "r")
out_file_a = open(out_file, "w")

def error(message):
    print("ERROR: ", message)
    quit(0)

out_file_a.write("#include <iostream>\n")
out_file_a.write("using namespace std;\n")
out_file_a.write("int main()\n")
out_file_a.write("{\n")

in_file_b = in_file_a.read().split("\n")
for line in in_file_b:
    try:
        line_b = line.split()
        if line_b[0] == "write":
            if line_b[1] == "var":
                out_file_a.write("cout << ")
                out_file_a.write(line_b[2])
                out_file_a.write(";\n")
            else:
                out_file_a.write("cout << \"")
                out_file_a.write(line_b[1])
                out_file_a.write("\";\n")
        elif line_b[0] == "var":
            assert line_b[2] == "=", error("No = in assignment")
            if type(line_b[3]) is str:
                ttype = "char "
            if ttype == "int ":
                out_file_a.write(ttype)
                out_file_a.write(line_b[1])
                out_file_a.write(" = ")
                out_file_a.write(line_b[3])
                out_file_a.write(";\n")
            elif ttype == "char ":
                out_file_a.write(ttype)
                out_file_a.write(line_b[1])
                out_file_a.write("[] = \"")
                out_file_a.write(line_b[3])
                out_file_a.write("\";\n")

    except:
        continue
        
out_file_a.write("}\n")