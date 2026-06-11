import sys


def console_log(args):
    global variables
    output = []
    for arg in args:
        if arg.startswith('"') and arg.endswith('"'):
            output.append(arg[1:-1])
        else:
            output.append(str(variables[arg]))
    print(*output,sep="")

def var_int(name, val):
    global variables
    variables[name] = int(val)
    
def var_str(name,string):
    global variables
    variables[name] = str(string)

def check(args):
    condition = args[0]
    tokens = condition.split()
    
    

    final = True
    for i in range(0,len(tokens),4):
        left = tokens[i]
        if left in variables:
            left = variables[left]
        op = tokens[i+1]
        right = tokens[i+2]
        if right in variables:
            right = variables[right]
        if op == '>' or op == '<':
            try:
                left = int(left)
                right = int(right)
            except:
                print("invalid syntax for operations")
                break
        
        if op == '==':
            result = left == right
        elif op == '!=':
            result = left != right
        elif op == '>':
            result = left > right
        elif op == '<':
            result = left < right
        else:
            print("invalid syntax for operatons")
            exit()
        if i == 0:
            final = result
        else:
            logic = tokens[i-1]
            if logic == "and":
                final = final and result
            if logic == 'or':
                final = final or result
        
        
        lastresult = result
    
    return final

    
#MAIN LOOP
if len(sys.argv) < 2:
    print("Usage: python3 interpreter.py <file>")
    exit()

path = sys.argv[1]
with open(path, "r") as f:
    lines = f.readlines()
    
    parsed_lines = []
    for raw_line in lines:  
        indent = len(raw_line) - len(raw_line.lstrip())
        parsed_lines.append({
                "indent": indent//4,
                "code": raw_line.strip()
        })
    variables = {}
    mainindex = 0
    currentindent = 0
    while mainindex < len(lines):
        
        line = lines[mainindex]
        line = line.strip()
        
        parts = line.strip()
        
        if not line:
            continue
            
        #jesli funkcja 
        if "(" in line and ")" in line:
            #ciecie agrumentow
            args = line[line.index("(")+1:line.rindex(")")]
            args = [a.strip() for a in args.split(",")]
            
            name = line[:line.index("(")].strip()

            #funkcje
            if name == "console_log":
                console_log(args)

                
            if name == "if":
              
                result = check(args)
                print("\nDEBBUG: ",args)
                print("DEBBUG: ",result,"\n")
    
                if not result:
                    blockindent = parsed_lines[mainindex]["indent"]
                    while mainindex + 1 < len(parsed_lines):
                        mainindex+=1
                        
                        if parsed_lines[mainindex]["indent"] <= blockindent:
                            mainindex-=1
                            break
                    
                
 
        #jesli variable
        else:
            parts = line.split()
            
            if parts[0] == "str":
               name = parts[1]
               value = line.split("=",1)[1].strip()
               if value.startswith('"') and value.endswith('"'):
                   value = value[1:-1]
               else:
                   print("invalid syntax for string variable")
                   break
               var_str(name,value)
            if parts[0] == "int":
                name = parts[1]
                value = line.split("=",1)[1].strip()
                try:
                    value = int(value)
                    var_int(name,value)
                except ValueError:
                    print("invalid syntax for integer variable")
                    break
        
        mainindex+=1
