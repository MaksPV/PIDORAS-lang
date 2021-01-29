import sys

def main(c="", hex=False, show_code=False):
    c = c.replace(" ", "").replace("\n", "")
    cmds = {
    "П": "arr[i] = (arr[i] + 1) % 256",
    "И": "print(chr(arr[i]), end='')",
    "Д": "i = (i + 1) % 256",
    "О": "s = (s + 1) % 256",
    "Р": "yach()",
    "А": "arr[i]",
    "С": "arr[s]"
    }
    
    ops = {
    "*": "for _ in range(z):"
    }
    
    code = """arr = [0 for _ in range(256)]
i = 0
s = 0
    
def yach():
    global arr, i, s
    z = input()
    for x in range(len(z)):
        arr[(i + x) % 256] = ord(z[x]) % 256

"""
    k = 0
    num = ""
    is_skob = False
    
    for i in range(len(c)):
        try:
            if c[i] in cmds:
                code += k * "\t" + cmds[c[i]] + "\n"
            elif c[i] in ops:
                if c[i-1] in "АС":
                    num = cmds[c[i-1]]
                code += k * "\t" + ops[c[i]].replace("z", str(num)) + " "
                code += "\n"
                if c[i+1] != "(":
                    code += (k + 1)*"\t"
                num = ""
            elif c[i] in "0123456789":
                num += c[i]
            elif c[i] != "*" and c[i + 1] == "(":
                code += "def "+ c[i] + "():\n"
                code += 1 * "\t" + "global arr, i, s\n"
                is_skob = True
                cmds[c[i]] = c[i] + "()"
            elif c[i] == "(":
                k += 1
            elif c[i] == ")":
                k -= 1
    
        except:
            pass
    if hex: code += """print()
print()
for i in range(16):
    print(*arr[i*16:i*16+16])"""
    if show_code:
        print(code)
        print()
    exec(code)

if __name__ == "__main__":
    params = sys.argv
    hex = False
    show_code = False
    if len(params) < 2:
        print("No code")
        sys.exit()
    if "-" == params[1][0]:
        if "f" in params[1]:
            with open(" ".join(params[2:]), "r") as file:
                code = file.read()
                file.close()
        if "h" in params[1]:
            hex = True
        if "c" in params[1]:
            show_code = True
    if "f" not in params[1]:
        code = " ".join(params[1:])
    main(code, hex, show_code)
