import ast
import operator
import sys
from typing import NoReturn


def console_log(args):
    global variables
    output = []
    for arg in args:
        output.append(str(resolve(arg)))

    print(*output, sep="")


# --------------------


OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
}


def eval_expr(node):
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name):
        return variables[node.id]

    if isinstance(node, ast.BinOp):
        return OPS[type(node.op)](eval_expr(node.left), eval_expr(node.right))

    if isinstance(node, ast.UnaryOp):
        return OPS[type(node.op)](eval_expr(node.operand))

    raise ValueError("Invalid expression")


# resolve ----
def resolve(token):
    token = token.strip()

    if token == "endl":
        return ""
        
    if token in ("True", "False"):
        return token == "True"
        
    if token.startswith('"') and token.endswith('"'):
        return token[1:-1]
    try:
        tree = ast.parse(token, mode="eval")
        return eval_expr(tree.body)
    except Exception:
        error_print(f"Invalid token: {token}", mainindex)


def add_var(var_type, name, val) -> None:
    global variables
    if var_type == "int":
        variables[name] = int(val)
    elif var_type == "str":
        variables[name] = str(val)
    elif var_type == "bool":
        variables[name] = resolve(val)
    else:
        error_print("Wrong variable type",mainindex)
    

def error_print(msg, line) -> NoReturn:
    print(f"Error ar line {line}: {msg}")
    exit()


def check(args):
    condition = args[0]
    tokens = condition.split()
    
    #print("DEBBUG TOKKENS: ", tokens)
    # 
    if len(tokens) == 1:
        if tokens[0]:
            return bool(resolve(tokens[0]))
    elif len(tokens) < 3:
        error_print("Invalid condition", mainindex)
    final = True
    for i in range(0, len(tokens), 4):
        left = resolve(tokens[i])
        right = resolve(tokens[i + 2])
        op = tokens[i + 1]
        if op in (">", "<", "<=", ">="):
            try:
                left = int(left)
                right = int(right)
            except ValueError:
                print("invalid syntax for operations")
                break

        if op == "==":
            result = left == right
        elif op == "!=":
            result = left != right
        elif op == ">":
            result = left > right
        elif op == "<":
            result = left < right
        elif op == "<=":
            result = left <= right
        elif op == ">=":
            result = left >= right
     
        else:
            error_print(f"Invalid operator: {op}", mainindex)
            return False
        #if no operators -----
        if i == 0:
            final = result
        else:
            if logic in ["and", "or"]:
                logic = tokens[i - 1]
                if logic == "and":
                    final = final and result
                if logic == "or":
                    final = final or result
            else:
                error_print("Invalid logic operator", mainindex)
        #end logic operators -----
        
    print("DEBBUG RESULT: ", final)
    
    return final


def skipblock(parsed_lines, start):
    block_indent = parsed_lines[start]["indent"]
    i = start + 1
    while i < len(parsed_lines):
        if parsed_lines[i]["indent"] <= block_indent:
            return i
        i += 1
    return len(parsed_lines)


# MAIN LOOP
if len(sys.argv) < 2:
    print("Usage: python3 interpreter.py <file>")
    exit()

path = sys.argv[1]
with open(path, "r") as f:
    lines = f.readlines()

    parsed_lines = []
    for raw_line in lines:
        indent = len(raw_line) - len(raw_line.lstrip())
        parsed_lines.append({"indent": indent // 4, "code": raw_line.strip()})
    variables = {}
    mainindex = 0
    if_stack = []
    while mainindex < len(lines):
        line = lines[mainindex].strip()

        if not line:
            mainindex += 1
            continue

        if line == "else":
            if len(if_stack) == 0:
                print("Invalid: else without if")
                exit()
            result = if_stack.pop()
            if result:
                mainindex = skipblock(parsed_lines, mainindex)
                continue
            mainindex += 1
            continue

        # jesli funkcja
        if "(" in line and ")" in line:
            # ciecie agrumentow
            args = line[line.index("(") + 1 : line.rindex(")")]
            args = [a.strip() for a in args.split(",")]

            name = line[: line.index("(")].strip()

            # funkcje
            if name == "console_log":
                console_log(args)

            # IF --------------------------
            if name == "if":
                result = check(args)
                if_stack.append(result)
                # print("\nDEBBUG: ",args)
                # print("DEBBUG: ",result,"\n")

                if not result:
                    mainindex = skipblock(parsed_lines, mainindex)
                    continue
        # IF_END ---------------------

        # jesli variable +++++++++++++++++++++++++++++++++++++++
        else:
            parts = line.split()
            var_type = parts[0]
            name = parts[1]
            value = line.split("=", 1)[1].strip()
            if var_type == "bool":
                if value == "True":
                    variables[name] = True
                elif value == "False":
                    variables[name] = False
                else:
                    error_print(f"Invalid boolean value({value})", mainindex)
                
            elif var_type == "str":
                
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                else:
                    error_print("invalid syntax for string variable",mainindex)
                add_var(var_type,name, value)
            elif var_type == "int":
                try:
                    value = int(value)
                    add_var(var_type,name, value)
                except ValueError:
                    error_print("invalid syntax for integer variable",mainindex)
                    break
            elif parts[0] not in ("int", "str","bool") and "=" in line:
                name, expression = line.split("=", 1)

                name = name.strip()
                expression = expression.strip()
                if name in variables:
                    variables[name] = resolve(expression)
                if name not in variables:
                    error_print(f"Undefined variable: {name}", mainindex)

        mainindex += 1
