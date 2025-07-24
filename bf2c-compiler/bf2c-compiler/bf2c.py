# bf2c.py - Brainfuck to C Compiler by Sagnik Sannigrahi

import os

def compile_brainfuck_to_c(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            code = f.read()
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        return

    # Filter only valid Brainfuck commands
    valid_ops = {'>', '<', '+', '-', '.', ',', '[', ']'}
    code = [char for char in code if char in valid_ops]

    c_code = [
        "#include <stdio.h>",
        "int main() {",
        "    char array[30000] = {0};",
        "    char *ptr = array;"
    ]

    indent = "    "
    for char in code:
        if char == '>':
            c_code.append(indent + "++ptr;")
        elif char == '<':
            c_code.append(indent + "--ptr;")
        elif char == '+':
            c_code.append(indent + "++*ptr;")
        elif char == '-':
            c_code.append(indent + "--*ptr;")
        elif char == '.':
            c_code.append(indent + "putchar(*ptr);")
        elif char == ',':
            c_code.append(indent + "*ptr = getchar();")
        elif char == '[':
            c_code.append(indent + "while (*ptr) {")
            indent += "    "
        elif char == ']':
            indent = indent[:-4]
            c_code.append(indent + "}")

    c_code.append("    return 0;")
    c_code.append("}")

    # Write to output .c file
    with open(output_file, 'w') as f:
        f.write('\n'.join(c_code))

    print(f"✅ Compilation Complete! C code saved to: {output_file}")

# ====== Main ======
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python bf2c.py <input.bf> <output.c>")
    else:
        compile_brainfuck_to_c(sys.argv[1], sys.argv[2])

